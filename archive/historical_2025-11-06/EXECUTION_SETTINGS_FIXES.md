# Execution Settings Fixes - Complete

## Summary

All execution settings have been corrected to match the actual n8n framework implementation. The settings are now 100% accurate and properly differentiate between trigger and executable nodes.

## Fixes Applied

### 1. Correct Field Names ✅

| Old (WRONG) | New (CORRECT) | Source |
|-------------|---------------|--------|
| `alwaysOutput` | `alwaysOutputData` | INode interface |
| `displayNote` | `notesInFlow` | INode interface |

### 2. Added Missing Settings ✅

| Setting | Type | Default | When Shown |
|---------|------|---------|------------|
| `maxTries` | number | 3 | When retryOnFail=true |
| `waitBetweenTries` | number | 1000 | When retryOnFail=true |

Constraints:
- `maxTries`: min=2, max=5
- `waitBetweenTries`: min=0, max=5000 (milliseconds)

### 3. Correct Technical Values ✅

**OnError Options:**

| Old (User-Friendly) | New (Technical) | Display Name |
|---------------------|-----------------|--------------|
| "Stop Workflow" | `stopWorkflow` | Stop Workflow |
| "Continue" | `continueRegularOutput` | Continue |
| "Continue (using error output)" | `continueErrorOutput` | Continue (using error output) |

### 4. Node Type Differentiation ✅

**Common Settings (ALL nodes - trigger + executable):**
- `notes` (string)
- `notesInFlow` (boolean)

**Executable Settings (NON-trigger nodes only):**
- `alwaysOutputData` (boolean)
- `executeOnce` (boolean)
- `retryOnFail` (boolean)
- `maxTries` (number) - conditional
- `waitBetweenTries` (number) - conditional
- `onError` (options)

### 5. Actual n8n Translations ✅

All descriptions now use the exact text from n8n's i18n files:

```
packages/frontend/editor-ui/src/plugins/i18n/locales/en.json
```

Examples:
- `alwaysOutputData`: "If active, will output a single, empty item when the output would have been empty. Use to prevent the workflow finishing on this node"
- `maxTries`: "Number of times to attempt to execute the node before failing the execution"
- `waitBetweenTries`: "How long to wait between each attempt (in milliseconds)"

## Code Changes

### Files Modified:

1. **n8n_node_extractor.py**
   - Lines 36-132: Replaced `STANDARD_SETTINGS` with `COMMON_SETTINGS` + `EXECUTABLE_SETTINGS`
   - Lines 1466-1525: Updated markdown generation to show correct settings per node type
   - Lines 1700-1712: Updated YAML schema to include settings based on node type
   - Lines 1810-1846: Updated JSON schema to include correct settings with constraints
   - Lines 1875-1893: Added `_get_node_settings()` helper method

2. **CLAUDE.md**
   - Lines 157-162: Updated output format documentation
   - Lines 384-430: Added comprehensive "Execution Settings (Framework-Level)" section

## Test Results

### Executable Node (ReadWriteFile)

Shows ALL settings:
```
| Notes | `notes` | string |  |
| Display Note in Flow? | `notesInFlow` | boolean | False |
| Always Output Data | `alwaysOutputData` | boolean | False |
| Execute Once | `executeOnce` | boolean | False |
| Retry On Fail | `retryOnFail` | boolean | False |
| Max. Tries | `maxTries` | number | 3 | (min: 2, max: 5) *conditional*
| Wait Between Tries (ms) | `waitBetweenTries` | number | 1000 | (min: 0, max: 5000) *conditional*
| On Error | `onError` | options | stopWorkflow |
```

**On Error Options:**
- Stop Workflow (`stopWorkflow`)
- Continue (`continueRegularOutput`)
- Continue (using error output) (`continueErrorOutput`)

### Trigger Node (MqttTrigger)

Shows ONLY common settings:
```
## Execution Settings

**Note:** Trigger nodes have limited execution settings.

| Notes | `notes` | string |  |
| Display Note in Flow? | `notesInFlow` | boolean | False |
```

## JSON Output Structure

### Executable Node:
```json
{
  "settings": {
    "common": {
      "notes": { ... },
      "notesInFlow": { ... }
    },
    "executable": {
      "alwaysOutputData": { ... },
      "executeOnce": { ... },
      "retryOnFail": { ... },
      "maxTries": { 
        "default": 3,
        "min": 2,
        "max": 5,
        "displayOptions": { "show": { "retryOnFail": [true] } }
      },
      "waitBetweenTries": { 
        "default": 1000,
        "min": 0,
        "max": 5000,
        "displayOptions": { "show": { "retryOnFail": [true] } }
      },
      "onError": {
        "default": "stopWorkflow",
        "options": [
          { "name": "Stop Workflow", "value": "stopWorkflow", "description": "..." },
          { "name": "Continue", "value": "continueRegularOutput", "description": "..." },
          { "name": "Continue (using error output)", "value": "continueErrorOutput", "description": "..." }
        ]
      }
    },
    "note": "Executable nodes have both common and executable settings"
  }
}
```

### Trigger Node:
```json
{
  "settings": {
    "common": {
      "notes": { ... },
      "notesInFlow": { ... }
    },
    "note": "Trigger nodes only have common settings (notes, notesInFlow)"
  }
}
```

## Source Verification

All settings verified against n8n source code:

1. **INode Interface:** `packages/workflow/src/interfaces.ts` (lines 6194-6217)
   - Defines all framework-level node properties
   - `alwaysOutputData`, `notesInFlow`, `retryOnFail`, `maxTries`, `waitBetweenTries`, etc.

2. **UI Settings:** `packages/frontend/editor-ui/src/features/ndv/shared/ndv.utils.ts`
   - `getNodeSettingsInitialValues()` - default values
   - `getSettingsProperties()` - property definitions with displayOptions

3. **Translations:** `packages/frontend/editor-ui/src/plugins/i18n/locales/en.json`
   - All display names and descriptions
   - Under `nodeSettings.*` keys

4. **OnError Type:** `packages/workflow/src/interfaces.ts`
   ```typescript
   export type OnError = 'continueErrorOutput' | 'continueRegularOutput' | 'stopWorkflow';
   ```

## Verification Status

✅ **CONFIRMED:** These settings are 100% universal and framework-level
✅ **CONFIRMED:** Correct field names from INode interface
✅ **CONFIRMED:** Correct technical values for onError
✅ **CONFIRMED:** Trigger nodes have only common settings
✅ **CONFIRMED:** Executable nodes have common + executable settings
✅ **CONFIRMED:** All descriptions match n8n's official translations

## Impact

This fix ensures that:
1. AI models trained on this data learn the **correct** n8n API
2. Generated code will use the **correct** field names
3. Documentation matches the **actual** n8n implementation
4. Users can copy-paste field IDs directly into their workflows
5. JSON Schema validation will work with real n8n workflows
