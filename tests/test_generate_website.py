"""
Tests for generate_website.py parsing logic
"""
import pytest
from pathlib import Path
import tempfile
import os
import sys

# Add the parent directory to sys.path to import generate_website
sys.path.insert(0, str(Path(__file__).parent.parent))

from generate_website import (
    parse_frontmatter,
    convert_plain_urls_to_links,
    process_markdown,
    load_course_metadata,
    process_question_file,
    find_section_name
)


class TestParseFrontmatter:
    """Test the YAML frontmatter parsing functionality"""
    
    def test_parse_frontmatter_valid_yaml(self):
        """Test parsing valid YAML frontmatter"""
        content = """---
question: "How do I install Python?"
id: "abc123"
sort_order: 1
tags: ["python", "installation"]
---
This is the markdown content.
More content here.
"""
        frontmatter, markdown = parse_frontmatter(content)
        
        assert frontmatter["question"] == "How do I install Python?"
        assert frontmatter["id"] == "abc123"
        assert frontmatter["sort_order"] == 1
        assert frontmatter["tags"] == ["python", "installation"]
        assert markdown == "This is the markdown content.\nMore content here."
    
    def test_parse_frontmatter_no_frontmatter(self):
        """Test content with no frontmatter"""
        content = "Just regular markdown content here."
        frontmatter, markdown = parse_frontmatter(content)
        
        assert frontmatter == {}
        assert markdown == content
    
    def test_parse_frontmatter_empty_frontmatter(self):
        """Test content with empty frontmatter"""
        content = """---
---
Some markdown content."""
        frontmatter, markdown = parse_frontmatter(content)
        
        assert frontmatter == {}
        assert markdown == "Some markdown content."
    
    def test_parse_frontmatter_invalid_yaml(self):
        """Test content with invalid YAML frontmatter"""
        content = """---
invalid: yaml: content: here
---
Markdown content."""
        frontmatter, markdown = parse_frontmatter(content)
        
        assert frontmatter == {}
        assert markdown == content
    
    def test_parse_frontmatter_incomplete_frontmatter(self):
        """Test content with incomplete frontmatter delimiter"""
        content = """---
question: "Test question"
Some content without closing delimiter."""
        frontmatter, markdown = parse_frontmatter(content)
        
        assert frontmatter == {}
        assert markdown == content


