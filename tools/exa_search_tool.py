from roma import tool
import aiohttp
import os
from typing import List, Dict, Any

@tool("search_competitors", description="Search for competitor products and alternatives using Exa")
async def search_competitors(product_category: str, max_results: int = 10) -> List[Dict[str, Any]]:
    """
    Search for competitors in a specific product category using Exa.ai
    """
    exa_key = os.getenv("EXA_API_KEY")
    
    url = "https://api.exa.ai/search"
    headers = {
        "Authorization": f"Bearer {exa_key}",
        "Content-Type": "application/json"
    }
    
    # Construct search query for competitors
    query = f"{product_category} competitors alternatives comparison review"
    
    data = {
        "query": query,
        "type": "neural",
        "numResults": max_results,
        "includeDomains": [],
        "excludeDomains": ["wikipedia.org", "reddit.com"]
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=data) as response:
            if response.status == 200:
                result = await response.json()
                competitors = []
                
                for item in result.get("results", []):
                    competitors.append({
                        "name": item.get("title", ""),
                        "url": item.get("url", ""),
                        "description": item.get("description", ""),
                        "content": item.get("content", "")[:500] + "..." if item.get("content") else "",
                        "published_date": item.get("publishedDate", ""),
                        "author": item.get("author", "")
                    })
                
                return competitors
            else:
                error_text = await response.text()
                return [{"error": f"Exa search failed: {response.status}", "details": error_text}]
