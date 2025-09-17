import hashlib
import re
from pathlib import Path

import requests
import docx

def clean_line(line):
    line = line.strip()
    line = line.strip('\uFEFF')
    return line

def sanitize_filename(text):
    """Convert text to safe filename with length limits"""
    # Remove special characters and replace spaces with hyphens
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    text = text.lower().strip('-')
    
    # Limit filename length (Windows has ~260 character path limit)
    if len(text) > 100:
        text = text[:100].rstrip('-')
    
    return text

def download_docx_file(file_id, course_name):
    """Download and cache docx file locally"""
    cache_dir = Path('cache')
    cache_dir.mkdir(exist_ok=True)
    
    cache_file = cache_dir / f'{course_name}.docx'
    
    if cache_file.exists():
        print(f"Using cached file for {course_name}")
        return cache_file
    
    print(f"Downloading {course_name}...")
    url = f'https://docs.google.com/document/d/{file_id}/export?format=docx'
    
    response = requests.get(url)
    response.raise_for_status()
    
    with open(cache_file, 'wb') as f:
        f.write(response.content)
    
    return cache_file

def extract_images_from_docx(doc, course_name):
    """Extract images from docx and save them to images directory"""
    images_dir = Path('images') / course_name
    images_dir.mkdir(parents=True, exist_ok=True)
    
    image_mapping = {}
    
    for rel_id, rel in doc.part.rels.items():
        if "image" in rel.target_ref:
            try:
                # Check if this is an internal relationship with a target part
                if hasattr(rel, 'is_external') and rel.is_external:
                    print(f"Skipping external image reference: {rel.target_ref}")
                    continue
                    
                image_data = rel.target_part.blob
                
                # Generate filename based on content hash
                image_hash = hashlib.md5(image_data).hexdigest()[:8]
                
                # Determine file extension
                content_type = rel.target_part.content_type
                if 'png' in content_type:
                    ext = 'png'
                elif 'jpeg' in content_type or 'jpg' in content_type:
                    ext = 'jpg'
                elif 'gif' in content_type:
                    ext = 'gif'
                else:
                    ext = 'png'
                
                image_filename = f'image_{image_hash}.{ext}'
                image_path = images_dir / image_filename
                
                with open(image_path, 'wb') as f:
                    f.write(image_data)
                
                # Map using the relationship ID with Jekyll-style absolute path
                image_mapping[rel_id] = f'/images/{course_name}/{image_filename}'
                print(f"Extracted image: {rel_id} -> {image_filename}")
            except (ValueError, AttributeError):
                # Skip external images or broken references
                print(f"Skipping external or broken image reference: {rel.target_ref}")
                continue
    
    return image_mapping

def extract_paragraph_content(paragraph):
    """Extract text and hyperlinks from a paragraph"""
    content_parts = []
    
    for run in paragraph.runs:
        text = run.text
        if not text:
            continue
            
        # Check if this run is part of a hyperlink
        hyperlink = None
        element = run._element
        
        # Look for hyperlink in the run's parent elements
        parent = element.getparent()
        while parent is not None:
            if parent.tag.endswith('}hyperlink'):
                # Found hyperlink element, get the relationship ID
                rel_id = parent.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')
                if rel_id:
                    try:
                        # Get the hyperlink target from document relationships
                        rel = paragraph._parent.part.rels[rel_id]
                        hyperlink = rel.target_ref
                    except (KeyError, AttributeError):
                        pass
                break
            parent = parent.getparent()
        
        # Add text with optional hyperlink
        if hyperlink:
            content_parts.append(f'[{text}]({hyperlink})')
        else:
            content_parts.append(text)
    
    return ''.join(content_parts)

def read_faq(cache_file, course_name):
    """Read FAQ from cached docx file and extract content with images and links"""
    doc = docx.Document(cache_file)
    
    # Extract images
    image_mapping = extract_images_from_docx(doc, course_name)
    
    questions = []

    question_heading_style = 'heading 2'
    section_heading_style = 'heading 1'
    
    section_title = ''
    question_title = ''
    answer_content = []
     
    for p in doc.paragraphs:
        style = p.style.name.lower()
        
        # Extract text with hyperlinks
        p_text = clean_line(extract_paragraph_content(p))
    
        # Check for images in paragraph using a simpler approach
        images_in_paragraph = []
        
        # Look for images in runs
        for run in p.runs:
            # Check for embedded images using element inspection
            element = run._element
            # Look for any blip elements that contain image references
            for blip in element.iter():
                if blip.tag.endswith('}blip'):
                    embed_attr = blip.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
                    if embed_attr and embed_attr in image_mapping:
                        images_in_paragraph.append(image_mapping[embed_attr])
    
        # Skip only if paragraph has no text AND no images
        if len(p_text) == 0 and len(images_in_paragraph) == 0:
            continue
    
        # Handle section headings (but still check for images)
        if style == section_heading_style:
            # Add any images from this heading paragraph before moving to new section
            for image_path in images_in_paragraph:
                answer_content.append({'type': 'image', 'content': image_path})
            section_title = p_text
            continue
    
        # Handle question headings (but still check for images)
        if style == question_heading_style:
            # Save previous question if it exists
            if answer_content and section_title and question_title:
                questions.append({
                    'content': answer_content,
                    'section': section_title,
                    'question': question_title,
                })
                answer_content = []
            
            # Add any images from this heading paragraph before moving to new question
            for image_path in images_in_paragraph:
                answer_content.append({'type': 'image', 'content': image_path})
    
            question_title = p_text
            continue
        
        # Add text content if present
        if p_text:
            answer_content.append({'type': 'text', 'content': p_text})
        
        # Add images (regardless of whether there's text)
        for image_path in images_in_paragraph:
            answer_content.append({'type': 'image', 'content': image_path})
    
    # Add the last question
    if answer_content and section_title and question_title:
        questions.append({
            'content': answer_content,
            'section': section_title,
            'question': question_title,
        })

    return questions