class TestConvertPlainUrlsToLinks:
    """Test the URL detection and conversion functionality"""
    
    def test_convert_single_http_url(self):
        """Test converting a single HTTP URL"""
        text = "Visit http://example.com for more info."
        result = convert_plain_urls_to_links(text)
        expected = "Visit [http://example.com](http://example.com) for more info."
        assert result == expected
    
    def test_convert_single_https_url(self):
        """Test converting a single HTTPS URL"""
        text = "Check out https://github.com/example/repo"
        result = convert_plain_urls_to_links(text)
        expected = "Check out [https://github.com/example/repo](https://github.com/example/repo)"
        assert result == expected
    
    def test_convert_multiple_urls(self):
        """Test converting multiple URLs in one text"""
        text = "Visit https://example.com and http://test.org for info."
        result = convert_plain_urls_to_links(text)
        expected = "Visit [https://example.com](https://example.com) and [http://test.org](http://test.org) for info."
        assert result == expected
    
    def test_preserve_urls_in_code_blocks(self):
        """Test that URLs inside code blocks are not converted"""
        text = """Here's how to download:
```bash
wget https://example.com/file.txt
curl -o data.csv https://raw.githubusercontent.com/user/repo/main/data.csv
```
Visit https://example.com for more info."""
        result = convert_plain_urls_to_links(text)
        
        # URLs in code blocks should remain unchanged
        assert "wget https://example.com/file.txt" in result
        assert "curl -o data.csv https://raw.githubusercontent.com/user/repo/main/data.csv" in result
        # URL outside code block should be converted
        assert "[https://example.com](https://example.com)" in result
    
    def test_preserve_urls_in_inline_code(self):
        """Test that URLs inside inline code are not converted"""
        text = "Use `curl https://api.example.com/data` to fetch data. Visit https://example.com for docs."
        result = convert_plain_urls_to_links(text)
        
        # URL in inline code should remain unchanged
        assert "`curl https://api.example.com/data`" in result
        # URL outside inline code should be converted
        assert "[https://example.com](https://example.com)" in result
    
    def test_preserve_existing_markdown_links(self):
        """Test that existing markdown links are not double-converted"""
        text = "Check [the docs](https://docs.example.com) and visit https://example.com"
        result = convert_plain_urls_to_links(text)
        
        # Existing markdown link should remain unchanged
        assert "[the docs](https://docs.example.com)" in result
        # Plain URL should be converted
        assert "[https://example.com](https://example.com)" in result
    
    def test_handle_urls_with_trailing_punctuation(self):
        """Test that trailing punctuation is handled correctly"""
        text = "Visit https://example.com. Also check https://test.org!"
        result = convert_plain_urls_to_links(text)
        expected = "Visit [https://example.com](https://example.com). Also check [https://test.org](https://test.org)!"
        assert result == expected
    
    def test_handle_complex_code_and_text_mix(self):
        """Test complex scenarios with mixed code blocks, inline code, and plain text"""
        text = """Download a CSV file:

```python
url = 'https://raw.githubusercontent.com/alexeygrigorev/datasets/master/housing.csv'
df = pd.read_csv(url)
```

You can also use `wget https://example.com/data.csv` command.

For more info visit https://github.com/example/repo."""
        result = convert_plain_urls_to_links(text)
        
        # URL in code block should remain unchanged
        assert "url = 'https://raw.githubusercontent.com/alexeygrigorev/datasets/master/housing.csv'" in result
        # URL in inline code should remain unchanged
        assert "`wget https://example.com/data.csv`" in result
        # Plain URL should be converted
        assert "[https://github.com/example/repo](https://github.com/example/repo)" in result
    
    def test_no_urls_present(self):
        """Test text with no URLs"""
        text = "This is just regular text with no URLs."
        result = convert_plain_urls_to_links(text)
        assert result == text
    
    def test_empty_string(self):
        """Test empty string input"""
        result = convert_plain_urls_to_links("")
        assert result == ""


class TestProcessMarkdown:
    """Test markdown processing functionality"""
    
    def test_process_markdown_basic(self):
        """Test basic markdown processing without images"""
        content = "# Title\n\nThis is **bold** text with https://example.com link."
        result = process_markdown(content)
        
        assert "<h1>Title</h1>" in result
        assert "<strong>bold</strong>" in result
        assert 'href="https://example.com"' in result
        assert 'target="_blank"' in result
    
    def test_process_markdown_with_image_placeholders(self):
        """Test markdown processing with image placeholders"""
        content = "Here's an image: <{IMAGE:img1}>\n\nAnd some text."
        images = [
            {"id": "img1", "description": "Test image", "path": "/images/test.png"}
        ]
        result = process_markdown(content, images)
        
        # The markdown processor converts the image to HTML
        assert 'alt="Test image"' in result
        assert 'src="/images/test.png"' in result
    
    def test_process_markdown_with_code_and_urls(self):
        """Test that markdown processing preserves URLs in code blocks"""
        content = """# Instructions

```bash
wget https://example.com/file.txt
```

Visit https://docs.example.com for more info."""
        result = process_markdown(content)
        
        # URL in code should remain as plain text in HTML (may have syntax highlighting)
        assert "https://example.com/file.txt" in result
        # URL in plain text should be converted to link
        assert 'href="https://docs.example.com"' in result


