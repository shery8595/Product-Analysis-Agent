#!/bin/bash

# Product Analysis Agent - Run Analysis Script
# Simplified script to run competitive analyses

set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

cd "$PROJECT_ROOT"

# Help function
show_help() {
    cat << EOF
Usage: $0 [OPTIONS] "PRODUCT_CATEGORY"

Product Analysis Agent - Run Competitive Analysis

OPTIONS:
    -c, --competitors COMPETITORS   Comma-separated list of competitors
    -d, --depth DEPTH               Analysis depth: basic, detailed, comprehensive (default: detailed)
    -o, --output FILE               Output file for report (default: auto-generated)
    -p, --profile PROFILE           ROMA profile to use (default: product_analysis)
    -h, --help                      Show this help message

EXAMPLES:
    $0 "AI coding assistants"
    $0 "project management software" -c "Jira,Asana,Trello"
    $0 "CRM software" -d basic -o my_report.json
    $0 "note-taking apps" -c "Evernote,Notion,Obsidian" -d comprehensive

API KEYS:
    Make sure your .env file contains:
    - OPENROUTER_API_KEY from https://openrouter.ai/
    - EXA_API_KEY from https://exa.ai/
EOF
}

# Default values
PRODUCT_CATEGORY=""
COMPETITORS=""
DEPTH="detailed"
OUTPUT_FILE=""
PROFILE="product_analysis"

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -c|--competitors)
            COMPETITORS="$2"
            shift 2
            ;;
        -d|--depth)
            DEPTH="$2"
            shift 2
            ;;
        -o|--output)
            OUTPUT_FILE="$2"
            shift 2
            ;;
        -p|--profile)
            PROFILE="$2"
            shift 2
            ;;
        -h|--help)
            show_help
            exit 0
            ;;
        -*)
            echo -e "${RED}Error: Unknown option $1${NC}"
            show_help
            exit 1
            ;;
        *)
            if [ -z "$PRODUCT_CATEGORY" ]; then
                PRODUCT_CATEGORY="$1"
            else
                echo -e "${RED}Error: Multiple product categories specified${NC}"
                show_help
                exit 1
            fi
            shift
            ;;
    esac
done

# Validate arguments
if [ -z "$PRODUCT_CATEGORY" ]; then
    echo -e "${RED}Error: Product category is required${NC}"
    show_help
    exit 1
fi

if [[ ! "$DEPTH" =~ ^(basic|detailed|comprehensive)$ ]]; then
    echo -e "${RED}Error: Depth must be basic, detailed, or comprehensive${NC}"
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo -e "${RED}Error: Virtual environment not found. Run install.sh first.${NC}"
    exit 1
fi

# Check if .env exists
if [ ! -f ".env" ]; then
    echo -e "${RED}Error: .env file not found. Run install.sh first.${NC}"
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

# Generate output filename if not specified
if [ -z "$OUTPUT_FILE" ]; then
    TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
    CATEGORY_SLUG=$(echo "$PRODUCT_CATEGORY" | tr ' ' '_' | tr '[:upper:]' '[:lower:]')
    OUTPUT_FILE="reports/${CATEGORY_SLUG}_analysis_${TIMESTAMP}.json"
fi

# Create reports directory if it doesn't exist
mkdir -p "$(dirname "$OUTPUT_FILE")"

# Prepare Python command
PYTHON_SCRIPT="
import asyncio
import sys
import os
sys.path.append('$PROJECT_ROOT')

from main import ProductAnalysisAgent

async def main():
    agent = ProductAnalysisAgent(profile='$PROFILE')
    
    competitors_list = None
    if '$COMPETITORS':
        competitors_list = [c.strip() for c in '$COMPETITORS'.split(',')]
    
    print(f'🚀 Starting analysis: {$PRODUCT_CATEGORY}')
    print(f'🔍 Competitors: {competitors_list or \\\"Auto-discover\\\"}')
    print(f'📊 Depth: {$DEPTH}')
    print(f'⚙️  Profile: {$PROFILE}')
    
    result = await agent.analyze_competitors(
        '$PRODUCT_CATEGORY',
        competitors=competitors_list,
        analysis_depth='$DEPTH'
    )
    
    # Save report
    agent.save_report(result, '$OUTPUT_FILE')
    
    print(f'\\\\n✅ Analysis complete!')
    print(f'📊 Competitors analyzed: {result[\\\"competitors_analyzed\\\"]}')
    print(f'💡 Recommendations: {len(result[\\\"recommendations\\\"])}')
    print(f'💾 Report saved to: {$OUTPUT_FILE}')
    
    # Print top recommendations
    print(f'\\\\n🎯 Top 3 recommendations:')
    for i, rec in enumerate(result['recommendations'][:3], 1):
        print(f'   {i}. {rec}')

if __name__ == \\\"__main__\\\":
    asyncio.run(main())
"

# Run the analysis
echo -e "${BLUE}🚀 Starting Product Analysis Agent${NC}"
echo -e "${BLUE}=========================================${NC}"
echo -e "${BLUE}Product:${NC} $PRODUCT_CATEGORY"
if [ -n "$COMPETITORS" ]; then
    echo -e "${BLUE}Competitors:${NC} $COMPETITORS"
else
    echo -e "${BLUE}Competitors:${NC} Auto-discover"
fi
echo -e "${BLUE}Depth:${NC} $DEPTH"
echo -e "${BLUE}Profile:${NC} $PROFILE"
echo -e "${BLUE}Output:${NC} $OUTPUT_FILE"
echo -e "${BLUE}=========================================${NC}"

python3 -c "$PYTHON_SCRIPT"

if [ $? -eq 0 ]; then
    echo -e "${GREEN}🎉 Analysis completed successfully!${NC}"
    
    # Offer to generate a markdown summary
    read -p "📄 Generate markdown summary? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        MARKDOWN_FILE="${OUTPUT_FILE%.json}.md"
        python3 -c "
import json
import sys
sys.path.append('$PROJECT_ROOT')
from examples.api_integration import ProductAnalysisAPI

with open('$OUTPUT_FILE', 'r') as f:
    data = json.load(f)

api = ProductAnalysisAPI()
markdown = api.export_to_markdown(data)

with open('$MARKDOWN_FILE', 'w', encoding='utf-8') as f:
    f.write(markdown)

print(f'Markdown summary saved to: $MARKDOWN_FILE')
"
    fi
else
    echo -e "${RED}❌ Analysis failed${NC}"
    exit 1
fi
