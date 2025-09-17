# DataTalks.Club FAQ Jekyll Site

This is a Jekyll site that contains frequently asked questions and answers from DataTalks.Club courses.

## Structure

- `_questions/` - Individual question markdown files with Jekyll frontmatter
- `_layouts/` - Jekyll layout templates
- `images/` - Extracted images from the original FAQ documents
- `assets/css/` - Custom CSS styles
- `_config.yml` - Jekyll configuration
- `index.md` - Main landing page
- `[course].md` - Course index pages

## Quick Start

### Using the Automation Scripts

Choose your preferred method:

**PowerShell (Recommended for Windows):**
```powershell
# Initial setup
.\faq.ps1 setup

# Process FAQ documents and serve site
.\faq.ps1 dev
```

**Batch file (Windows Command Prompt):**
```cmd
# Initial setup
faq setup

# Process FAQ documents and serve site
faq dev
```

**Shell script (Linux/Mac/WSL):**
```bash
# Initial setup
./faq.sh setup

# Process FAQ documents and serve site
./faq.sh dev
```

**Makefile (Linux/Mac - has Windows compatibility issues):**
```bash
# Initial setup
make setup

# Process FAQ documents and serve site
make dev
```

### Available Commands

| Command | Description |
|---------|-------------|
| `setup` | Initial setup (install Python deps + Jekyll) |
| `process` | Process FAQ documents and generate Jekyll site |
| `serve` | Serve Jekyll site locally (http://localhost:4000) |
| `build` | Build Jekyll site for production |
| `dev` | Process + serve (development workflow) |
| `clean` | Clean generated files |
| `install` | Install Jekyll dependencies only |
| `stats` | Show site statistics |

## Manual Setup

If you prefer to run commands manually:

1. Install Jekyll and dependencies:
   ```bash
   gem install jekyll bundler
   bundle install
   ```

2. Process FAQ documents:
   ```bash
   uv run python faq_processor.py
   ```

3. Serve the site:
   ```bash
   bundle exec jekyll serve
   ```

4. Open your browser to `http://localhost:4000`

## Content

The site contains FAQ content from the following courses:
- Data Engineering Zoomcamp
- Machine Learning Zoomcamp
- MLOps Zoomcamp

Each question is stored as an individual markdown file with Jekyll frontmatter containing:
- `question` - The question text
- `section` - The section/category the question belongs to
- `course` - The course the question is from

## Processing

The content was processed from the original Google Docs FAQ documents using the `faq_processor.py` script, which:
1. Downloads and caches DOCX files
2. Extracts embedded images
3. Converts content to individual Jekyll question files
4. Generates course index pages
5. Creates the Jekyll site structure

## Images

Images are stored in `/images/[course]/` directories and referenced using Jekyll's absolute path syntax (`/images/...`) for proper display.
