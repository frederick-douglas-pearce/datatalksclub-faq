#!/usr/bin/env python3
"""
Throw-away script to rename markdown files in _questions directory.
This script will:
1. Find all .md files in _questions directory recursively
2. Parse the YAML frontmatter to extract sort_order
3. Rename files to format: {sort_order}_{old_name}
   where sort_order has leading zeros (0010, 0020, etc.)
"""

import re
from pathlib import Path
from typing import Optional

def extract_sort_order(content: str) -> Optional[int]:
    """Extract sort_order from YAML frontmatter."""
    if not content.startswith('---\n'):
        return None
    
    # Find the end of frontmatter
    end_match = re.search(r'\n---\n', content)
    if not end_match:
        return None
    
    frontmatter_text = content[4:end_match.start()]  # Skip first '---\n'
    
    # Look for sort_order
    sort_order_match = re.search(r'^sort_order:\s*(\d+)\s*$', frontmatter_text, re.MULTILINE)
    
    if sort_order_match:
        try:
            return int(sort_order_match.group(1))
        except ValueError:
            pass
    
    return None

def clean_filename(filename: str) -> str:
    """Remove any existing sort_order prefixes from filename."""
    # Remove .md extension if present
    if filename.endswith('.md'):
        filename = filename[:-3]
    
    # Remove existing sort_order prefixes (pattern: digits_)
    # This handles cases where files were already renamed multiple times
    while re.match(r'^\d+_', filename):
        filename = re.sub(r'^\d+_', '', filename, count=1)
    
    return filename

def main():
    """Main function to rename all markdown files."""
    # Find all markdown files in _questions directory
    questions_dir = Path("_questions")
    if not questions_dir.exists():
        print("Error: _questions directory not found!")
        return
    
    md_files = list(questions_dir.glob("**/*.md"))
    print(f"Found {len(md_files)} markdown files")
    
    # Process each file
    renamed_count = 0
    error_count = 0
    
    for filepath in md_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            sort_order = extract_sort_order(content)
            
            if sort_order is None:
                print(f"Warning: Missing sort_order in {filepath}")
                error_count += 1
                continue
            
            # Clean the old filename (remove existing sort_order prefixes)
            old_name_clean = clean_filename(filepath.name)
            
            # Format sort_order with leading zeros (4 digits)
            sort_order_str = f"{sort_order:04d}"
            
            # Create new filename: {sort_order}_{clean_old_name}.md
            new_filename = f"{sort_order_str}_{old_name_clean}.md"
            new_filepath = filepath.parent / new_filename
            
            # Check if rename is needed
            if filepath.name == new_filename:
                print(f"No rename needed: {filepath.name}")
                continue
            
            # Check if target file already exists
            if new_filepath.exists():
                print(f"Warning: Target file already exists, skipping: {new_filename}")
                error_count += 1
                continue
            
            # Rename the file
            filepath.rename(new_filepath)
            print(f"Renamed: {filepath.name} -> {new_filename}")
            renamed_count += 1
            
        except Exception as e:
            print(f"Error processing {filepath}: {e}")
            error_count += 1
    
    print(f"\nCompleted! Renamed {renamed_count} files. {error_count} errors/skipped.")

if __name__ == "__main__":
    main()