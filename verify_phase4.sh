#!/bin/bash
# Quick verification script for Phase 4 completion

echo "╔═══════════════════════════════════════════════════════════════════════╗"
echo "║            PHASE 4 VERIFICATION CHECKLIST                             ║"
echo "╚═══════════════════════════════════════════════════════════════════════╝"
echo ""

# Check files exist
echo "📁 Checking Files..."
files=(
  "coordination_lib.py"
  "agent_start.py"
  "claim_issue.py"
  "propose_fix.py"
  "apply_fix.py"
  "release_issue.py"
)

for file in "${files[@]}"; do
  if [ -f "$file" ] && [ -x "$file" ]; then
    echo "  ✅ $file"
  else
    echo "  ❌ $file (missing or not executable)"
  fi
done

echo ""
echo "📊 System Statistics..."
total_issues=$(cat issues/index.json | python3 -c "import sys, json; print(json.load(sys.stdin)['total_issues'])")
total_fixes=$(cat fixes/index.json | python3 -c "import sys, json; print(json.load(sys.stdin)['total_fixes'])")
echo "  • Total Issues: $total_issues"
echo "  • Total Fixes: $total_fixes"

echo ""
echo "🔍 Testing Basic Functionality..."
echo "  • Testing agent_start.py..."
python3 agent_start.py --agent claude_code 2>&1 | grep -q "Starting claude_code" && echo "    ✅ WORKS" || echo "    ❌ FAILED"

echo ""
echo "✅ Phase 4 verification complete!"
