#!/usr/bin/env python3
"""
Cleanup script for duplicate and malformed extraction files
Keeps only the normalized lowercase versions
"""

import json
import re
from pathlib import Path
from collections import defaultdict

# Configuration
CURRENT_DIR = Path("/media/tyler/fastraid/Projects/n8n Node Scrapper")
OUTPUT_DIR = CURRENT_DIR / "extracted_docs"


def normalize_filename(name: str) -> str:
    """
    Normalize node name for consistent, safe filenames
    (Must match the normalization in n8n_node_extractor.py)
    """
    # Convert to lowercase
    normalized = name.lower()
    # Replace spaces and hyphens with underscores
    normalized = normalized.replace(' ', '_').replace('-', '_')
    # Remove any characters that aren't alphanumeric or underscore
    normalized = re.sub(r'[^a-z0-9_]', '', normalized)
    # Remove duplicate underscores
    normalized = re.sub(r'_+', '_', normalized)
    # Remove leading/trailing underscores
    normalized = normalized.strip('_')
    return normalized


def cleanup_duplicates():
    """Remove duplicate files, keeping only normalized versions"""
    print("=" * 70)
    print("CLEANING UP DUPLICATE FILES")
    print("=" * 70)
    print()

    # Group files by normalized name
    files_by_normalized = defaultdict(list)

    for f in OUTPUT_DIR.glob("*_data.json"):
        try:
            with open(f) as file:
                data = json.load(file)
                node_name = data.get('node_info', {}).get('name', '')
                if node_name:
                    normalized = normalize_filename(node_name)
                    files_by_normalized[normalized].append({
                        'json': f,
                        'md': f.with_name(f.name.replace('_data.json', '_documentation.md')),
                        'node_name': node_name,
                        'file_base': f.stem.replace('_data', '')
                    })
        except Exception as e:
            print(f"Warning: Could not process {f.name}: {e}")

    # Process each group
    removed_count = 0
    kept_count = 0

    for normalized_name, file_group in files_by_normalized.items():
        if len(file_group) <= 1:
            # No duplicates
            kept_count += 1
            continue

        print(f"\nProcessing duplicates for: {normalized_name}")
        print(f"  Found {len(file_group)} versions:")

        # Find which file to keep (prefer the one matching normalized name)
        to_keep = None
        to_remove = []

        for item in file_group:
            file_base = item['file_base']
            item_normalized = normalize_filename(file_base)

            print(f"    - {item['json'].name} (base: {file_base}, normalized: {item_normalized})")

            if item_normalized == normalized_name:
                # This matches the normalized name
                if to_keep is None:
                    to_keep = item
                    print(f"      → KEEP (matches normalized name)")
                else:
                    # Multiple files match - keep the one with more properties
                    try:
                        with open(item['json']) as f:
                            data = json.load(f)
                            item_props = len(data.get('properties', []))

                        with open(to_keep['json']) as f:
                            data = json.load(f)
                            keep_props = len(data.get('properties', []))

                        if item_props > keep_props:
                            to_remove.append(to_keep)
                            to_keep = item
                            print(f"      → KEEP (has more properties: {item_props} vs {keep_props})")
                        else:
                            to_remove.append(item)
                            print(f"      → REMOVE (fewer properties)")
                    except:
                        to_remove.append(item)
                        print(f"      → REMOVE (error reading)")
            else:
                to_remove.append(item)
                print(f"      → REMOVE (doesn't match normalized name)")

        # If nothing matched normalized name, keep the first one with most properties
        if to_keep is None and file_group:
            max_props = -1
            for item in file_group:
                try:
                    with open(item['json']) as f:
                        data = json.load(f)
                        props = len(data.get('properties', []))
                        if props > max_props:
                            max_props = props
                            if to_keep:
                                to_remove.append(to_keep)
                            to_keep = item
                        else:
                            to_remove.append(item)
                except:
                    to_remove.append(item)

        # Remove duplicates
        for item in to_remove:
            try:
                if item['json'].exists():
                    item['json'].unlink()
                    print(f"    Removed: {item['json'].name}")
                    removed_count += 1

                if item['md'].exists():
                    item['md'].unlink()
                    print(f"    Removed: {item['md'].name}")
                    removed_count += 1
            except Exception as e:
                print(f"    Error removing {item['json'].name}: {e}")

        kept_count += 1

    print()
    print(f"Summary: Kept {kept_count} nodes, removed {removed_count} duplicate files")
    return removed_count


def cleanup_malformed():
    """Remove malformed filenames (containing ${...} templates)"""
    print()
    print("=" * 70)
    print("CLEANING UP MALFORMED FILES")
    print("=" * 70)
    print()

    removed_count = 0

    for f in OUTPUT_DIR.iterdir():
        if '${' in f.name or '(${' in f.name:
            print(f"Removing malformed file: {f.name}")
            try:
                f.unlink()
                removed_count += 1
            except Exception as e:
                print(f"  Error: {e}")

    print(f"Removed {removed_count} malformed files")
    return removed_count


def main():
    print("\n" + "=" * 70)
    print("FILE CLEANUP UTILITY")
    print("=" * 70)
    print()

    dup_removed = cleanup_duplicates()
    mal_removed = cleanup_malformed()

    print()
    print("=" * 70)
    print("CLEANUP COMPLETE")
    print("=" * 70)
    print(f"Total files removed: {dup_removed + mal_removed}")
    print("=" * 70)
    print()


if __name__ == "__main__":
    main()
