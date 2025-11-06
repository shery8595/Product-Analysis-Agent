from roma import tool
from PyPDF2 import PdfReader
import aiofiles
import os
from typing import Dict, Any

@tool("analyze_product_pdf", description="Analyze product PDFs for specifications and features")
async def analyze_product_pdf(file_path: str) -> Dict[str, Any]:
    """
    Analyze product PDF documents to extract specifications and features
    """
    try:
        if not os.path.exists(file_path):
            return {"error": f"PDF file not found: {file_path}"}
        
        async with aiofiles.open(file_path, 'rb') as file:
            pdf_content = await file.read()
        
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        
        # Extract key information (simplified)
        lines = text.split('\n')
        specifications = []
        features = []
        
        # Look for specification patterns
        spec_keywords = ["specification", "technical", "requirement", "capacity", "performance"]
        feature_keywords = ["feature", "benefit", "advantage", "capability", "function"]
        
        for line in lines:
            line_lower = line.lower()
            if any(keyword in line_lower for keyword in spec_keywords):
                specifications.append(line.strip())
            if any(keyword in line_lower for keyword in feature_keywords):
                features.append(line.strip())
        
        return {
            "file_name": os.path.basename(file_path),
            "total_pages": len(reader.pages),
            "total_text_length": len(text),
            "specifications_found": specifications[:10],  # Top 10
            "features_found": features[:10],  # Top 10
            "sample_content": text[:1000] + "..." if len(text) > 1000 else text,
            "analysis_status": "success"
        }
    
    except Exception as e:
        return {
            "error": str(e),
            "analysis_status": "failed"
        }
