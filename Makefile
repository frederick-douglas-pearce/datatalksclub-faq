# DataTalks.Club FAQ Makefile
# Easy commands to manage the FAQ Jekyll site

.PHONY: help install process serve build clean setup dev stats validate

# Default target
help:
	@echo "DataTalks.Club FAQ Management"
	@echo "============================="
	@echo ""
	@echo "Available commands:"
	@echo "  make setup     - Initial setup (install Python deps + Jekyll)"
	@echo "  make process   - Process FAQ documents and generate Jekyll site"
	@echo "  make serve     - Serve Jekyll site locally (http://localhost:4000)"
	@echo "  make build     - Build Jekyll site for production"
	@echo "  make dev       - Process + serve (development workflow)"
	@echo "  make clean     - Clean generated files"
	@echo "  make install   - Install Jekyll dependencies only"
	@echo "  make stats     - Show site statistics"
	@echo ""
	@echo "Quick start:"
	@echo "  make setup && make dev"

# Initial setup - install all dependencies
setup:
	@echo "Setting up DataTalks.Club FAQ..."
	@echo "Installing Python dependencies..."
	uv sync
	@echo "Installing Jekyll dependencies..."
	gem install bundler jekyll
	bundle install
	@echo "Setup complete! Run 'make dev' to start development."

# Install Jekyll dependencies only
install:
	@echo "Installing Jekyll dependencies..."
	bundle install

# Process FAQ documents from Google Docs
process:
	@echo "Processing FAQ documents..."
	@echo "This will:"
	@echo "  - Download DOCX files from Google Docs"
	@echo "  - Extract images and content"
	@echo "  - Generate Jekyll site structure"
	@echo ""
	uv run python faq_processor.py
	@echo ""
	@echo "Processing complete!"

# Serve Jekyll site locally
serve:
	@echo "Starting Jekyll development server..."
	@echo "Site will be available at: http://localhost:4000"
	@echo "Press Ctrl+C to stop"
	@echo ""
	bundle exec jekyll serve --livereload

# Build Jekyll site for production
build:
	@echo "Building Jekyll site for production..."
	bundle exec jekyll build
	@echo "Site built in _site/ directory"

# Development workflow: process + serve
dev: process serve

# Clean generated files
clean:
	@echo "Cleaning generated files..."
	rm -rf _site
	rm -rf .jekyll-cache
	rm -rf _questions
	rm -rf _layouts
	rm -rf images
	rm -rf markdown
	rm -f _config.yml
	rm -f index.md
	rm -f *-zoomcamp.md
	@echo "Clean complete!"

# Quick rebuild - clean cache and rebuild
rebuild:
	@echo "Rebuilding site..."
	rm -rf _site .jekyll-cache
	bundle exec jekyll build

# Check Jekyll site for issues
check:
	@echo "Checking Jekyll site..."
	bundle exec jekyll doctor
	bundle exec jekyll build --dry-run

# Update dependencies
update:
	@echo "Updating dependencies..."
	uv sync --upgrade
	bundle update

# Statistics about the generated site
stats:
	@echo "Site Statistics"
	@echo "==============="
	@if [ -d "_questions" ]; then echo "Questions: $(ls _questions/*.md 2>/dev/null | wc -l)"; else echo "Questions: 0"; fi
	@if [ -d "images" ]; then echo "Images: $(find images -name '*.png' -o -name '*.jpg' -o -name '*.gif' 2>/dev/null | wc -l)"; else echo "Images: 0"; fi
	@if ls *-zoomcamp.md >/dev/null 2>&1; then echo "Courses: $(ls *-zoomcamp.md 2>/dev/null | wc -l)"; else echo "Courses: 0"; fi
	@if [ -d "_layouts" ]; then echo "Layouts: $(ls _layouts/*.html 2>/dev/null | wc -l)"; else echo "Layouts: 0"; fi
	@echo ""
	@echo "Course breakdown:"
	@if [ -d "_questions" ]; then \
		echo "  Data Engineering: $(ls _questions/data-engineering-*.md 2>/dev/null | wc -l)"; \
		echo "  Machine Learning: $(ls _questions/machine-learning-*.md 2>/dev/null | wc -l)"; \
		echo "  MLOps: $(ls _questions/mlops-*.md 2>/dev/null | wc -l)"; \
	fi

# Validate that all images exist
validate:
	@echo "Validating image references..."
	@if [ -d "_questions" ]; then \
		python3 -c "import glob, re, os; \
		errors = 0; \
		for file in glob.glob('_questions/*.md'): \
			with open(file, 'r', encoding='utf-8') as f: \
				content = f.read(); \
				images = re.findall(r'!\[Image\]\(([^)]+)\)', content); \
				for img in images: \
					img_path = img.lstrip('/'); \
					if not os.path.exists(img_path): \
						print(f'Missing image: {img} in {file}'); \
						errors += 1; \
		print('✓ All image references are valid' if errors == 0 else f'✗ Found {errors} missing images'); \
		exit(1 if errors > 0 else 0)"; \
	else \
		echo "No questions directory found. Run 'make process' first."; \
	fi