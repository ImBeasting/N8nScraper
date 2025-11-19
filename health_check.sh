#!/bin/bash
# Multi-Agent Coordination Health Check Script

echo "=== Multi-Agent Coordination Health Check ==="
echo ""

cd "/media/tyler/fastraid/Projects/n8n Node Scrapper"

# Check for stale locks
echo "Checking for stale locks (>60 minutes)..."
stale=$(find collaboration/ -name "*.lock" -mmin +60 2>/dev/null)
if [ -z "$stale" ]; then
    echo "  ✅ No stale locks found"
else
    echo "  ⚠️  Found stale locks:"
    echo "$stale" | while read lock; do
        echo "    - $lock"
    done
fi
echo ""

# Check agent heartbeats
echo "Checking agent heartbeats..."
python3 - << 'PYTHON'
import json
from datetime import datetime, timedelta

with open('collaboration/agent_heartbeats.json') as f:
    heartbeats = json.load(f)

now = datetime.now()
for agent, data in heartbeats.items():
    if data['timestamp']:
        last = datetime.fromisoformat(data['timestamp'])
        if now - last > timedelta(minutes=5):
            print(f'  ⚠️  {agent} heartbeat stale ({(now - last).seconds // 60} min old)')
        else:
            print(f'  ✅ {agent} heartbeat active')
    else:
        print(f'  ℹ️  {agent} never started')
PYTHON
echo ""

# Check report freshness
echo "Checking report freshness..."
if [ -f "reports/generation_metadata.json" ]; then
    python3 - << 'PYTHON'
import json
from datetime import datetime, timedelta

with open('reports/generation_metadata.json') as f:
    meta = json.load(f)

last_gen = datetime.fromisoformat(meta['last_generated'])
age = (datetime.now() - last_gen).seconds // 60

if age < 120:
    print(f'  ✅ Reports generated {age} minutes ago')
else:
    print(f'  ⚠️  Reports stale ({age} minutes old)')
PYTHON
else
    echo "  ⚠️  No generation metadata found"
fi
echo ""

# File structure check
echo "Checking directory structure..."
for dir in collaboration issues fixes reports; do
    if [ -d "$dir" ]; then
        echo "  ✅ $dir/ exists"
    else
        echo "  ❌ $dir/ missing"
    fi
done
echo ""

# Count issues and fixes
echo "Statistics:"
python3 - << 'PYTHON'
import json

with open('issues/index.json') as f:
    issues = json.load(f)
with open('fixes/index.json') as f:
    fixes = json.load(f)

print(f'  Total Issues: {issues["total_issues"]}')
print(f'  Total Fixes: {fixes["total_fixes"]}')
print(f'  Unresolved Issues: {issues["by_status"].get("new", 0) + issues["by_status"].get("in_progress", 0)}')
PYTHON
echo ""

echo "=== Health Check Complete ==="
