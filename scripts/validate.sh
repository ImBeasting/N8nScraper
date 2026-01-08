#!/bin/bash
# Unified validation script for N8nScraper
# Runs extraction validation and coordination health checks
# Returns exit code for CI/CD integration

set -e  # Exit on first error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Project root (assumes script is in scripts/ subdirectory)
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_ROOT"

echo "==============================================="
echo "N8nScraper Validation Suite"
echo "==============================================="
echo ""

VALIDATION_PASSED=true

# ============================================
# 1. EXTRACTION QUALITY VALIDATION
# ============================================
echo "1. Running extraction validation..."
echo "   Command: python3 validate_extraction.py"
echo ""

if python3 validate_extraction.py > /tmp/n8n_validation.log 2>&1; then
    echo -e "${GREEN}✓ Extraction validation completed${NC}"

    # Check for critical issues
    ZERO_PROPS=$(grep "Nodes with 0 properties:" /tmp/n8n_validation.log | grep -oP '\d+' | head -1 || echo "0")
    NULL_DISPLAYS=$(grep "Properties with null displayName:" /tmp/n8n_validation.log | grep -oP '\d+' | head -1 || echo "0")
    TEMPLATE_VARS=$(grep "Files with template variables:" /tmp/n8n_validation.log | grep -oP '\d+' | head -1 || echo "0")

    echo "   - Zero properties: $ZERO_PROPS (target: ≤1)"
    echo "   - Null displayNames: $NULL_DISPLAYS (target: 0)"
    echo "   - Template variables: $TEMPLATE_VARS (target: 0)"

    # NoOp is the only valid zero-property node
    if [ "$ZERO_PROPS" -gt 1 ]; then
        echo -e "${RED}✗ CRITICAL: More than 1 zero-property node detected${NC}"
        VALIDATION_PASSED=false
    fi

    if [ "$NULL_DISPLAYS" -gt 0 ]; then
        echo -e "${RED}✗ CRITICAL: Null displayNames detected${NC}"
        VALIDATION_PASSED=false
    fi

    if [ "$TEMPLATE_VARS" -gt 0 ]; then
        echo -e "${YELLOW}⚠ WARNING: Unresolved template variables detected${NC}"
    fi
else
    echo -e "${RED}✗ Extraction validation failed${NC}"
    cat /tmp/n8n_validation.log
    VALIDATION_PASSED=false
fi
echo ""

# ============================================
# 2. COORDINATION HEALTH CHECK
# ============================================
echo "2. Checking coordination health..."

# Check for stale locks (>60 minutes old)
STALE_LOCKS=0
if [ -d "collaboration" ]; then
    while IFS= read -r -d '' lock_dir; do
        if [ -f "$lock_dir/lock_info.json" ]; then
            LOCK_TIME=$(jq -r '.locked_at' "$lock_dir/lock_info.json")
            LOCK_EPOCH=$(date -d "$LOCK_TIME" +%s 2>/dev/null || echo "0")
            NOW_EPOCH=$(date +%s)
            AGE_MINUTES=$(( (NOW_EPOCH - LOCK_EPOCH) / 60 ))

            if [ "$AGE_MINUTES" -gt 60 ]; then
                LOCKED_BY=$(jq -r '.locked_by' "$lock_dir/lock_info.json")
                echo -e "${YELLOW}⚠ Stale lock found: $(basename "$lock_dir") (age: ${AGE_MINUTES}m, owner: $LOCKED_BY)${NC}"
                STALE_LOCKS=$((STALE_LOCKS + 1))
            fi
        fi
    done < <(find collaboration -type d -name "*.lock" -print0 2>/dev/null)

    if [ "$STALE_LOCKS" -eq 0 ]; then
        echo -e "${GREEN}✓ No stale locks detected${NC}"
    else
        echo -e "${YELLOW}⚠ Found $STALE_LOCKS stale lock(s) - run cleanup.sh${NC}"
    fi
else
    echo -e "${YELLOW}⚠ No collaboration directory found (first run?)${NC}"
fi
echo ""

# ============================================
# 3. FILE PAIR CONSISTENCY
# ============================================
echo "3. Checking file pair consistency..."

if [ -d "extracted_docs" ]; then
    JSON_COUNT=$(find extracted_docs -name "*_data.json" | wc -l)
    MD_COUNT=$(find extracted_docs -name "*_documentation.md" | wc -l)

    echo "   - JSON files: $JSON_COUNT"
    echo "   - Markdown files: $MD_COUNT"

    if [ "$JSON_COUNT" -eq "$MD_COUNT" ]; then
        echo -e "${GREEN}✓ File pairs are balanced${NC}"
    else
        echo -e "${RED}✗ File pair mismatch (JSON: $JSON_COUNT, MD: $MD_COUNT)${NC}"
        VALIDATION_PASSED=false
    fi
else
    echo -e "${YELLOW}⚠ No extracted_docs directory found${NC}"
fi
echo ""

# ============================================
# 4. QUALITY METRICS SUMMARY
# ============================================
echo "4. Quality metrics summary..."

if [ -f "validation_report.json" ]; then
    TOTAL_FILES=$(jq '.stats.total_data_files' validation_report.json)
    DUPLICATE_GROUPS=$(jq '.stats.duplicate_groups' validation_report.json)

    echo "   - Total nodes extracted: $TOTAL_FILES"
    echo "   - Duplicate groups: $DUPLICATE_GROUPS (target: 0)"

    if [ "$DUPLICATE_GROUPS" -gt 0 ]; then
        echo -e "${YELLOW}⚠ Duplicate file groups detected${NC}"
    fi
else
    echo -e "${YELLOW}⚠ No validation_report.json found - run validate_extraction.py first${NC}"
fi
echo ""

# ============================================
# FINAL RESULT
# ============================================
echo "==============================================="
if [ "$VALIDATION_PASSED" = true ]; then
    echo -e "${GREEN}✓ VALIDATION PASSED${NC}"
    echo "==============================================="
    exit 0
else
    echo -e "${RED}✗ VALIDATION FAILED${NC}"
    echo "==============================================="
    echo ""
    echo "See full validation output at: /tmp/n8n_validation.log"
    exit 1
fi
