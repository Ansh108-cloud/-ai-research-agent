"""
AI Research Agent Backend - Built with FastAPI and Groq API
Zero cost, open-source setup
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import json
from datetime import datetime
import requests
from duckduckgo_search import DDGS
from typing import Optional
from pathlib import Path

# Load environment variables
load_dotenv()

app = FastAPI(title="AI Research Agent", version="1.0")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Groq client
try:
    from groq import Groq
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    print("✅ Groq API initialized")
except Exception as e:
    print(f"⚠️ Groq not available: {e}")
    client = None


# ==================== DATA MODELS ====================

class ResearchRequest(BaseModel):
    query: str
    max_searches: int = 5
    depth: str = "standard"  # "quick", "standard", "deep"


class ResearchResponse(BaseModel):
    query: str
    report: str
    sources: list
    search_history: list
    timestamp: str
    reasoning_steps: list


# ==================== WEB SEARCH FUNCTION ====================

def search_web(query: str, max_results: int = 5) -> list:
    """
    Search the web using DuckDuckGo (free, no API key needed)
    """
    try:
        ddgs = DDGS()
        results = ddgs.text(query, max_results=max_results)
        
        formatted_results = []
        for result in results:
            formatted_results.append({
                "title": result.get("title", ""),
                "link": result.get("href", ""),
                "snippet": result.get("body", ""),
                "source": "DuckDuckGo"
            })
        
        return formatted_results
    except Exception as e:
        print(f"Search error: {e}")
        return []


# ==================== AI AGENT LOGIC ====================

class ResearchAgent:
    def __init__(self, llm_client, max_iterations: int = 5):
        self.client = llm_client
        self.max_iterations = max_iterations
        self.conversation_history = []
        self.research_findings = []
        self.search_count = 0
        
    def think_and_plan(self, query: str) -> dict:
        """
        Step 1: AI analyzes query and creates research plan
        """
        prompt = f"""You are an expert research analyst. Analyze this query and create a research plan.

Query: {query}

Respond in JSON format:
{{
    "research_questions": ["question 1", "question 2", "question 3"],
    "search_queries": ["search 1", "search 2", "search 3"],
    "expected_depth": "how deep should this research be?",
    "key_areas_to_cover": ["area 1", "area 2"]
}}"""

        # ✅ FIXED: Using correct Groq/OpenAI syntax
        response = self.client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=1000
        )
        
        try:
            # ✅ FIXED: Correct response parsing
            plan = json.loads(response.choices[0].message.content)
            return plan
        except:
            return {
                "research_questions": [query],
                "search_queries": [query],
                "expected_depth": "standard",
                "key_areas_to_cover": ["general"]
            }
    
    def execute_search(self, search_queries: list) -> dict:
        """
        Step 2: Execute web searches based on research plan
        """
        all_results = {}
        
        for search_query in search_queries[:3]:  # Limit to 3 searches
            print(f"🔍 Searching: {search_query}")
            results = search_web(search_query, max_results=5)
            all_results[search_query] = results
            self.search_count += 1
        
        return all_results
    
    def analyze_findings(self, findings: dict, original_query: str) -> dict:
        """
        Step 3: AI analyzes search results and identifies gaps
        """
        findings_text = json.dumps(findings, indent=2)
        
        prompt = f"""Based on these research findings, analyze the information and identify what else needs to be researched.

Original Query: {original_query}

Findings:
{findings_text}

Provide analysis in JSON:
{{
    "key_insights": ["insight 1", "insight 2"],
    "information_gaps": ["gap 1", "gap 2"],
    "needs_further_research": true,
    "confidence_level": 0.0,
    "suggested_followup_searches": ["search 1", "search 2"]
}}"""

        # ✅ FIXED: Using correct Groq/OpenAI syntax
        response = self.client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=1000
        )
        
        try:
            # ✅ FIXED: Correct response parsing
            analysis = json.loads(response.choices[0].message.content)
            return analysis
        except:
            return {
                "key_insights": ["Information gathered"],
                "information_gaps": [],
                "needs_further_research": False,
                "confidence_level": 0.7,
                "suggested_followup_searches": []
            }
    
    def generate_report(self, query: str, all_findings: dict, analyses: list) -> str:
        """
        Step 4: Generate comprehensive final report
        """
        context = f"""
Query: {query}

Research Findings:
{json.dumps(all_findings, indent=2)}

Analyses:
{json.dumps(analyses, indent=2)}
"""
        
        prompt = f"""Based on the research findings and analysis below, generate a comprehensive, well-structured report.

{context}

Create a professional report with:
1. Executive Summary
2. Key Findings
3. Detailed Analysis
4. Conclusions
5. Sources Cited