class TestFindSectionName:
    """Test the section name finding functionality"""
    
    def test_find_section_name_existing(self):
        """Test finding an existing section name"""
        section_order = [
            {"id": "general", "name": "General Questions"},
            {"id": "module-1", "name": "Module 1: Introduction"},
            {"id": "advanced", "name": "Advanced Topics"}
        ]
        
        result = find_section_name(section_order, "module-1")
        assert result == "Module 1: Introduction"
    
    def test_find_section_name_missing(self):
        """Test finding a non-existing section name"""
        section_order = [
            {"id": "general", "name": "General Questions"},
            {"id": "module-1", "name": "Module 1: Introduction"}
        ]
        
        result = find_section_name(section_order, "module-2")
        assert result == "module-2"
    
    def test_find_section_name_empty_list(self):
        """Test finding section name in empty list"""
        section_order = []
        
        result = find_section_name(section_order, "test")
        assert result == "test"


class TestLoadCourseMetadata:
    """Test course metadata loading functionality"""
    
    def test_load_course_metadata_valid_file(self):
        """Test loading valid metadata file"""
        # Create a temporary metadata file
        with tempfile.TemporaryDirectory() as temp_dir:
            course_dir = Path(temp_dir)
            metadata_file = course_dir / "_metadata.yaml"
            
            metadata_content = """
course_name: "Test Course"
sections:
  - id: "general"
    name: "General Questions"
  - id: "module-1"
    name: "Module 1: Introduction"
"""
            metadata_file.write_text(metadata_content)
            
            result = load_course_metadata(course_dir)
            
            assert result["course_name"] == "Test Course"
            assert len(result["sections"]) == 2
            assert result["sections"][0]["id"] == "general"
            assert result["sections"][0]["name"] == "General Questions"
    
    def test_load_course_metadata_missing_file(self):
        """Test loading metadata when file doesn't exist"""
        with tempfile.TemporaryDirectory() as temp_dir:
            course_dir = Path(temp_dir)
            
            result = load_course_metadata(course_dir)
            
            assert result["course_name"] == course_dir.name
            assert result["sections"] == []


class TestProcessQuestionFile:
    """Test question file processing functionality"""
    
    def test_process_question_file_valid(self):
        """Test processing a valid question file"""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Change to the temp directory to make relative paths work
            original_cwd = os.getcwd()
            os.chdir(temp_dir)
            
            try:
                # Create the _questions directory structure in temp dir
                questions_dir = Path("_questions") / "test-course" / "general"
                questions_dir.mkdir(parents=True)
                question_file = questions_dir / "test_question.md"
                
                content = """---
question: "How do I install Python?"
id: "test123"
sort_order: 1
---
You can install Python from https://python.org

Use the following command:
```bash
wget https://python.org/downloads/python.tar.gz
```
"""
                question_file.write_text(content)
                
                result = process_question_file("test-course", "General", question_file)
                
                assert result is not None
                assert result["question"] == "How do I install Python?"
                assert result["id"] == "test123"
                assert result["sort_order"] == 1
                assert result["section"] == "General"
                assert result["course"] == "test-course"
                # Check that URLs are properly handled
                assert 'href="https://python.org"' in result["content"]
                # URLs in code blocks should remain as plain text
                assert "https://python.org/downloads/python.tar.gz" in result["content"]
            finally:
                os.chdir(original_cwd)
    
    def test_process_question_file_missing_question(self):
        """Test processing a file missing the required question field"""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Change to the temp directory to make relative paths work
            original_cwd = os.getcwd()
            os.chdir(temp_dir)
            
            try:
                # Create the _questions directory structure in temp dir
                questions_dir = Path("_questions") / "test-course" / "general"
                questions_dir.mkdir(parents=True)
                question_file = questions_dir / "test_question.md"
                
                content = """---
id: "test123"
sort_order: 1
---
Some content without a question field."""
                question_file.write_text(content)
                
                result = process_question_file("test-course", "General", question_file)
                
                assert result is None
            finally:
                os.chdir(original_cwd)


if __name__ == "__main__":
    pytest.main([__file__])