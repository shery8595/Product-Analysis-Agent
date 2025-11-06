#!/usr/bin/env python3
"""
Basic usage examples for the Product Analysis Agent
"""

import asyncio
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import ProductAnalysisAgent

async def example_ai_coding_assistants():
    """Example: Analyze AI coding assistants market"""
    print("🔍 Analyzing AI Coding Assistants Market...")
    
    agent = ProductAnalysisAgent()
    
    result = await agent.analyze_competitors(
        "AI coding assistants",
        competitors=["GitHub Copilot", "Amazon CodeWhisperer", "Tabnine", "Cursor", "Codeium"]
    )
    
    print(f"✅ Analysis complete! Analyzed {result['competitors_analyzed']} competitors")
    print(f"📊 Feature matrix covers {len(result['comparison_matrix'])} competitors")
    print(f"💡 Generated {len(result['recommendations'])} strategic recommendations")
    
    # Save detailed report
    with open("ai_coding_assistants_analysis.md", "w") as f:
        f.write(f"# AI Coding Assistants Competitive Analysis\n\n")
        f.write(result['market_analysis'])
    
    print("📄 Full report saved to: ai_coding_assistants_analysis.md")

async def example_project_management_tools():
    """Example: Analyze project management tools"""
    print("🔍 Analyzing Project Management Tools Market...")
    
    agent = ProductAnalysisAgent()
    
    result = await agent.analyze_competitors(
        "project management software",
        competitors=["Jira", "Asana", "Trello", "Monday.com", "ClickUp"]
    )
    
    print(f"✅ Analysis complete! Check project_management_analysis.md")
    
    with open("project_management_analysis.md", "w") as f:
        f.write(f"# Project Management Software Competitive Analysis\n\n")
        f.write(result['market_analysis'])

async def main():
    """Run all examples"""
    print("🚀 Product Analysis Agent - Examples")
    print("=" * 50)
    
    await example_ai_coding_assistants()
    print("\n" + "-" * 50 + "\n")
    await example_project_management_tools()
    
    print("\n🎉 All examples completed!")

if __name__ == "__main__":
    asyncio.run(main())
