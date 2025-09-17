#!/usr/bin/env python3

import docx
from docx import Document
import sys
import os

def examine_document_xml_simple():
    print("Examining XML structure of test_links.docx...")
    
    try:
        # Load your test document
        doc = Document('test_links.docx')
        
        print("=== Searching for hyperlink elements ===")
        
        for i, paragraph in enumerate(doc.paragraphs):
            if not paragraph.text.strip():
                continue
                
            # Get the paragraph element
            p_elem = paragraph._p
            
            # Search for hyperlink elements more directly
            hyperlinks_found = []
            for elem in p_elem.iter():
                if elem.tag.endswith('}hyperlink'):
                    hyperlinks_found.append(elem)
            
            if hyperlinks_found:
                print(f"\n--- Paragraph {i+1} has {len(hyperlinks_found)} hyperlinks ---")
                print(f"Paragraph text: '{paragraph.text}'")
                print(f"Number of runs: {len(paragraph.runs)}")
                
                for j, hyperlink_elem in enumerate(hyperlinks_found):
                    print(f"\n  Hyperlink {j+1}:")
                    
                    # Get relationship ID
                    rel_id = None
                    for attr_name, attr_value in hyperlink_elem.attrib.items():
                        if 'id' in attr_name.lower():
                            rel_id = attr_value
                            print(f"    Relationship ID: {rel_id}")
                    
                    # Get all text from this hyperlink element
                    hyperlink_text = ''
                    for text_elem in hyperlink_elem.iter():
                        if text_elem.tag.endswith('}t') and text_elem.text:
                            hyperlink_text += text_elem.text
                    
                    print(f"    Hyperlink text: '{hyperlink_text}'")
                    
                    # Get the URL
                    if rel_id:
                        try:
                            rel = paragraph._parent.part.rels[rel_id]
                            print(f"    Target URL: {rel.target_ref}")
                        except (KeyError, AttributeError) as e:
                            print(f"    Error getting URL: {e}")
                
                # Also show all runs in this paragraph
                print(f"\n  All runs in this paragraph:")
                for k, run in enumerate(paragraph.runs):
                    print(f"    Run {k}: '{run.text}'")
    
    except FileNotFoundError:
        print("test_links.docx not found. Please make sure the file exists.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    examine_document_xml_simple()