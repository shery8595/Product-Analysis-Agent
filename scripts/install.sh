#!/bin/bash

# Product Analysis Agent - Installation Script
# Complete setup for the competitive analysis agent

set -e  # Exit on any error

echo "🚀 Product Analysis Agent - Installation"
echo "========================================"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Helper functions
print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Check system requirements
print_info "Checking system requirements..."

# Check Python version
if ! command -v python3 &> /dev/null; then
    print_error "Python 3 is required but not installed."
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
print_info "Python version: $PYTHON_VERSION"

if [[ $(echo "$PYTHON_VERSION < 3.10" | bc -l) -eq 1 ]]; then
    print_error "Python 3.10 or higher is required. Current version: $PYTHON_VERSION"
    exit 1
fi

# Check for virtual environment
print_info "Setting up virtual environment..."

if [ ! -d "venv" ]; then
    print_info "Creating virtual environment..."
    python3 -m venv venv
    print_success "Virtual environment created"
else
    print_info "Virtual environment already exists"
fi

# Activate virtual environment
print_info "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
print_info "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
print_info "Installing dependencies from requirements.txt..."
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    print_success "Dependencies installed successfully"
else
    print_error "requirements.txt not found"
    exit 1
fi

# Fix common compatibility issues
print_info "Checking for compatibility issues..."

# Fix ULID compatibility
print_info "Ensuring ULID compatibility..."
pip uninstall -y ulid ulid-py ulid3 2>/dev/null || true
pip install ulid-py==1.1.0

# Setup environment configuration
print_info "Setting up environment configuration..."

if [ ! -f ".env" ]; then
    if [ -f ".env.example" ]; then
        cp .env.example .env
        print_warning "Created .env file from template"
        print_warning "Please edit .env file with your actual API keys"
    else
        print_error ".env.example not found"
        exit 1
    fi
else
    print_info ".env file already exists"
fi

# Create necessary directories
print_info "Creating necessary directories..."
mkdir -p logs
mkdir -p reports
mkdir -p data/executions
mkdir -p .cache
mkdir -p config/profiles

# Set proper permissions
print_info "Setting directory permissions..."
chmod -R 755 logs reports data .cache config

# Verify directory structure
print_info "Verifying directory structure..."
directories=("logs" "reports" "data/executions" ".cache" "config/profiles")
for dir in "${directories[@]}"; do
    if [ -d "$dir" ]; then
        print_success "✓ $dir"
    else
        print_error "✗ $dir - directory missing"
    fi
done

# Check if profiles are set up
print_info "Checking configuration profiles..."
if [ -f "config/profiles/product_analysis.yaml" ]; then
    print_success "Product analysis profile found"
else
    print_warning "Product analysis profile not found - ensure it's created"
fi

# Test basic imports
print_info "Testing Python imports..."
if python3 -c "
import sys
sys.path.append('.')
try:
    from main import ProductAnalysisAgent
    import asyncio
    import aiohttp
    print('✅ Basic imports successful')
except ImportError as e:
    print(f'❌ Import error: {e}')
    sys.exit(1)
"; then
    print_success "Import test passed"
else
    print_error "Import test failed"
    exit 1
fi

# Create run script
print_info "Creating run script..."
cat > run_analysis.sh << 'EOF'
#!/bin/bash

# Product Analysis Agent - Run Script
source venv/bin/activate

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "❌ .env file not found. Please run install.sh first."
    exit 1
fi

# Run the analysis
python main.py "$@"
EOF

chmod +x run_analysis.sh

# Create quick start examples
print_info "Creating example scripts..."
cat > examples/quick_start.py << 'EOF'
#!/usr/bin/env python3
"""
Quick Start Example for Product Analysis Agent
"""
import asyncio
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import ProductAnalysisAgent

async def quick_example():
    """Quick example to verify installation"""
    print("🚀 Testing Product Analysis Agent...")
    
    agent = ProductAnalysisAgent()
    
    # Quick test with small analysis
    result = await agent.analyze_competitors(
        "note-taking apps",
        competitors=["Evernote", "Notion"],
        analysis_depth="basic"
    )
    
    print(f"✅ Test completed!")
    print(f"📊 Analyzed: {result['product_category']}")
    print(f"🔍 Competitors: {result['competitors_analyzed']}")
    print(f"💡 Recommendations: {len(result['recommendations'])}")

if __name__ == "__main__":
    asyncio.run(quick_example())
EOF

print_success "Installation completed successfully!"
echo ""
echo "🎯 NEXT STEPS:"
echo "1. Edit the .env file with your API keys:"
echo "   - OpenRouter API key from https://openrouter.ai/"
echo "   - Exa API key from https://exa.ai/"
echo ""
echo "2. Test the installation:"
echo "   python examples/quick_start.py"
echo ""
echo "3. Run a full analysis:"
echo "   python main.py"
echo "   or"
echo "   ./run_analysis.sh"
echo ""
echo "4. Check the examples:"
echo "   python examples/basic_usage.py"
echo ""
echo "📚 Documentation: See README.md for detailed usage"
echo ""
echo "Need help? Check the troubleshooting section in README.md"
