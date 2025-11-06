# 🚀 Product Analysis Agent

A specialized ROMA-based agent for comprehensive competitive product analysis. Automates market research by searching competitor products, analyzing websites, and generating detailed comparison reports.

## 🎯 Purpose
**"Launch Product Analysis" Workflow:**
1. **Executor** searches competitor products (Exa)
2. **Executor** reads and analyzes competitor websites (FileToolkit)
3. **Planner** creates structured comparison framework
4. **Aggregator** synthesizes findings
5. **Output:** Comprehensive competitive analysis report

## 🏗️ Architecture
- **ROMA Framework** with DSPy backend
- **Multi-agent orchestration** (Atomizer → Planner → Executor → Aggregator)
- **Exa.ai integration** for web search
- **OpenRouter** for free-tier LLM access

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Docker & Docker Compose
- [OpenRouter API Key](https://openrouter.ai/)
- [Exa.ai API Key](https://exa.ai/)

### Installation
```bash
# Clone and setup
git clone <your-repo>
cd product-analysis-agent

# Install dependencies
pip install -r requirements.txt

# Setup environment
cp .env.example .env
# Edit .env with your API keys

# Run the agent
python main.py
