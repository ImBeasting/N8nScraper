#!/usr/bin/env python3
"""Test _split_into_objects function"""

from pathlib import Path
import re

# Sample content from HTTP Request options array
test_content = """
			{
				displayName: 'Batching',
				name: 'batching',
				placeholder: 'Add Batching',
				type: 'fixedCollection',
				typeOptions: {
					multipleValues: false,
				},
				default: {
					batch: {},
				},
				options: [
					{
						displayName: 'Batching',
						name: 'batch',
						values: [
							{
								displayName: 'Items per Batch',
								name: 'batchSize',
								type: 'number',
								typeOptions: {
									minValue: -1,
								},
								default: 50,
								description:
									'Input will be split in batches to throttle requests. -1 for disabled. 0 will be treated as 1.',
							},
						],
					},
				],
			},
			{
				displayName: 'Ignore SSL Issues (Insecure)',
				name: 'allowUnauthorizedCerts',
				type: 'boolean',
				noDataExpression: true,
				default: false,
				description:
					'Whether to download the response even if SSL certificate validation is not possible',
			}
"""

def _split_into_objects_debug(text):
    """Debug version with logging"""
    objects = []
    spreads = []
    depth = 0
    current = ""
    i = 0

    print(f"Input length: {len(text)} chars")
    print(f"First 100 chars: {text[:100]}")

    while i < len(text):
        char = text[i]

        if char == '{':
            depth += 1
            if i < 50:
                print(f"  [{i}] '{char}' -> depth={depth}")
        elif char == '}':
            depth -= 1
            if i < 300 or (depth == 0 and i > 300):
                print(f"  [{i}] '{char}' -> depth={depth}, current_len={len(current)}")
        elif char == ',' and depth == 0:
            print(f"  [{i}] Found comma at depth 0, saving object (len={len(current.strip())})")
            cleaned = current.strip()
            if cleaned and not cleaned.startswith('...'):
                if re.match(r'^\w+$', cleaned):
                    spreads.append(cleaned)
                else:
                    objects.append(cleaned)
                    print(f"    -> Saved object #{len(objects)}")
            current = ""
            i += 1
            continue

        current += char
        i += 1

    # Handle remaining content
    if current.strip() and depth == 0:
        cleaned = current.strip().rstrip(',').strip()
        print(f"  End: Remaining content (len={len(cleaned)}), depth={depth}")
        if cleaned and cleaned != ',' and not cleaned.startswith('...'):
            if re.match(r'^\w+$', cleaned):
                spreads.append(cleaned)
            else:
                objects.append(cleaned)
                print(f"    -> Saved final object #{len(objects)}")

    return objects, spreads

objects, spreads = _split_into_objects_debug(test_content)
print(f"\nResult: {len(objects)} objects, {len(spreads)} spreads")
print(f"\nFirst object preview (first 200 chars):")
if objects:
    print(objects[0][:200])
