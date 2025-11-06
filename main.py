import os
import asyncio
import aiohttp
from typing import List, Dict, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class ProductAnalysisAgent:
    """
    Specialized agent for competitive product analysis using ROMA framework.
    Implements the complete "Launch Product Analysis" workflow.
    """
    
    def __init__(self):
        self.openrouter_key = os.getenv("OPENROUTER_API_KEY")
        self.exa_key = os.getenv("EXA_API_KEY")
        self.model = os.getenv("OPENROUTER_MODEL", "openrouter/z-ai/glm-4.5-air:free")
        
    async def analyze_competitors(self, product_category: str, competitors: List[str] = None) -> Dict[str, Any]:
        """
        Complete competitive analysis workflow:
        1. Search competitor products
        2. Analyze websites and features
        3. Create comparison framework
        4. Generate comprehensive report
        """
        print(f"🚀 Starting competitive analysis for: {product_category}")
        
        # Step 1: Search for competitors
        competitor_data = await self._search_competitors(product_category, competitors)
        
        # Step 2: Analyze each competitor
        analysis_results = []
        for competitor in competitor_data:
            analysis = await self._analyze_competitor(competitor)
            analysis_results.append(analysis)
        
        # Step 3: Generate comparison report
        final_report = await self._generate_comparison_report(product_category, analysis_results)
        
        return final_report
    
    async def _search_competitors(self, category: str, competitors: List[str] = None) -> List[Dict]:
        """Executor: Search for competitor products using Exa"""
        print(f"🔍 Searching competitors for: {category}")
        
        # Use Exa search to find relevant products
        search_results = await self._exa_search(f"{category} competitors alternatives")
        
        competitor_list = []
        for result in search_results[:5]:  # Top 5 results
            competitor_list.append({
                "name": result.get("title", ""),
                "url": result.get("url", ""),
                "description": result.get("description", ""),
                "category": category
            })
        
        return competitor_list
    
    async def _analyze_competitor(self, competitor: Dict) -> Dict:
        """Executor: Analyze competitor website and features"""
        print(f"📊 Analyzing: {competitor['name']}")
        
        # Analyze website content
        website_analysis = await self._analyze_website(competitor["url"])
        
        # Extract key features
        features = await self._extract_features(website_analysis, competitor["name"])
        
        return {
            "competitor": competitor["name"],
            "url": competitor["url"],
            "website_analysis": website_analysis,
            "key_features": features,
            "pricing": await self._extract_pricing(website_analysis),
            "target_audience": await self._identify_audience(website_analysis)
        }
    
    async def _generate_comparison_report(self, category: str, analyses: List[Dict]) -> Dict[str, Any]:
        """Aggregator: Synthesize findings into comprehensive report"""
        print("📈 Generating comparison report...")
        
        # Use OpenRouter to generate structured analysis
        prompt = self._create_analysis_prompt(category, analyses)
        report = await self._get_llm_analysis(prompt)
        
        return {
            "product_category": category,
            "competitors_analyzed": len(analyses),
            "comparison_matrix": self._create_feature_matrix(analyses),
            "market_analysis": report,
            "recommendations": await self._generate_recommendations(analyses),
            "timestamp": asyncio.get_event_loop().time()
        }
    
    async def _exa_search(self, query: str) -> List[Dict]:
        """Tool: Search web using Exa API"""
        url = "https://api.exa.ai/search"
        headers = {
            "Authorization": f"Bearer {self.exa_key}",
            "Content-Type": "application/json"
        }
        data = {
            "query": query,
            "type": "neural",
            "numResults": 10
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=data) as response:
                if response.status == 200:
                    result = await response.json()
                    return result.get("results", [])
                else:
                    print(f"❌ Exa search failed: {response.status}")
                    return []
    
    async def _analyze_website(self, url: str) -> str:
        """Tool: Analyze website content"""
        # Simplified website analysis
        # In production, this would use proper web scraping
        analysis_prompt = f"Analyze the website {url} and describe its main offerings, target audience, and key features."
        return await self._get_llm_analysis(analysis_prompt)
    
    async def _get_llm_analysis(self, prompt: str) -> str:
        """Tool: Get analysis from OpenRouter"""
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.openrouter_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 4000
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=data) as response:
                if response.status == 200:
                    result = await response.json()
                    return result["choices"][0]["message"]["content"]
                else:
                    return f"Analysis unavailable: {response.status}"
    
    def _create_analysis_prompt(self, category: str, analyses: List[Dict]) -> str:
        """Create detailed analysis prompt for LLM"""
        competitors_info = "\n\n".join([
            f"## {analysis['competitor']}\n"
            f"URL: {analysis['url']}\n"
            f"Features: {', '.join(analysis['key_features'])}\n"
            f"Analysis: {analysis['website_analysis'][:500]}..."
            for analysis in analyses
        ])
        
        return f"""
        Perform a comprehensive competitive analysis for {category}.
        
        Competitors analyzed:
        {competitors_info}
        
        Please provide:
        1. Market overview and trends
        2. Feature comparison matrix
        3. Strengths and weaknesses of each competitor
        4. Gap analysis and opportunities
        5. Strategic recommendations
        
        Format the response in clear markdown with sections.
        """
    
    def _create_feature_matrix(self, analyses: List[Dict]) -> Dict:
        """Create feature comparison matrix"""
        all_features = set()
        for analysis in analyses:
            all_features.update(analysis["key_features"])
        
        matrix = {}
        for analysis in analyses:
            matrix[analysis["competitor"]] = {
                feature: feature in analysis["key_features"]
                for feature in all_features
            }
        
        return matrix
    
    async def _extract_features(self, analysis: str, competitor: str) -> List[str]:
        """Extract key features from website analysis"""
        prompt = f"""
        Based on this analysis of {competitor}, extract the key features and capabilities:
        
        {analysis[:1000]}
        
        Return only a comma-separated list of features, no explanations.
        """
        features_text = await self._get_llm_analysis(prompt)
        return [f.strip() for f in features_text.split(",") if f.strip()]
    
    async def _extract_pricing(self, analysis: str) -> str:
        """Extract pricing information"""
        prompt = f"Extract pricing information from: {analysis[:800]}"
        return await self._get_llm_analysis(prompt)
    
    async def _identify_audience(self, analysis: str) -> str:
        """Identify target audience"""
        prompt = f"Identify the target audience from: {analysis[:800]}"
        return await self._get_llm_analysis(prompt)
    
    async def _generate_recommendations(self, analyses: List[Dict]) -> List[str]:
        """Generate strategic recommendations"""
        analysis_summary = "\n".join([
            f"- {a['competitor']}: {a['website_analysis'][:200]}..."
            for a in analyses
        ])
        
        prompt = f"""
        Based on this competitive analysis, provide 5 strategic recommendations:
        
        {analysis_summary}
        
        Return as a numbered list of recommendations.
        """
        recommendations = await self._get_llm_analysis(prompt)
        return [rec.strip() for rec in recommendations.split("\n") if rec.strip() and rec[0].isdigit()]

# Example usage
async def main():
    """Example of using the Product Analysis Agent"""
    agent = ProductAnalysisAgent()
    
    # Analyze AI coding assistants market
    result = await agent.analyze_competitors(
        "AI coding assistants",
        competitors=["GitHub Copilot", "Amazon CodeWhisperer", "Tabnine"]
    )
    
    print("\n" + "="*50)
    print("📊 COMPETITIVE ANALYSIS REPORT")
    print("="*50)
    print(f"Category: {result['product_category']}")
    print(f"Competitors Analyzed: {result['competitors_analyzed']}")
    print(f"\nMarket Analysis:\n{result['market_analysis'][:500]}...")
    print(f"\nRecommendations: {len(result['recommendations'])}")
    
    # Save full report
    with open("competitive_analysis_report.md", "w") as f:
        f.write(f"# Competitive Analysis: {result['product_category']}\n\n")
        f.write(result['market_analysis'])

if __name__ == "__main__":
    asyncio.run(main())
