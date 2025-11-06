#!/usr/bin/env python3
"""
API Integration Examples for Product Analysis Agent
Shows how to integrate with other systems and workflows
"""

import asyncio
import aiohttp
import json
import sys
import os
from typing import Dict, Any, List

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import ProductAnalysisAgent

class ProductAnalysisAPI:
    """
    API wrapper for Product Analysis Agent with RESTful interface
    """
    
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.agent = ProductAnalysisAgent()
    
    async def analyze_competitors_api(self, 
                                    product_category: str,
                                    competitors: List[str] = None,
                                    analysis_depth: str = "detailed") -> Dict[str, Any]:
        """
        Analyze competitors via API-like interface
        """
        return await self.agent.analyze_competitors(
            product_category, competitors, analysis_depth
        )
    
    async def generate_comparison_chart(self, analysis_result: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate comparison chart data from analysis results
        """
        feature_matrix = analysis_result.get('feature_comparison_matrix', {})
        
        chart_data = {
            "type": "feature_comparison",
            "product_category": analysis_result['product_category'],
            "competitors": list(feature_matrix.keys()),
            "features": [],
            "data": []
        }
        
        # Extract features from the first competitor
        if feature_matrix:
            first_competitor = list(feature_matrix.keys())[0]
            features = list(feature_matrix[first_competitor].keys())
            chart_data["features"] = features
            
            # Prepare data for charting
            for competitor, features_dict in feature_matrix.items():
                competitor_data = {
                    "competitor": competitor,
                    "features_present": sum(1 for present in features_dict.values() if present),
                    "total_features": len(features_dict),
                    "coverage_percentage": round(
                        sum(1 for present in features_dict.values() if present) / len(features_dict) * 100, 1
                    )
                }
                chart_data["data"].append(competitor_data)
        
        return chart_data
    
    async def export_to_markdown(self, analysis_result: Dict[str, Any]) -> str:
        """
        Export analysis results to markdown format
        """
        markdown = f"""# Competitive Analysis: {analysis_result['product_category']}

## Executive Summary

{analysis_result.get('market_analysis', 'No market analysis available.')}

## Competitors Analyzed

- **Total**: {analysis_result['competitors_analyzed']} competitors
- **Analysis Depth**: {analysis_result['analysis_depth']}

## Key Findings

"""
        
        # Add key findings
        for i, finding in enumerate(analysis_result.get('key_findings', [])[:10], 1):
            markdown += f"{i}. {finding}\n"
        
        markdown += "\n## Strategic Recommendations\n\n"
        
        # Add recommendations
        for i, recommendation in enumerate(analysis_result['recommendations'], 1):
            markdown += f"{i}. {recommendation}\n"
        
        # Add feature comparison table if available
        feature_matrix = analysis_result.get('feature_comparison_matrix', {})
        if feature_matrix:
            markdown += "\n## Feature Comparison\n\n"
            markdown += "| Feature | " + " | ".join(feature_matrix.keys()) + " |\n"
            markdown += "|---------|" + "|".join(["---" for _ in feature_matrix.keys()]) + "|\n"
            
            # Get all unique features
            all_features = set()
            for features in feature_matrix.values():
                all_features.update(features.keys())
            
            # Add each feature row
            for feature in sorted(all_features)[:15]:  # Limit to first 15 features for readability
                row = f"| {feature} |"
                for competitor in feature_matrix.keys():
                    has_feature = "✅" if feature_matrix[competitor].get(feature) else "❌"
                    row += f" {has_feature} |"
                markdown += row + "\n"
        
        return markdown
    
    async def send_to_slack(self, analysis_result: Dict[str, Any], webhook_url: str) -> bool:
        """
        Send analysis summary to Slack via webhook
        """
        try:
            summary = f"""🚀 *Competitive Analysis Complete!*

*Product Category*: {analysis_result['product_category']}
*Competitors Analyzed*: {analysis_result['competitors_analyzed']}
*Key Recommendations*: {len(analysis_result['recommendations'])}

*Top Recommendations*:
{chr(10).join(f"• {rec}" for rec in analysis_result['recommendations'][:3])}

*Report Generated*: {analysis_result['report_timestamp']}
"""
            
            payload = {
                "text": summary,
                "username": "Product Analysis Agent",
                "icon_emoji": ":mag:"
            }
            
            async with aiohttp.ClientSession() as session:
                async with session.post(webhook_url, json=payload) as response:
                    return response.status == 200
                    
        except Exception as e:
            print(f"❌ Slack integration error: {str(e)}")
            return False
    
    async def save_to_database(self, analysis_result: Dict[str, Any], db_config: Dict[str, str]) -> bool:
        """
        Save analysis results to database (simulated)
        """
        # This is a simulation - in production, you'd use actual database drivers
        try:
            # Simulate database save
            print(f"💾 Saving analysis to database: {analysis_result['product_category']}")
            
            # Here you would implement actual database integration
            # Example with SQLAlchemy, MongoDB, etc.
            
            return True
        except Exception as e:
            print(f"❌ Database save error: {str(e)}")
            return False

async def example_api_integration():
    """Demonstrate API integration capabilities"""
    print("🔌 API Integration Examples")
    print("=" * 50)
    
    api = ProductAnalysisAPI()
    
    # Example analysis
    print("1. Running competitor analysis...")
    analysis = await api.analyze_competitors_api(
        "note-taking apps",
        competitors=["Evernote", "Notion", "Obsidian", "OneNote"],
        analysis_depth="basic"
    )
    
    print("2. Generating comparison chart data...")
    chart_data = await api.generate_comparison_chart(analysis)
    print(f"   📊 Chart data for {len(chart_data['competitors'])} competitors")
    
    print("3. Exporting to markdown...")
    markdown_report = await api.export_to_markdown(analysis)
    print(f"   📄 Markdown report: {len(markdown_report)} characters")
    
    print("4. Simulating Slack integration...")
    # Note: Using dummy webhook URL for demonstration
    slack_sent = await api.send_to_slack(analysis, "https://hooks.slack.com/services/EXAMPLE")
    print(f"   💬 Slack message: {'Sent' if slack_sent else 'Failed'}")
    
    print("5. Simulating database save...")
    db_saved = await api.save_to_database(analysis, {"type": "simulated"})
    print(f"   💾 Database save: {'Success' if db_saved else 'Failed'}")
    
    # Save the generated reports
    os.makedirs("reports", exist_ok=True)
    
    # Save chart data as JSON
    with open("reports/chart_data.json", "w") as f:
        json.dump(chart_data, f, indent=2)
    
    # Save markdown report
    with open("reports/api_integration_report.md", "w", encoding="utf-8") as f:
        f.write(markdown_report)
    
    print(f"\n✅ API integration examples completed!")
    print(f"💾 Reports saved to 'reports/' directory")

async def example_batch_processing():
    """Example of batch processing multiple markets"""
    print("\n🔁 Batch Processing Example")
    print("=" * 40)
    
    api = ProductAnalysisAPI()
    
    markets = [
        {"category": "video conferencing", "competitors": ["Zoom", "Microsoft Teams", "Google Meet", "Slack"]},
        {"category": "password managers", "competitors": ["LastPass", "1Password", "Bitwarden", "Dashlane"]},
        {"category": "email marketing", "competitors": ["Mailchimp", "ConvertKit", "Sendinblue", "ActiveCampaign"]},
    ]
    
    results = []
    
    for market in markets:
        print(f"📊 Analyzing {market['category']}...")
        try:
            analysis = await api.analyze_competitors_api(
                market["category"],
                market["competitors"],
                analysis_depth="basic"
            )
            results.append(analysis)
            print(f"   ✅ Completed: {market['category']}")
        except Exception as e:
            print(f"   ❌ Failed: {market['category']} - {str(e)}")
    
    # Generate batch summary
    batch_summary = {
        "total_markets_analyzed": len(results),
        "total_competitors": sum(r['competitors_analyzed'] for r in results),
        "markets": [
            {
                "category": r['product_category'],
                "competitors_analyzed": r['competitors_analyzed'],
                "recommendations_count": len(r['recommendations'])
            }
            for r in results
        ]
    }
    
    # Save batch results
    with open("reports/batch_processing_results.json", "w") as f:
        json.dump(batch_summary, f, indent=2)
    
    print(f"\n🎉 Batch processing completed!")
    print(f"📈 Analyzed {len(results)} markets with {batch_summary['total_competitors']} total competitors")

async def main():
    """Run all API integration examples"""
    print("🚀 Product Analysis Agent - API Integration Examples")
    print("=" * 60)
    
    try:
        # Run API integration examples
        await example_api_integration()
        
        # Run batch processing example
        await example_batch_processing()
        
        print("\n" + "=" * 60)
        print("🎯 INTEGRATION PATTERNS DEMONSTRATED:")
        print("✅ RESTful API interface")
        print("✅ Data export (JSON, Markdown)")
        print("✅ Notification integration (Slack)")
        print("✅ Database integration")
        print("✅ Batch processing")
        print("✅ Chart data generation")
        
        print("\n🚀 NEXT STEPS FOR INTEGRATION:")
        print("1. Deploy as a microservice with proper API endpoints")
        print("2. Add authentication and rate limiting")
        print("3. Integrate with your data warehouse")
        print("4. Connect to BI tools for visualization")
        print("5. Set up automated reporting workflows")
        
    except Exception as e:
        print(f"❌ Error in API examples: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
