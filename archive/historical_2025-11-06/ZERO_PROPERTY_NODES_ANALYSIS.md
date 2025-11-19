# Zero-Property Nodes Analysis

## Node 1: NoOp ✅ CORRECT BY DESIGN

**File:** `n8n/packages/nodes-base/nodes/NoOp/NoOp.node.ts`

**Source code (line 24):**
```typescript
properties: [],
```

**Analysis:** This node intentionally has zero properties. It's a "No Operation" node that passes data through without any configuration options. This is correct behavior.

**Status:** ✅ **No fix needed** - Working as intended

---

## Node 2: OnfleetTrigger ❌ EXTRACTION BUG

**File:** `n8n/packages/nodes-base/nodes/Onfleet/OnfleetTrigger.node.ts`

**Source code (line 51):**
```typescript
properties: [eventDisplay, eventNameField],
```

**Imported from (line 12):**
```typescript
import { eventDisplay, eventNameField } from './descriptions/OnfleetWebhookDescription';
```

**Actual properties defined in `OnfleetWebhookDescription.ts`:**
```typescript
export const eventDisplay: INodeProperties = {
  displayName: 'Trigger On',
  name: 'triggerOn',
  type: 'options',
  // ... full property object
};

export const eventNameField = {
  displayName: 'Additional Fields',
  name: 'additionalFields',
  type: 'collection',
  // ... full property object
} as INodeProperties;
```

**Root Cause:**

The properties array contains **bare identifier references** to imported property objects:
- `[eventDisplay, eventNameField]` ← Direct references
- NOT `[{...}, {...}]` ← Object literals
- NOT `[...eventDisplay, ...eventNameField]` ← Spread operators

The extractor's `_split_into_objects()` function only handles:
1. Object literals `{...}` (tracked by brace depth)
2. Spread operators `...identifier`
3. But NOT bare identifier references

**Fix Required:**

Enhance `_split_into_objects()` to detect and resolve bare identifier references as if they were spread operators.

**Pattern to detect:**
- Comma-separated identifiers: `identifier1, identifier2`
- Not starting with `{` (object literal)
- Not starting with `...` (spread operator)
- Match pattern: `\w+` (word characters only)

**Implementation:**
Treat bare identifiers like spread operators for resolution purposes, since they both require looking up imported/exported definitions.

---

## Summary

- **NoOp:** ✅ Correct (0 properties by design)
- **OnfleetTrigger:** ❌ Bug (should have 2 properties)

**Next step:** Implement bare identifier resolution in extractor

---

## Fix Implemented ✅

**Enhancement:** Bare Identifier Resolution in Properties Arrays

**Code Changes:**

1. **Modified `_split_into_objects()` (lines 936-970)**
   - Added detection for bare identifiers (e.g., `eventDisplay, eventNameField`)
   - Changed comma handling: triggers item separation at depth 0
   - Treats bare identifiers as "spreads" for resolution purposes

2. **Added `extract_exported_property()` (lines 475-513)**
   - Extracts single property objects (not arrays)
   - Handles both typed and untyped exports:
     - `export const name: INodeProperties = {...}`
     - `export const name = {...} as INodeProperties`

3. **Enhanced `_resolve_spreads()` (lines 1074-1082)**
   - Falls back to `extract_exported_property()` when array extraction returns empty
   - Supports both array and single property references

**Test Results:**

Before fix:
```
✓ Extracted 0 properties
```

After fix:
```
✓ Extracted 2 properties
  - triggerOn (Trigger On) - options type
  - additionalFields (Additional Fields) - collection type
```

**Impact:** 
- Fixes OnfleetTrigger (2 properties extracted)
- Supports pattern used by other nodes with imported property references
- Zero-property nodes: 2 → 1 (only NoOp remains, which is correct)

**Status:** ✅ COMPLETE
