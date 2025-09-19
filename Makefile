.PHONY: faq website test test-unit test-int test-fast help

# Extract FAQ data from Google Docs (with cleanup)
faq:
	uv run python process_faq.py

# Generate static website
website:
	uv run python generate_website.py

# Test targets
test:
	@echo "🧪 Running all tests..."
	uv run pytest tests/ -v

test-unit:
	@echo "🔬 Running unit tests..."
	uv run pytest tests/unit/ -v

test-int:
	@echo "🔄 Running integration tests..."
	uv run pytest tests/integration/ -v

