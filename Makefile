.PHONY: extract website clean help

# Default target
help:
	@echo "Available targets:"
	@echo "  extract  - Extract FAQ data from Google Docs and generate markdown files"
	@echo "  website  - Generate static website from markdown files"
	@echo "  clean    - Remove generated files"
	@echo "  help     - Show this help message"

# Extract FAQ data from Google Docs
extract:
	uv run faq_processor.py

# Generate static website
website:
	uv run generate.py