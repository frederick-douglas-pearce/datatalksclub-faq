#!/usr/bin/env python3

import docx
from docx import Document
from docx.oxml.ns import qn
import sys
import os

def examine_document_xml():
    print("Examining XML structure of test_links.docx...")
    
    try:
        # Load your test document
        doc = Document('test_links.docx')
        
        print("=== Searching for hyperlink elements in XML ===")
        
        # Look at raw XML to understand structure
        for i, paragraph in enumerate(doc.paragraphs):
            if not paragraph.text.strip():
                continue
                
            # Get the paragraph XML
            p_xml = paragraph._p
            
            # Look for hyperlink elements
            hyperlink_elements = p_xml.xpath('.//w:hyperlink', namespaces={'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'})
            
            if hyperlink_elements:
                print(f"\n--- Paragraph {i+1} has hyperlinks ---")
                print(f"Paragraph text: '{paragraph.text}'")
                
                for j, hyperlink_elem in enumerate(hyperlink_elements):
                    print(f"\n  Hyperlink {j+1}:")
                    
                    # Get relationship ID
                    rel_id = hyperlink_elem.get(qn('r:id'))
                    print(f"    Relationship ID: {rel_id}")
                    
                    # Get hyperlink text by looking at text elements within it
                    text_elements = hyperlink_elem.xpath('.//w:t', namespaces={'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'})
                    hyperlink_text = ''.join([t.text for t in text_elements if t.text])
                    print(f"    Hyperlink text: '{hyperlink_text}'")
                    
                    # Get the URL
                    if rel_id:
                        try:
                            rel = paragraph._parent.part.rels[rel_id]
                            print(f"    Target URL: {rel.target_ref}")
                        except (KeyError, AttributeError) as e:
                            print(f"    Error getting URL: {e}")
    
    except FileNotFoundError:
        print("test_links.docx not found. Please make sure the file exists.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    examine_document_xml()