.PHONY: faq website

# Extract FAQ data from Google Docs (with cleanup)
faq:
	uv run python process_faq.py

# Generate static website
website:
	uv run python generate_website.py