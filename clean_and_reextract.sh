#!/bin/bash
# Clean and re-extract all nodes with new fixes

echo "========================================"
echo "CLEAN RE-EXTRACTION SCRIPT"
echo "========================================"
echo ""

# Step 1: Backup existing files
echo "Step 1: Creating backup..."
if [ -d "extracted_docs" ]; then
    BACKUP_DIR="extracted_docs_backup_$(date +%Y%m%d_%H%M%S)"
    cp -r extracted_docs "$BACKUP_DIR"
    echo "  ✓ Backup created: $BACKUP_DIR"
else
    echo "  ! No extracted_docs directory found"
fi

# Step 2: Clean extracted_docs
echo ""
echo "Step 2: Cleaning extracted_docs directory..."
rm -rf extracted_docs/*
echo "  ✓ Directory cleaned"

# Step 3: Re-extract all nodes
echo ""
echo "Step 3: Re-extracting all nodes..."
echo "  This will take 30-60 minutes for 530+ nodes..."
echo ""
python3 n8n_node_extractor.py extract-all 2>&1 | tee extraction_full.log

# Step 4: Run validation
echo ""
echo "Step 4: Running validation..."
python3 validate_extraction.py

echo ""
echo "========================================"
echo "COMPLETE! Check validation results above"
echo "========================================"
