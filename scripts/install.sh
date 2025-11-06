#!/bin/bash

# Product Analysis Agent - Installation Script
echo "🚀 Installing Product Analysis Agent..."

# Check Python version
python3 --version || { echo "❌ Python 3 required"; exit 1; }

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Upgrade pip
echo "🔄 Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# Fix ULID compatibility issue
echo "🔧 Fixing ULID compatibility..."
pip uninstall -y ulid ulid-py ulid3
pip install ulid-py==1.1.0

# Setup environment
echo "⚙️ Setting up environment..."
if [ ! -f .env ]; then
    cp .env.example .env
    echo "📝 Please edit .env file with your API keys"
else
    echo "✅ .env file already exists"
fi

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p logs
mkdir -p data/executions
mkdir -p .cache

echo "🎉 Installation complete!"
echo "👉 Next steps:"
echo "   1. Edit .env with your API keys"
echo "   2. Run: python main.py"
echo "   3. Or try: python examples/basic_usage.py"