def yaml_escape(text):
    """Escape text for YAML frontmatter using quoted strings"""
    if not text:
        return '""'
    
    # Escape quotes and backslashes
    text = text.replace('\\', '\\\\')  # Escape backslashes first
    text = text.replace('"', '\\"')   # Escape quotes
    text = text.replace('\n', ' ')    # Replace newlines with spaces
    text = text.replace('\r', ' ')    # Replace carriage returns with spaces
    
    # Always wrap in quotes for safety
    return f'"{text}"'

def liquid_escape(text):
    """Escape text to prevent Liquid template processing - simplified approach"""
    if not text:
        return text
    
    # Use code blocks to prevent Liquid processing
    return text

def create_question_file(question_data, course_name, question_index):
    """Create individual question markdown file with Jekyll frontmatter in course folder"""
    course_dir = Path('_questions') / course_name
    course_dir.mkdir(parents=True, exist_ok=True)
    
    # Create safe filename
    question_title = question_data['question']
    safe_title = sanitize_filename(question_title)
    filename = f'{question_index:03d}-{safe_title}.md'
    
    question_file = course_dir / filename
    
    with open(question_file, 'w', encoding='utf-8') as f:
        # Write Jekyll frontmatter with proper escaping
        f.write('---\n')
        f.write(f'question: {yaml_escape(question_data["question"])}\n')
        f.write(f'section: {yaml_escape(question_data["section"])}\n')
        f.write(f'course: {yaml_escape(course_name)}\n')
        f.write('---\n\n')
        
        # Write answer content without raw tags since output is false
        for item in question_data['content']:
            if item['type'] == 'text':
                f.write(f'{item["content"]}\n\n')
            elif item['type'] == 'image':
                f.write(f'![Image]({item["content"]})\n\n')
    
    return filename

def create_course_index(course_data):
    """Create course index page that uses Liquid templates to display questions from collection"""
    course_name = course_data['course']
    
    # Create course index in root directory
    index_file = Path(f'{course_name}.md')
    
    with open(index_file, 'w', encoding='utf-8') as f:
        # Write Jekyll frontmatter
        f.write('---\n')
        f.write('layout: default\n')
        f.write(f'title: "{course_name.replace("-", " ").title()} FAQ"\n')
        f.write('---\n\n')
        
        f.write(f'# {course_name.replace("-", " ").title()} FAQ\n\n')
        
        # Use Liquid template to loop through questions from collection
        f.write('{% assign course_questions = site.questions | where: "course", "' + course_name + '" %}\n')
        f.write('{% assign sections = course_questions | group_by: "section" %}\n\n')
        
        f.write('{% for section in sections %}\n')
        f.write('## {{ section.name }}\n\n')
        
        f.write('{% for question in section.items %}\n')
        f.write('### {{ question.question }}\n\n')
        f.write('{{ question.content }}\n\n')
        f.write('---\n\n')
        f.write('{% endfor %}\n\n')
        f.write('{% endfor %}\n')
    
    print(f"Generated course index: {index_file}")

def create_index_page():
    """Create main index page"""
    index_content = '''---
layout: default
title: DataTalks.Club FAQ
---

# DataTalks.Club FAQ

Welcome to the FAQ collection for DataTalks.Club courses.

## Available Courses

- [Data Engineering Zoomcamp]({{ site.baseurl }}/data-engineering-zoomcamp)
- [Machine Learning Zoomcamp]({{ site.baseurl }}/machine-learning-zoomcamp)
- [MLOps Zoomcamp]({{ site.baseurl }}/mlops-zoomcamp)

## About

This site contains frequently asked questions and answers from the DataTalks.Club community courses.
'''
    
    with open('index.md', 'w', encoding='utf-8') as f:
        f.write(index_content)
    
    print("Generated main index: index.md")



# Main execution
faq_documents = {
    'data-engineering-zoomcamp': '19bnYs80DwuUimHM65UV3sylsCn2j1vziPOwzBwQrebw',
    'machine-learning-zoomcamp': '1LpPanc33QJJ6BSsyxVg-pWNMplal84TdZtq10naIhD8',
    'mlops-zoomcamp': '12TlBfhIiKtyBv8RnsoJR6F72bkPDGEvPOItJIxaEzE0',
}

# Create index page
print("Creating index page...")
create_index_page()

documents = []

for course, file_id in faq_documents.items():
    print(f"\nProcessing {course}...")
    
    # Download and cache docx file
    cache_file = download_docx_file(file_id, course)
    
    # Read FAQ with images
    course_documents = read_faq(cache_file, course)
    
    course_data = {'course': course, 'questions': course_documents}
    documents.append(course_data)
    
    # Create individual question files
    print(f"Creating question files for {course}...")
    for i, question_data in enumerate(course_documents):
        create_question_file(question_data, course, i + 1)
    
    # Create course index page
    create_course_index(course_data)

print(f"\nProcessed {len(documents)} courses successfully!")
print("Generated files:")
print("- _questions/ - Individual question files")
print("- index.md - Main index page")
print("- [course].md - Course index pages")
print("- images/ - Extracted images organized by course")