Format it nicely with markdown."""

        # ✅ FIXED: Using correct Groq/OpenAI syntax
        response = self.client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=2000
        )
        
        # ✅ FIXED: Correct response parsing
        return response.choices[0].message.content
    
    def research(self, query: str, max_searches: int = 5) -> dict:
        """
        Main research loop - orchestrates the entire process
        """
        reasoning_steps = []
        
        # Step 1: Create research plan
        print("📋 Creating research plan...")
        plan = self.think_and_plan(query)
        reasoning_steps.append({
            "step": "Plan",
            "action": "AI created research plan",
            "plan": plan
        })
        
        # Step 2: Execute searches
        print("🔍 Executing searches...")
        findings = self.execute_search(plan.get("search_queries", [query]))
        reasoning_steps.append({
            "step": "Search",
            "action": f"Executed {self.search_count} searches",
            "results_count": len(findings)
        })
        
        # Step 3: Analyze findings and check for gaps
        print("🧠 Analyzing findings...")
        analyses = []
        all_findings = findings.copy()
        
        for iteration in range(self.max_iterations):
            analysis = self.analyze_findings(all_findings, query)
            analyses.append(analysis)
            
            reasoning_steps.append({
                "step": f"Analysis {iteration + 1}",
                "confidence": analysis.get("confidence_level", 0),
                "gaps": analysis.get("information_gaps", [])
            })
            
            # If no more research needed or max iterations reached, break
            if not analysis.get("needs_further_research", False) or iteration >= 2:
                break
            
            # Do followup searches if suggested
            followup_queries = analysis.get("suggested_followup_searches", [])
            if followup_queries:
                print(f"🔄 Doing followup searches...")
                followup_findings = self.execute_search(followup_queries)
                all_findings.update(followup_findings)
        
        # Step 4: Generate final report
        print("📝 Generating report...")
        report = self.generate_report(query, all_findings, analyses)
        
        reasoning_steps.append({
            "step": "Report Generation",
            "action": "Final report generated",
            "word_count": len(report.split())
        })
        
        # Flatten sources
        sources = []
        for search_query, results in all_findings.items():
            sources.extend(results)
        
        return {
            "query": query,
            "report": report,
            "sources": sources,
            "search_history": list(all_findings.keys()),
            "timestamp": datetime.now().isoformat(),
            "reasoning_steps": reasoning_steps
        }


# ==================== API ROUTES ====================

@app.get("/")
async def root():
    """Serve the HTML frontend"""
    index_path = Path(__file__).parent / "index.html"
    
    # If index.html exists, serve it
    if index_path.exists():
        return FileResponse(str(index_path), media_type="text/html")
    
    # Fallback: return status
    return {
        "status": "running",
        "service": "AI Research Agent",
        "version": "1.0",
        "llm_available": client is not None
    }

@app.get("/api/status")
async def status():
    """API status endpoint"""
    return {
        "status": "running",
        "service": "AI Research Agent",
        "version": "1.0",
        "llm_available": client is not None
    }


@app.post("/research", response_model=ResearchResponse)
async def research(request: ResearchRequest):
    """
    Main research endpoint
    """
    
    if not client:
        raise HTTPException(
            status_code=503,
            detail="LLM service not available. Please set GROQ_API_KEY environment variable."
        )
    
    if not request.query or len(request.query) < 3:
        raise HTTPException(status_code=400, detail="Query must be at least 3 characters")
    
    try:
        # Initialize research agent
        agent = ResearchAgent(client, max_iterations=3)
        
        # Run research
        result = agent.research(request.query, max_searches=request.max_searches)
        
        return ResearchResponse(**result)
    
    except Exception as e:
        print(f"Error during research: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/quick-search")
async def quick_search(query: str):
    """Quick search endpoint (no AI processing, just raw search results)"""
    if not query:
        raise HTTPException(status_code=400, detail="Query parameter required")
    
    results = search_web(query, max_results=10)
    
    return {
        "query": query,
        "results": results,
        "count": len(results)
    }


# ==================== RUN SERVER ====================

if __name__ == "__main__":
    import uvicorn
    
    # Check for API key
    if not os.getenv("GROQ_API_KEY"):
        print("⚠️  WARNING: GROQ_API_KEY not set!")
        print("1. Get free key from: https://console.groq.com/keys")
        print("2. Create .env file with: GROQ_API_KEY=your_key_here")
    
    print("🚀 Starting AI Research Agent...")
    print("📍 Local: http://localhost:8000")
    print("📚 Docs: http://localhost:8000/docs")
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000)),  # ✅ FIXED: Render port
        reload=False  # ✅ FIXED: False for production
    )
