#!/usr/bin/env python3

import docx
from docx import Document
import sys
import os

# Add the current directory to path to import from faq_processor
sys.path.insert(0, os.getcwd())
from faq_processor import extract_paragraph_content

def debug_real_document():
    print("Debugging real document link extraction...")
    
    # Load the data engineering document
    doc = Document('cache/data-engineering-zoomcamp.docx')
    
    # Search for paragraphs containing "Homebrew" or "github.com/Homebrew"
    for i, paragraph in enumerate(doc.paragraphs):
        paragraph_text = paragraph.text.lower()
        
        if 'homebrew' in paragraph_text or 'github.com/homebrew' in paragraph_text:
            print(f"\n=== Found Homebrew reference in Paragraph {i+1} ===")
            print(f"Style: {paragraph.style.name}")
            print(f"Raw text: '{paragraph.text}'")
            
            # Extract content using our function
            extracted_content = extract_paragraph_content(paragraph)
            print(f"Extracted content: '{extracted_content}'")
            
            # Debug: Check runs and their properties
            print(f"Number of runs: {len(paragraph.runs)}")
            for j, run in enumerate(paragraph.runs):
                print(f"  Run {j}: '{run.text}'")
                
                # Check for hyperlink properties in detail
                element = run._element
                print(f"    Element tag: {element.tag}")
                
                # Check all ancestors for hyperlink
                current = element
                hyperlink_ancestors = []
                while current is not None:
                    tag = current.tag
                    hyperlink_ancestors.append(tag)
                    if tag.endswith('}hyperlink'):
                        print(f"    *** HYPERLINK FOUND in ancestor chain ***")
                        rel_id = current.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')
                        print(f"    Relationship ID: {rel_id}")
                        
                        # Try to get the actual URL
                        try:
                            rel = paragraph._parent.part.rels[rel_id]
                            print(f"    Target URL: {rel.target_ref}")
                        except (KeyError, AttributeError) as e:
                            print(f"    Error getting URL: {e}")
                        break
                    current = current.getparent()
                
                print(f"    Ancestor chain: {[t.split('}')[-1] for t in hyperlink_ancestors]}")
            
            # Only show first match for now
            break

if __name__ == "__main__":
    debug_real_document()