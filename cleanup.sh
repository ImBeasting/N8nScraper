#!/bin/bash
# Cleanup Script: Remove stale locks and archive old logs

echo "=== Multi-Agent Coordination Cleanup ==="
echo ""

cd "/media/tyler/fastraid/Projects/n8n Node Scrapper"

# Remove stale locks (>2 hours)
echo "Removing stale locks (>2 hours old)..."
stale=$(find collaboration/ -name "*.lock" -mmin +120 2>/dev/null)
if [ -z "$stale" ]; then
    echo "  No stale locks to remove"
else
    find collaboration/ -name "*.lock" -mmin +120 -delete
    echo "  ✅ Removed stale locks"
fi
echo ""

# Archive old audit logs (>30 days)
echo "Archiving old audit logs..."
mkdir -p collaboration/archives
if [ -f "collaboration/audit_log.jsonl" ]; then
    size=$(stat -f%z collaboration/audit_log.jsonl 2>/dev/null || stat -c%s collaboration/audit_log.jsonl)
    if [ $size -gt 10485760 ]; then  # 10MB
        timestamp=$(date +%Y%m%d_%H%M%S)
        mv collaboration/audit_log.jsonl "collaboration/archives/audit_log_${timestamp}.jsonl"
        touch collaboration/audit_log.jsonl
        gzip "collaboration/archives/audit_log_${timestamp}.jsonl"
        echo "  ✅ Archived audit log (${size} bytes)"
    else
        echo "  Audit log size OK (${size} bytes)"
    fi
fi
echo ""

# Clean old backups (>60 days)
echo "Cleaning old backups..."
if [ -d "reports/backups" ]; then
    find reports/backups/ -name "*.md" -mtime +60 -delete 2>/dev/null
    count=$(find reports/backups/ -name "*.md" | wc -l)
    echo "  Current backups: $count files"
fi
echo ""

echo "=== Cleanup Complete ==="
