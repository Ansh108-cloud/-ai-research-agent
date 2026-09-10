# 🚀 QUICKSTART - Build Your AI Research Agent in 10 Minutes

## ⚡ What You're Building

A **free, open-source AI research tool** that works like Perplexity's Deep Research:
- ✅ Conducts multi-step research
- ✅ Performs autonomous web searches
- ✅ Generates comprehensive reports
- ✅ Cites all sources
- ✅ Completely FREE to run

---

## 📋 Prerequisites

- **Python 3.8+** installed ([Download](https://python.org))
- **A free Groq API key** ([Get it here in 1 minute](https://console.groq.com/keys))
- A code editor (VS Code recommended)

---

## 🎯 Step-by-Step Setup

### Step 1️⃣: Create Project Folder

```bash
# Create a new folder
mkdir my-research-agent
cd my-research-agent

# Copy these files to the folder:
# - app.py
# - index.html
# - requirements.txt
# - .env.example
```

### Step 2️⃣: Get Your Free LLM API Key

**Go to:** https://console.groq.com/keys

1. Click "Sign up" (takes 30 seconds)
2. Create an account
3. Go to "API Keys" section
4. Copy your API key

### Step 3️⃣: Set Up Environment

```bash
# Create a copy of .env file
cp .env.example .env

# Open .env in your editor and add your Groq key:
# GROQ_API_KEY=your_actual_key_here
```

### Step 4️⃣: Install Dependencies

```bash
# Create Python virtual environment
python -m venv venv

# Activate it:
# On Mac/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate

# Install packages
pip install -r requirements.txt
```

### Step 5️⃣: Run the Server

```bash
python app.py
```

You should see:
```
✅ Groq API initialized
🚀 Starting AI Research Agent...
📍 Local: http://localhost:8000
📚 Docs: http://localhost:8000/docs
```

### Step 6️⃣: Open in Browser

1. Open your browser
2. Go to: **http://localhost:8000**
3. You should see the beautiful UI!

### Step 7️⃣: Test It Out

Try asking:
- "What are the latest developments in AI in 2026?"
- "How does quantum computing work?"
- "Compare Python vs JavaScript for web development"

**Watch it research for 2-5 minutes** and then show you a comprehensive report!

---

## 🎮 How to Use

### Using the Web Interface

1. **Enter your query** in the search box
2. **Choose research depth:**
   - Quick: 2-3 searches (30 seconds)
   - Standard: 5-7 searches (2 minutes)
   - Deep: 10+ searches (5 minutes)
3. **Click "Start Research"**
4. Wait for it to complete
5. **View results in tabs:**
   - 📝 Report (formatted answer)
   - 🔗 Sources (all references)
   - 🧠 Reasoning (how it researched)

### Using the API Directly

```bash
# Test the API with curl
curl -X POST "http://localhost:8000/research" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What is blockchain?",
    "max_searches": 5,
    "depth": "standard"
  }'
```

---

## 🔧 Customization Ideas

### Idea 1: Add More Search Sources
Replace DuckDuckGo with:
- Google Custom Search (100 free/day)
- SerpAPI (100 free/month)
- Bing Search API

### Idea 2: Use Different LLMs
Instead of Groq, try:
- **OpenAI** (but costs $)
- **Ollama** (run locally, free)
- **Hugging Face** (free tier)
- **Together AI** (free tier)

### Idea 3: Add Database
Store past searches:
```python
# Add SQLite to save research history
import sqlite3
db = sqlite3.connect('research.db')
```

### Idea 4: Export Options
Add exports in different formats:
```python
# PDF export
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate
```

### Idea 5: Custom Plugins
Create specialized agents for:
- Academic research
- News analysis
- Product research
- Health information

---

## 🚀 Deployment (Still FREE!)

### Option 1: Render.com (Recommended)

1. Go to https://render.com
2. Sign up (free)
3. Click "New Web Service"
4. Connect your GitHub repo
5. Set environment variables
6. Deploy! (free tier has 750 hours/month)

### Option 2: Railway.app

1. Go to https://railway.app
2. Sign up with GitHub
3. Create new project
4. Add your repo
5. Add environment variables
6. Deploy! (free tier with credits)

### Option 3: Replit

1. Go to https://replit.com
2. Import from GitHub (your repo)
3. Add GROQ_API_KEY to secrets
4. Click Run
5. Share your link!

---

## 📊 How It Works Under the Hood

```
User Question
    ↓
[Research Planning] AI creates search strategy
    ↓
[Web Search] DuckDuckGo searches for information
    ↓
[Analysis] AI analyzes findings, identifies gaps
    ↓
[Iteration] If needed, do more searches
    ↓
[Report Generation] AI synthesizes all findings
    ↓
Beautiful Report + Sources
```

---

## 💰 Cost Analysis (Spoiler: It's FREE!)

| Component | Cost | Notes |
|-----------|------|-------|
| Groq API | **FREE** | Up to 30 requests/min |
| DuckDuckGo Search | **FREE** | Unlimited searches |
| Render/Railway | **FREE** | Free tier available |
| Python/FastAPI | **FREE** | Open source |
| Hosting | **FREE** | Free tier services |
| **TOTAL** | **$0** | Forever free! |

---

## 🐛 Troubleshooting

### "ModuleNotFoundError"
```bash
# Make sure virtual environment is activated:
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

### "GROQ_API_KEY not set"
```bash
# Check your .env file
cat .env  # Mac/Linux
type .env  # Windows

# Make sure it has your actual API key!
```

### "Connection refused on localhost:8000"
```bash
# Make sure the server is running
python app.py

# Try in a new terminal while keeping server running
```

### "Search returns no results"
This is normal - DuckDuckGo sometimes needs better queries. Try:
- More specific searches
- Different keywords
- Recent/current events may have limited results

---

## 📚 Next Steps

### Beginner Level
- [ ] Get it running locally
- [ ] Ask 5 different research queries
- [ ] Explore the source code
- [ ] Try customizing the prompt

### Intermediate Level
- [ ] Deploy to Render/Railway
- [ ] Add more search providers
- [ ] Create a custom UI
- [ ] Add database storage

### Advanced Level
- [ ] Build specialized research agents
- [ ] Add multi-user support
- [ ] Integrate with other APIs
- [ ] Create mobile app version
- [ ] Add real-time streaming responses

---

## 🎓 Learning Resources

- **FastAPI Docs:** https://fastapi.tiangolo.com
- **Groq API Docs:** https://console.groq.com/docs
- **Python Virtual Environments:** https://docs.python.org/3/tutorial/venv.html
- **Agents & LLMs:** https://www.deeplearning.ai/short-courses/

---

## 💡 Pro Tips

1. **Use DuckDuckGo bangs** for better searches:
   - `!w` for Wikipedia
   - `!gh` for GitHub
   - `!hn` for Hacker News

2. **Batch Your Requests** - The free tier is generous, but batch requests to save quota

3. **Cache Results** - Add SQLite to avoid duplicate searches

4. **Monitor Usage** - Check Groq dashboard to see API usage

5. **Rate Limiting** - Add delays between searches for stability

---

## 🆘 Need Help?

If you get stuck:

1. Check error messages carefully
2. Read through the AI_RESEARCH_AGENT_GUIDE.md
3. Test individual parts (search, LLM) separately
4. Enable debug logging in app.py
5. Ask Claude: "How do I fix [error]?"

---

## 🎉 Congratulations!

You've just built a professional-grade AI research tool from scratch, **completely free**! 

Now you can:
- Research anything in seconds
- Deploy it online
- Customize it for your needs
- Impress your friends/colleagues
- Monetize it if you want!

**Happy researching! 🚀**
