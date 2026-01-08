#!/usr/bin/env python3
"""Debug script to test collection parsing"""

import re
from pathlib import Path

# Read the Description.ts file
desc_file = Path("n8n/packages/nodes-base/nodes/HttpRequest/V3/Description.ts")
content = desc_file.read_text()

# Find the "options" collection field
# Start from line 668 and find the field
lines = content.split('\n')

# Find the line with name: 'options' and type: 'collection'
start_idx = None
for i, line in enumerate(lines):
    if i >= 660 and i <= 670 and "name: 'options'" in line:
        print(f"Found 'options' field at line {i+1}")
        start_idx = i - 5  # Go back a bit to get the full object
        break

if start_idx:
    # Extract ~200 lines to see the full structure
    section = '\n'.join(lines[start_idx:start_idx+200])
    print("\n=== SECTION ===")
    print(section[:2000])  # First 2000 chars

    # Now try to extract just the options array
    # Pattern: options: [...]
    options_match = re.search(r"options:\s*\[([\s\S]*?)\](?=\s*[,}])", section)
    if options_match:
        print("\n\n=== FOUND OPTIONS MATCH ===")
        options_content = options_match.group(1)
        print(f"Options content length: {len(options_content)} chars")
        print(f"First 500 chars:\n{options_content[:500]}")
    else:
        print("\n\n=== NO OPTIONS MATCH ===")
        print("Pattern did not match. Let me try a different approach...")

        # Try finding "options: [" and counting brackets
        if "options: [" in section:
            idx = section.index("options: [")
            print(f"Found 'options: [' at position {idx}")
            # Count brackets from there
            start = idx + len("options: [")
            depth = 1
            i = start
            while i < len(section) and depth > 0:
                if section[i] == '[':
                    depth += 1
                elif section[i] == ']':
                    depth -= 1
                i += 1

            if depth == 0:
                options_array = section[start:i-1]
                print(f"\n=== EXTRACTED VIA BRACKET COUNTING ===")
                print(f"Length: {len(options_array)} chars")
                print(f"First 800 chars:\n{options_array[:800]}")
            else:
                print(f"Bracket counting failed, depth={depth}")
