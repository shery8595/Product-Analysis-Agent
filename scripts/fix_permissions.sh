#!/bin/bash

# Product Analysis Agent - Fix Permissions Script
# Fixes common permission and directory issues

set -e

echo "🔧 Fixing Permissions and Directory Issues"
echo "=========================================="

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Check if we're in the right directory
if [ ! -f "main.py" ] && [ ! -f "requirements.txt" ]; then
    print_error "Please run this script from the project root directory"
    exit 1
fi

# Fix directory permissions
print_warning "Fixing directory permissions..."

# Create necessary directories if they don't exist
DIRECTORIES=("logs" "reports" "data/executions" ".cache" "config/profiles" "examples/sample_outputs")
for dir in "${DIRECTORIES[@]}"; do
    if [ ! -d "$dir" ]; then
        print_warning "Creating missing directory: $dir"
        mkdir -p "$dir"
    fi
done

# Set proper permissions
print_warning "Setting directory permissions..."
chmod -R 755 logs reports data .cache config examples

# Fix file permissions for scripts
print_warning "Setting script permissions..."
if [ -f "scripts/install.sh" ]; then
    chmod +x scripts/install.sh
fi
if [ -f "scripts/run_analysis.sh" ]; then
    chmod +x scripts/run_analysis.sh
fi
if [ -f "run_analysis.sh" ]; then
    chmod +x run_analysis.sh
fi

# Fix Python file permissions
print_warning "Setting Python file permissions..."
find . -name "*.py" -exec chmod 644 {} \;

# Check for .env file
if [ ! -f ".env" ]; then
    print_warning ".env file not found"
    if [ -f ".env.example" ]; then
        print_warning "Copying .env.example to .env"
        cp .env.example .env
        print_success "Created .env file from template"
        print_warning "Please edit .env with your actual API keys"
    else
        print_error ".env.example not found"
    fi
else
    print_success ".env file exists"
fi

# Check virtual environment
if [ ! -d "venv" ]; then
    print_warning "Virtual environment not found"
    print_warning "Run: python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt"
else
    print_success "Virtual environment exists"
fi

# Check if profiles directory has necessary files
if [ ! -f "config/profiles/product_analysis.yaml" ]; then
    print_warning "Product analysis profile not found in config/profiles/"
    print_warning "Ensure your ROMA profiles are properly configured"
fi

# Verify directory structure
print_warning "Verifying directory structure..."
for dir in "${DIRECTORIES[@]}"; do
    if [ -d "$dir" ]; then
        print_success "✓ $dir"
    else
        print_error "✗ $dir - creation failed"
    fi
done

# Check write permissions
print_warning "Testing write permissions..."
TEST_FILE="logs/permission_test.txt"
if touch "$TEST_FILE" 2>/dev/null; then
    rm "$TEST_FILE"
    print_success "Write permissions OK"
else
    print_error "Write permission denied in logs directory"
    print_warning "Try: sudo chown -R $(whoami) . && chmod -R 755 ."
fi

print_success "Permission fix completed!"
echo ""
echo "If you're still having issues:"
echo "1. Check that all API keys are set in .env"
echo "2. Ensure virtual environment is activated: source venv/bin/activate"
echo "3. Verify all dependencies are installed: pip install -r requirements.txt"
echo "4. Check ROMA framework installation"
echo ""
echo "For ROMA-specific issues, see: https://github.com/sentient-agi/ROMA"
