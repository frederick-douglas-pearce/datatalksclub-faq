#!/bin/bash
# DataTalks.Club FAQ Management Script for Git Bash/Linux/Mac
# Usage: ./faq.sh [command]

show_help() {
    echo "DataTalks.Club FAQ Management"
    echo "============================="
    echo ""
    echo "Available commands:"
    echo "  ./faq.sh setup     - Initial setup (install Python deps + Jekyll)"
    echo "  ./faq.sh process   - Process FAQ documents and generate Jekyll site"
    echo "  ./faq.sh serve     - Serve Jekyll site locally (http://localhost:4000)"
    echo "  ./faq.sh build     - Build Jekyll site for production"
    echo "  ./faq.sh dev       - Process + serve (development workflow)"
    echo "  ./faq.sh clean     - Clean generated files"
    echo "  ./faq.sh install   - Install Jekyll dependencies only"
    echo "  ./faq.sh stats     - Show site statistics"
    echo ""
    echo "Quick start:"
    echo "  ./faq.sh setup"
    echo "  ./faq.sh dev"
}

setup() {
    echo "Setting up DataTalks.Club FAQ..."
    echo "Installing Python dependencies..."
    uv sync
    echo "Installing Jekyll dependencies..."
    gem install bundler jekyll
    bundle install
    echo "Setup complete! Run './faq.sh dev' to start development."
}

install_deps() {
    echo "Installing Jekyll dependencies..."
    gem install bundler jekyll
    bundle install
}

process_faq() {
    echo "Processing FAQ documents..."
    echo "This will:"
    echo "  - Download DOCX files from Google Docs"
    echo "  - Extract images and content"
    echo "  - Generate Jekyll site structure"
    echo ""
    uv run python faq_processor.py
    echo ""
    echo "Processing complete!"
}

serve_site() {
    echo "Starting Jekyll development server..."
    echo "Site will be available at: http://localhost:4000"
    echo "Press Ctrl+C to stop"
    echo ""
    bundle exec jekyll serve --livereload
}

build_site() {
    echo "Building Jekyll site for production..."
    bundle exec jekyll build
    echo "Site built in _site/ directory"
}

dev_workflow() {
    process_faq
    serve_site
}

clean_files() {
    echo "Cleaning generated files..."
    rm -rf _site .jekyll-cache _questions _layouts images markdown
    rm -f _config.yml index.md *-zoomcamp.md
    echo "Clean complete!"
}

show_stats() {
    echo "Site Statistics"
    echo "==============="
    
    if [ -d "_questions" ]; then
        questions=$(find _questions -name "*.md" | wc -l)
    else
        questions=0
    fi
    echo "Questions: $questions"
    
    if [ -d "images" ]; then
        images=$(find images -name "*.png" -o -name "*.jpg" -o -name "*.gif" | wc -l)
    else
        images=0
    fi
    echo "Images: $images"
    
    courses=$(ls *-zoomcamp.md 2>/dev/null | wc -l || echo 0)
    echo "Courses: $courses"
    
    if [ -d "_layouts" ]; then
        layouts=$(find _layouts -name "*.html" | wc -l)
    else
        layouts=0
    fi
    echo "Layouts: $layouts"
    
    if [ -d "_questions" ]; then
        echo ""
        echo "Course breakdown:"
        echo "  Data Engineering: $(find _questions -name "data-engineering-*.md" | wc -l)"
        echo "  Machine Learning: $(find _questions -name "machine-learning-*.md" | wc -l)"
        echo "  MLOps: $(find _questions -name "mlops-*.md" | wc -l)"
    fi
}

# Main script logic
case "$1" in
    "help"|""|"-h"|"--help")
        show_help
        ;;
    "setup")
        setup
        ;;
    "install")
        install_deps
        ;;
    "process")
        process_faq
        ;;
    "serve")
        serve_site
        ;;
    "build")
        build_site
        ;;
    "dev")
        dev_workflow
        ;;
    "clean")
        clean_files
        ;;
    "stats")
        show_stats
        ;;
    *)
        echo "Unknown command: $1"
        echo ""
        show_help
        exit 1
        ;;
esac