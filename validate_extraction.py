#!/usr/bin/env python3
"""
Validation script for n8n node extraction quality
Checks for common issues and generates detailed reports
"""

import json
import glob
import re
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Tuple, Any

# Configuration
CURRENT_DIR = Path("/media/tyler/fastraid/Projects/n8n Node Scrapper")
OUTPUT_DIR = CURRENT_DIR / "extracted_docs"

class ExtractionValidator:
    def __init__(self):
        self.issues = defaultdict(list)
        self.stats = defaultdict(int)

    def validate_all(self):
        """Run all validation checks"""
        print("=" * 70)
        print("N8N NODE EXTRACTION VALIDATION")
        print("=" * 70)
        print()

        self.check_file_naming_duplicates()
        self.check_zero_properties()
        self.check_null_displaynames()
        self.check_template_variables()
        self.check_malformed_filenames()
        self.check_missing_fields()
        self.check_data_consistency()

        self.print_summary()
        self.save_report()

    def check_file_naming_duplicates(self):
        """Check for duplicate node extractions with different naming"""
        print("Checking for file naming duplicates...")

        data_files = list(OUTPUT_DIR.glob("*_data.json"))
        self.stats['total_data_files'] = len(data_files)

        # Group by lowercase name to find case duplicates
        by_lowercase = defaultdict(list)
        for f in data_files:
            try:
                with open(f) as file:
                    data = json.load(file)
                    node_name = data.get('node_info', {}).get('name', '')
                    if node_name:
                        by_lowercase[node_name.lower()].append({
                            'file': f.name,
                            'node_name': node_name
                        })
            except:
                pass

        duplicates = {k: v for k, v in by_lowercase.items() if len(v) > 1}
        self.stats['duplicate_groups'] = len(duplicates)

        for key, files in duplicates.items():
            self.issues['duplicate_files'].append({
                'normalized_name': key,
                'files': files
            })

        print(f"  ✓ Found {len(duplicates)} duplicate groups")
        print()

    def check_zero_properties(self):
        """Find nodes with zero properties extracted"""
        print("Checking for nodes with zero properties...")

        zero_props = []
        for f in OUTPUT_DIR.glob("*_data.json"):
            try:
                with open(f) as file:
                    data = json.load(file)
                    prop_count = len(data.get('properties', []))
                    if prop_count == 0:
                        zero_props.append({
                            'file': f.name,
                            'node_name': data.get('node_info', {}).get('name', 'unknown')
                        })
            except:
                pass

        self.stats['zero_properties'] = len(zero_props)
        self.issues['zero_properties'] = zero_props

        print(f"  ✓ Found {len(zero_props)} nodes with 0 properties")
        print()

    def check_null_displaynames(self):
        """Find properties with null displayName"""
        print("Checking for null displayName values...")

        null_displays = []
        for f in OUTPUT_DIR.glob("*_data.json"):
            try:
                with open(f) as file:
                    data = json.load(file)
                    for prop in data.get('properties', []):
                        if prop.get('displayName') is None:
                            null_displays.append({
                                'file': f.name,
                                'property_name': prop.get('name', 'unknown'),
                                'property_type': prop.get('type', 'unknown')
                            })
            except:
                pass

        self.stats['null_displaynames'] = len(null_displays)
        self.issues['null_displaynames'] = null_displays

        print(f"  ✓ Found {len(null_displays)} properties with null displayName")
        print()

    def check_template_variables(self):
        """Find unresolved template variables in documentation"""
        print("Checking for unresolved template variables...")

        template_issues = []

        # Check markdown files
        for f in OUTPUT_DIR.glob("*_documentation.md"):
            try:
                content = f.read_text()
                matches = re.findall(r'\$\{[^}]+\}', content)
                if matches:
                    template_issues.append({
                        'file': f.name,
                        'type': 'markdown',
                        'variables': list(set(matches))
                    })
            except:
                pass

        # Check JSON files
        for f in OUTPUT_DIR.glob("*_data.json"):
            try:
                with open(f) as file:
                    data = json.load(file)
                    issues_in_file = []

                    for prop in data.get('properties', []):
                        dn = prop.get('displayName', '')
                        if dn and isinstance(dn, str) and '${' in dn:
                            issues_in_file.append({
                                'property': prop.get('name', 'unknown'),
                                'displayName': dn
                            })

                    if issues_in_file:
                        template_issues.append({
                            'file': f.name,
                            'type': 'json',
                            'issues': issues_in_file
                        })
            except:
                pass

        self.stats['template_variables'] = len(template_issues)
        self.issues['template_variables'] = template_issues

        print(f"  ✓ Found {len(template_issues)} files with unresolved templates")
        print()

    def check_malformed_filenames(self):
        """Check for malformed filenames"""
        print("Checking for malformed filenames...")

        malformed = []
        for f in OUTPUT_DIR.iterdir():
            if '${' in f.name or '(${' in f.name:
                malformed.append(f.name)

        self.stats['malformed_filenames'] = len(malformed)
        self.issues['malformed_filenames'] = malformed

        print(f"  ✓ Found {len(malformed)} malformed filenames")
        print()

    def check_missing_fields(self):
        """Check for common missing fields"""
        print("Checking for missing critical fields...")

        missing_fields = {
            'group': [],
            'inputs': [],
            'outputs': [],
            'icon': []
        }

        for f in OUTPUT_DIR.glob("*_data.json"):
            try:
                with open(f) as file:
                    data = json.load(file)
                    node_info = data.get('node_info', {})

                    # Check for empty group
                    if not node_info.get('group'):
                        missing_fields['group'].append(f.name)

                    # Check for empty inputs/outputs (check both node_info and metadata)
                    inputs = node_info.get('inputs') or data.get('metadata', {}).get('inputs')
                    outputs = node_info.get('outputs') or data.get('metadata', {}).get('outputs')
                    if not inputs:
                        missing_fields['inputs'].append(f.name)
                    if not outputs:
                        missing_fields['outputs'].append(f.name)

                    # Check for missing icon
                    if not node_info.get('icon'):
                        missing_fields['icon'].append(f.name)
            except:
                pass

        for field, files in missing_fields.items():
            self.stats[f'missing_{field}'] = len(files)
            if files:
                self.issues[f'missing_{field}'] = files[:20]  # Limit to first 20

        print(f"  ✓ Missing group: {len(missing_fields['group'])} files")
        print(f"  ✓ Missing inputs: {len(missing_fields['inputs'])} files")
        print(f"  ✓ Missing outputs: {len(missing_fields['outputs'])} files")
        print(f"  ✓ Missing icon: {len(missing_fields['icon'])} files")
        print()

    def check_data_consistency(self):
        """Check consistency between JSON and markdown files"""
        print("Checking data consistency between JSON and MD files...")

        inconsistencies = []

        for json_file in OUTPUT_DIR.glob("*_data.json"):
            md_file = json_file.with_name(json_file.name.replace('_data.json', '_documentation.md'))

            if not md_file.exists():
                inconsistencies.append({
                    'issue': 'missing_md',
                    'json_file': json_file.name
                })

        for md_file in OUTPUT_DIR.glob("*_documentation.md"):
            json_file = md_file.with_name(md_file.name.replace('_documentation.md', '_data.json'))

            if not json_file.exists():
                inconsistencies.append({
                    'issue': 'missing_json',
                    'md_file': md_file.name
                })

        self.stats['file_inconsistencies'] = len(inconsistencies)
        self.issues['file_inconsistencies'] = inconsistencies

        print(f"  ✓ Found {len(inconsistencies)} file pair inconsistencies")
        print()

    def print_summary(self):
        """Print validation summary"""
        print()
        print("=" * 70)
        print("VALIDATION SUMMARY")
        print("=" * 70)
        print()

        print(f"Total data files: {self.stats['total_data_files']}")
        print()

        print("CRITICAL ISSUES:")
        print(f"  • Duplicate file groups: {self.stats['duplicate_groups']}")
        print(f"  • Nodes with 0 properties: {self.stats['zero_properties']}")
        print(f"  • Properties with null displayName: {self.stats['null_displaynames']}")
        print(f"  • Files with template variables: {self.stats['template_variables']}")
        print(f"  • Malformed filenames: {self.stats['malformed_filenames']}")
        print()

        print("MISSING FIELD ISSUES:")
        print(f"  • Missing group: {self.stats.get('missing_group', 0)}")
        print(f"  • Missing inputs: {self.stats.get('missing_inputs', 0)}")
        print(f"  • Missing outputs: {self.stats.get('missing_outputs', 0)}")
        print(f"  • Missing icon: {self.stats.get('missing_icon', 0)}")
        print()

        print("FILE CONSISTENCY:")
        print(f"  • File pair inconsistencies: {self.stats['file_inconsistencies']}")
        print()

    def save_report(self):
        """Save detailed report to JSON"""
        report_file = CURRENT_DIR / "validation_report.json"

        report = {
            'stats': dict(self.stats),
            'issues': dict(self.issues)
        }

        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)

        print(f"Detailed report saved to: {report_file}")
        print()

        # Also print some examples
        print("=" * 70)
        print("EXAMPLE ISSUES")
        print("=" * 70)
        print()

        if self.issues.get('duplicate_files'):
            print("DUPLICATE FILES (first 5):")
            for dup in self.issues['duplicate_files'][:5]:
                print(f"  {dup['normalized_name']}:")
                for f in dup['files']:
                    print(f"    - {f['file']} (node_name: {f['node_name']})")
            print()

        if self.issues.get('zero_properties'):
            print("ZERO PROPERTIES (first 10):")
            for item in self.issues['zero_properties'][:10]:
                print(f"  - {item['file']} (node: {item['node_name']})")
            print()

        if self.issues.get('null_displaynames'):
            print("NULL DISPLAYNAMES (first 10):")
            for item in self.issues['null_displaynames'][:10]:
                print(f"  - {item['file']}: {item['property_name']} ({item['property_type']})")
            print()

        if self.issues.get('template_variables'):
            print("TEMPLATE VARIABLES (first 5):")
            for item in self.issues['template_variables'][:5]:
                print(f"  - {item['file']} ({item['type']})")
                if item['type'] == 'markdown':
                    print(f"    Variables: {', '.join(item['variables'][:3])}")
            print()

        if self.issues.get('malformed_filenames'):
            print("MALFORMED FILENAMES:")
            for fname in self.issues['malformed_filenames']:
                print(f"  - {fname}")
            print()


def main():
    validator = ExtractionValidator()
    validator.validate_all()

    print("=" * 70)
    print("Validation complete!")
    print("=" * 70)


if __name__ == "__main__":
    main()
