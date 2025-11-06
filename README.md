<div align="center">

# 🚀 Product Analysis Agent

### Automated Competitive Intelligence powered by ROMA Framework

[![ROMA Framework](https://img.shields.io/badge/ROMA-Framework-blue?style=flat-square)](https://github.com/sentient-agi/ROMA)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg?style=flat-square)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[Features](#-key-features) • [Quick Start](#-quick-start) • [Examples](#-usage-examples) • [Architecture](#-architecture) • [Documentation](#-documentation)

---

*Analyze competitors, generate insights, and create comprehensive market reports — fully automated.*

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [How It Works](#-how-it-works)
- [Quick Start](#-quick-start)
- [Usage Examples](#-usage-examples)
- [Architecture](#-architecture)
- [Configuration](#️-configuration)
- [Project Structure](#-project-structure)
- [API Integration](#-api-integration)
- [Contributing](#-contributing)
- [Troubleshooting](#-troubleshooting)
- [Roadmap](#-roadmap)
- [License](#-license)

---

## 🎯 Overview

**Product Analysis Agent** is a specialized competitive intelligence tool built on the [ROMA (Recursive-Open-Meta-Agent)](https://github.com/sentient-agi/ROMA) framework. It automates the entire market research workflow — from competitor discovery to comprehensive report generation — using AI-powered agents and free-tier APIs.

### 💡 Perfect For

- **Product Managers** conducting market analysis
- **Founders** researching competitive landscapes
- **Marketing Teams** developing positioning strategies
- **Sales Teams** preparing competitive battle cards
- **Investors** performing due diligence on markets

### 🎁 What You Get
```bash
Input:  "AI coding assistants"
        + ["GitHub Copilot", "Tabnine", "Cursor", ...]

Output: ✅ Comprehensive competitive analysis report
        ✅ Feature comparison matrix (27+ features)
        ✅ Pricing analysis and positioning insights
        ✅ SWOT analysis for each competitor
        ✅ 7+ strategic recommendations
        ✅ Market trends and opportunities
```

---

## ✨ Key Features

<table>
<tr>
<td width="50%">

### 🔍 **Automated Research**
- **Intelligent competitor discovery** using Exa.ai search
- **Automatic website analysis** and content extraction
- **PDF document processing** for spec sheets
- **Multi-source data aggregation**

### 🤖 **AI-Powered Analysis**
- **ROMA meta-agent orchestration** (Atomizer → Planner → Executor → Aggregator)
- **LLM-driven insights** using OpenRouter (free tier)
- **Contextual feature extraction** from web content
- **SWOT analysis generation** with strategic recommendations

</td>
<td width="50%">

### 📊 **Rich Outputs**
- **Feature comparison matrices** with 20+ dimensions
- **Comprehensive markdown reports** ready for distribution
- **Structured JSON data** for programmatic access
- **Visualization-ready** chart data exports

### 🎛️ **Flexible & Extensible**
- **Custom analysis profiles** via YAML configuration
- **Pluggable toolkits** (Exa, FileToolkit, WebScraper)
- **Three analysis depths**: basic, detailed, comprehensive
- **Batch processing** for multiple markets

</td>
</tr>
</table>

---

## 🔄 How It Works

The agent follows ROMA's **"Launch Product Analysis"** workflow:
```
┌─────────────────────────────────────────────────────────────┐
│  INPUT: Product Category + Optional Competitor List         │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│  PHASE 1: SEARCH (Executor Agent)                           │
│  🔍 Discover competitors using Exa.ai neural search         │
│  📊 Gather product pages, documentation, pricing info       │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│  PHASE 2: ANALYZE (Executor Agent + Toolkits)               │
│  🌐 Scrape and parse competitor websites                    │
│  📄 Extract features, pricing, target audiences             │
│  🔎 Analyze PDF documents and spec sheets                   │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│  PHASE 3: STRUCTURE (Planner Agent)                         │
│  🧩 Create comparison framework                             │
│  📐 Define analysis dimensions                              │
│  🎯 Identify key differentiators                            │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│  PHASE 4: SYNTHESIZE (Aggregator Agent)                     │
│  🤖 Generate SWOT analyses                                  │
│  💡 Create strategic recommendations                        │
│  📈 Identify market gaps and opportunities                  │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│  OUTPUT: Comprehensive Market Analysis Report               │
│  📊 JSON + Markdown formats                                 │
│  🎨 Visualization-ready data                                │
└─────────────────────────────────────────────────────────────┘
```

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.10+** installed
- **[OpenRouter API Key](https://openrouter.ai/)** (free tier available)
- **[Exa.ai API Key](https://exa.ai/)** (free tier: 1,000 searches/month)

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/product-analysis-agent.git
cd product-analysis-agent

# Run automated installation
chmod +x scripts/install.sh
./scripts/install.sh

# Configure your API keys
cp .env.example .env
nano .env  # Add your OPENROUTER_API_KEY and EXA_API_KEY
```

**Manual Installation:**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your API keys
```

### First Run
```bash
# Run the default example
python main.py

# Expected output:
# 🚀 Starting competitive analysis for: AI coding assistants
# 🔍 Phase 1: Searching competitor data...
# 📊 Phase 2: Analyzing competitors...
#    ✅ Analyzed: GitHub Copilot
#    ✅ Analyzed: Amazon CodeWhisperer
#    ✅ Analyzed: Tabnine
# 📈 Phase 3: Generating comprehensive report...
# 🎉 Analysis complete! Processed 3 competitors
```

---

## 💻 Usage Examples

### Command Line Interface
```bash
# Basic analysis
./scripts/run_analysis.sh "AI coding assistants"

# With specific competitors
./scripts/run_analysis.sh "project management software" \
  -c "Jira,Asana,Trello,Monday.com"

# Different analysis depths
./scripts/run_analysis.sh "CRM software" -d comprehensive

# Custom output location
./scripts/run_analysis.sh "note-taking apps" \
  -c "Notion,Evernote,Obsidian" \
  -o custom_report.json
```

### Python API
```python
from main import ProductAnalysisAgent
import asyncio

async def analyze_market():
    # Initialize agent
    agent = ProductAnalysisAgent()
    
    # Run analysis
    result = await agent.analyze_competitors(
        product_category="AI coding assistants",
        competitors=["GitHub Copilot", "Tabnine", "Cursor"],
        analysis_depth="detailed"  # basic, detailed, comprehensive
    )
    
    # Access results
    print(f"Analyzed: {result['competitors_analyzed']} competitors")
    print(f"Features: {len(result['feature_comparison_matrix'])}")
    print(f"Recommendations: {len(result['recommendations'])}")
    
    # Save report
    report_path = agent.save_report(result)
    print(f"Report saved: {report_path}")
    
    return result

# Run the analysis
asyncio.run(analyze_market())
```

### Batch Processing
```python
import asyncio
from main import ProductAnalysisAgent

async def batch_analysis():
    agent = ProductAnalysisAgent()
    
    markets = [
        {
            "category": "video conferencing",
            "competitors": ["Zoom", "Microsoft Teams", "Google Meet"]
        },
        {
            "category": "password managers",
            "competitors": ["1Password", "LastPass", "Bitwarden"]
        }
    ]
    
    for market in markets:
        result = await agent.analyze_competitors(
            market["category"],
            market["competitors"],
            analysis_depth="basic"
        )
        agent.save_report(result)

asyncio.run(batch_analysis())
```

---

## 📊 Example Output

### Terminal Output
```
🚀 Product Analysis Agent
==========================================
🔍 Analyzing: AI Coding Assistants Market

📊 Phase 1: Searching competitor data...
   ✅ Found 5 competitors

📊 Phase 2: Analyzing competitors...
   ✅ Analyzed: GitHub Copilot - 23 features found
   ✅ Analyzed: Amazon CodeWhisperer - 19 features found
   ✅ Analyzed: Tabnine - 17 features found
   ✅ Analyzed: Cursor - 21 features found
   ✅ Analyzed: Codeium - 15 features found

📈 Phase 3: Generating comprehensive report...

🎉 Analysis complete! Processed 5 competitors

📈 COMPETITIVE ANALYSIS RESULTS
==========================================
🏢 Product Category: AI Coding Assistants
🔍 Competitors Analyzed: 5
📊 Features Compared: 27 unique features
💡 Strategic Recommendations: 7

🎯 TOP RECOMMENDATIONS:
   1. Focus on vertical-specific solutions for fintech/healthcare
   2. Enhance security features and compliance certifications
   3. Develop mobile IDE integration capabilities
   4. Create flexible pricing tiers for different organization sizes
   5. Invest in real-time collaboration features

💾 Report saved to: reports/ai_coding_assistants_20240115_143022.json
📄 Markdown report: reports/ai_coding_assistants_20240115_143022.md
```

### JSON Report Structure
```json
{
  "product_category": "AI Coding Assistants",
  "report_timestamp": "2024-01-15T14:30:22",
  "competitors_analyzed": 5,
  "analysis_depth": "detailed",
  
  "feature_comparison_matrix": {
    "GitHub Copilot": {
      "multi_language_support": true,
      "ide_integration": true,
      "security_scanning": false,
      "free_tier": false,
      "on_premise_deployment": false,
      "codebase_awareness": true
    },
    "Amazon CodeWhisperer": {
      "multi_language_support": true,
      "ide_integration": true,
      "security_scanning": true,
      "free_tier": true,
      "on_premise_deployment": false,
      "codebase_awareness": false
    }
  },
  
  "market_analysis": "The AI coding assistants market is experiencing rapid growth...",
  
  "key_findings": [
    "Market dominated by Microsoft/GitHub and AWS",
    "Free tier becoming competitive necessity",
    "Security features critical for enterprise adoption",
    "Mobile development support is an underserved niche"
  ],
  
  "recommendations": [
    "Focus on vertical-specific solutions for high-value industries",
    "Enhance security features with compliance certifications",
    "Develop mobile IDE integration capabilities"
  ],
  
  "swot_analyses": {
    "GitHub Copilot": {
      "strengths": [
        "Deep GitHub ecosystem integration",
        "Microsoft backing and resources",
        "Large training dataset"
      ],
      "weaknesses": [
        "Privacy concerns for enterprises",
        "Higher pricing point",
        "Occasional irrelevant suggestions"
      ],
      "opportunities": [
        "Enterprise market expansion",
        "API and third-party integrations",
        "Vertical-specific models"
      ],
      "threats": [
        "Open source alternatives",
        "Regulatory scrutiny on AI code",
        "Rapid competitor innovation"
      ]
    }
  }
}
```

### Markdown Report Sample

See [examples/sample_outputs/competitive_analysis_sample.md](examples/sample_outputs/competitive_analysis_sample.md) for a full example.

---

## 🏗️ Architecture

### System Architecture
```
┌─────────────────────────────────────────────────────────────┐
│                    ROMA Framework                           │
│           Multi-Agent Orchestration Layer                   │
└─────────────────────────────────────────────────────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
   ┌─────────┐       ┌─────────┐       ┌─────────┐
   │Atomizer │       │ Planner │       │Executor │
   │  Agent  │──────▶│  Agent  │──────▶│  Agent  │
   └─────────┘       └─────────┘       └─────────┘
        │                  │                  │
        │                  │                  ▼
        │                  │           ┌─────────────┐
        │                  │           │  Toolkits   │
        │                  │           ├─────────────┤
        │                  │           │ • Exa API   │
        │                  │           │ • FileKit   │
        │                  │           │ • WebKit    │
        │                  │           │ • PDFKit    │
        │                  │           └─────────────┘
        │                  │
        └──────────┬───────┘
                   ▼
            ┌─────────────┐
            │ Aggregator  │
            │    Agent    │
            └─────────────┘
                   │
                   ▼
            ┌─────────────┐
            │   Report    │
            │  Generator  │
            └─────────────┘
```

### Agent Responsibilities

| Agent | Role | Key Functions |
|-------|------|---------------|
| **Atomizer** | Task decomposition | Breaks analysis into subtasks, validates inputs |
| **Planner** | Strategy design | Creates comparison framework, defines dimensions |
| **Executor** | Data collection | Searches web, analyzes sites, extracts features |
| **Aggregator** | Synthesis | Generates insights, SWOT analyses, recommendations |

### Toolkit Integration
```yaml
toolkits:
  - name: Exa Search
    purpose: Neural web search for competitor discovery
    api: https://api.exa.ai
    
  - name: FileToolkit
    purpose: PDF and document processing
    formats: [pdf, txt, md]
    
  - name: WebScraper
    purpose: Website analysis and content extraction
    capabilities: [html_parsing, feature_extraction, pricing_detection]
```

---

## ⚙️ Configuration

### Environment Variables (.env)
```bash
# Required API Keys
OPENROUTER_API_KEY=sk-or-v1-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
EXA_API_KEY=your_exa_api_key_here

# Optional Configuration
OPENROUTER_MODEL=openrouter/z-ai/glm-4.5-air:free
MAX_COMPETITORS=5
ANALYSIS_DEPTH=detailed  # basic/detailed/comprehensive
OUTPUT_FORMAT=markdown   # markdown/json/html

# Performance
REQUEST_TIMEOUT=120
MAX_CONCURRENT_SEARCHES=3
CACHE_ENABLED=true
```

### Analysis Profile (config/profiles/product_analysis.yaml)
```yaml
name: "product_analysis"
description: "Competitive analysis with market research"

# Analysis Configuration
analysis:
  max_competitors: 5
  depth: detailed
  include_pricing_analysis: true
  include_feature_matrix: true
  include_swot_analysis: true
  output_sections:
    - executive_summary
    - market_overview
    - competitor_profiles
    - feature_comparison
    - pricing_analysis
    - strategic_recommendations

# Agent Settings
agents:
  executor:
    llm:
      model: "openrouter/z-ai/glm-4.5-air:free"
      temperature: 0.5
      max_tokens: 4000
    toolkits:
      - class_name: MCPToolkit
        toolkit_config:
          server_name: exa
          url: https://mcp.exa.ai/mcp
      - class_name: FileToolkit
      - class_name: CalculatorToolkit

  aggregator:
    llm:
      temperature: 0.2
      max_tokens: 5000
    agent_config:
      synthesis_method: comparative_analysis
      output_format: markdown
```

### Customizing Analysis Depth
```python
# Basic: Fast overview (5-10 minutes)
result = await agent.analyze_competitors(
    "CRM software",
    analysis_depth="basic"
)

# Detailed: Comprehensive analysis (15-30 minutes)
result = await agent.analyze_competitors(
    "project management tools",
    analysis_depth="detailed"  # Default
)

# Comprehensive: Deep dive with all features (30-60 minutes)
result = await agent.analyze_competitors(
    "AI platforms",
    analysis_depth="comprehensive"
)
```

---

## 📁 Project Structure
```
product-analysis-agent/
├── main.py                           # Core agent implementation
├── requirements.txt                  # Python dependencies
├── .env.example                      # Environment template
├── .gitignore
│
├── config/
│   └── profiles/
│       └── product_analysis.yaml     # ROMA agent configuration
│
├── tools/                            # Custom analysis tools
│   ├── __init__.py
│   ├── exa_search_tool.py           # Exa.ai search integration
│   ├── web_scraper_tool.py          # Website analysis
│   └── pdf_analysis_tool.py         # PDF processing
│
├── scripts/                          # Utility scripts
│   ├── install.sh                   # Automated setup
│   ├── run_analysis.sh              # CLI runner
│   └── fix_permissions.sh           # Troubleshooting
│
├── examples/                         # Usage examples
│   ├── basic_usage.py               # Simple examples
│   ├── api_integration.py           # API patterns
│   ├── quick_start.py               # Test installation
│   └── sample_outputs/
│       └── competitive_analysis_sample.md
│
├── reports/                          # Generated reports (gitignored)
├── data/                             # Execution data (gitignored)
├── logs/                             # Application logs (gitignored)
└── .cache/                           # Temporary cache (gitignored)
```

---

## 🔌 API Integration

### Exporting to Other Formats
```python
from examples.api_integration import ProductAnalysisAPI

api = ProductAnalysisAPI()

# Run analysis
result = await api.analyze_competitors_api("CRM software")

# Export to Markdown
markdown = await api.export_to_markdown(result)
with open("report.md", "w") as f:
    f.write(markdown)

# Generate chart data for visualization
chart_data = await api.generate_comparison_chart(result)
# Use with Plotly, Chart.js, etc.
```

### Slack Integration
```python
# Send analysis summary to Slack
webhook_url = "https://hooks.slack.com/services/YOUR/WEBHOOK/URL"
await api.send_to_slack(result, webhook_url)
```

### Webhook Notifications
```python
# POST analysis results to your API
import aiohttp

async def send_to_api(analysis_result):
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://your-api.com/analysis",
            json=analysis_result
        ) as response:
            return response.status == 200
```

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Ways to Contribute

- 🐛 **Bug Reports**: Open an issue with reproduction steps
- 💡 **Feature Requests**: Describe new analysis capabilities
- 🔧 **Code Contributions**: Submit PRs for new features
- 📚 **Documentation**: Improve guides and examples
- 🧪 **Testing**: Add test cases and edge scenarios

### Development Setup
```bash
# Fork and clone
git clone https://github.com/yourusername/product-analysis-agent.git
cd product-analysis-agent

# Create feature branch
git checkout -b feature/your-feature-name

# Install development dependencies
pip install -r requirements.txt
pip install pytest black flake8

# Make changes and test
pytest tests/
black .
flake8 .

# Submit PR
git push origin feature/your-feature-name
```

### Adding New Tools
```python
# tools/your_custom_tool.py
from roma import tool

@tool("custom_analysis", description="Your custom analysis")
async def custom_analysis(data: dict) -> dict:
    # Your implementation
    return analysis_result
```

Register in `config/profiles/product_analysis.yaml`:
```yaml
toolkits:
  - class_name: CustomToolkit
    enabled: true
```

---

## 🐛 Troubleshooting

### Common Issues

**Issue: "Missing API keys" error**
```bash
# Solution: Ensure .env file exists and has valid keys
cp .env.example .env
nano .env  # Add your keys
```

**Issue: "ImportError: No module named 'roma'"**
```bash
# Solution: Reinstall dependencies
pip install --upgrade sentient-agent-framework roma-dspy
```

**Issue: "Exa search timeout"**
```bash
# Solution: Increase timeout in .env
REQUEST_TIMEOUT=180
```

**Issue: Permission denied on scripts**
```bash
# Solution: Fix permissions
chmod +x scripts/*.sh
./scripts/fix_permissions.sh
```

### Debug Mode
```bash
# Enable debug logging
DEBUG=true python main.py
```

### Getting Help

- 📖 Check [ROMA Documentation](https://github.com/sentient-agi/ROMA)
- 💬 Open a [GitHub Issue](https://github.com/yourusername/product-analysis-agent/issues)
- 📧 Contact: your-email@example.com

---

## 🗺️ Roadmap

### Current Version: 1.0.0
- ✅ Multi-agent ROMA integration
- ✅ Exa.ai search integration
- ✅ Website and PDF analysis
- ✅ SWOT analysis generation
- ✅ Markdown/JSON report outputs

### Planned Features

**v1.1.0** (Q2 2024)
- [ ] Real-time market monitoring
- [ ] Automated report scheduling
- [ ] Email report distribution
- [ ] Interactive HTML reports

**v1.2.0** (Q3 2024)
- [ ] Data visualization dashboard
- [ ] Excel/Google Sheets export
- [ ] API rate limiting and caching
- [ ] Multi-language support

**v2.0.0** (Q4 2024)
- [ ] Real-time collaboration features
- [ ] Historical trend analysis
- [ ] Custom ML model training
- [ ] Enterprise SSO integration

### Community Requests
Vote on features in [GitHub Discussions](https://github.com/yourusername/product-analysis-agent/discussions)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
MIT License

Copyright (c) 2024 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

## 🙏 Acknowledgments

- **[ROMA Framework](https://github.com/sentient-agi/ROMA)** - Multi-agent orchestration
- **[Exa.ai](https://exa.ai/)** - Neural search API
- **[OpenRouter](https://openrouter.ai/)** - LLM API aggregation
- **DSPy** - LLM programming framework

---

## 📞 Contact & Support

- **GitHub**: [@yourusername](https://github.com/yourusername)
- **Email**: your-email@example.com
- **Twitter**: [@yourhandle](https://twitter.com/yourhandle)
- **Issues**: [Report a bug](https://github.com/yourusername/product-analysis-agent/issues)

---

<div align="center">

**⭐ Star this repo if you find it useful!**

Made with ❤️ using [ROMA](https://github.com/sentient-agi/ROMA)

[Report Bug](https://github.com/yourusername/product-analysis-agent/issues) • [Request Feature](https://github.com/yourusername/product-analysis-agent/issues) • [Documentation](https://github.com/yourusername/product-analysis-agent/wiki)

</div>
