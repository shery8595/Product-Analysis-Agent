from roma import tool
import aiohttp
from bs4 import BeautifulSoup
from typing import Dict, Any

@tool("analyze_website", description="Analyze competitor website structure and content")
async def analyze_website(url: str) -> Dict[str, Any]:
    """
    Analyze a competitor website to extract key information about their product
    """
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=30) as response:
                if response.status == 200:
                    html_content = await response.text()
                    soup = BeautifulSoup(html_content, 'html.parser')
                    
                    # Extract key information
                    title = soup.find('title')
                    h1_tags = soup.find_all('h1')
                    h2_tags = soup.find_all('h2')
                    
                    # Extract meta description
                    meta_desc = soup.find('meta', attrs={'name': 'description'})
                    description = meta_desc['content'] if meta_desc else ""
                    
                    # Extract key sections (simplified)
                    key_sections = []
                    for section in h2_tags[:10]:  # First 10 h2 sections
                        key_sections.append(section.get_text().strip())
                    
                    # Look for pricing indicators
                    pricing_indicators = ["$", "price", "pricing", "plan", "subscription"]
                    pricing_elements = []
                    
                    for text in [tag.get_text() for tag in soup.find_all(['p', 'div', 'span'])]:
                        if any(indicator in text.lower() for indicator in pricing_indicators):
                            pricing_elements.append(text.strip()[:200])
                    
                    return {
                        "url": url,
                        "title": title.get_text().strip() if title else "No title",
                        "description": description,
                        "main_headings": [h1.get_text().strip() for h1 in h1_tags],
                        "key_sections": key_sections,
                        "pricing_mentions": pricing_elements[:5],  # Top 5 pricing mentions
                        "word_count": len(soup.get_text().split()),
                        "analysis_status": "success"
                    }
                else:
                    return {
                        "url": url,
                        "error": f"HTTP {response.status}",
                        "analysis_status": "failed"
                    }
    except Exception as e:
        return {
            "url": url,
            "error": str(e),
            "analysis_status": "failed"
        }
