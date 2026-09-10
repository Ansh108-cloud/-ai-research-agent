# 🌍 FREE Deployment Guide

Deploy your AI Research Agent online **completely free** to the world!

---

## Option 1: Render.com (Recommended - Easiest)

### Step 1: Push to GitHub
```bash
# Create a GitHub repo
git init
git add .
git commit -m "Initial commit"
git push origin main
```

### Step 2: Create render.yaml
Create a `render.yaml` file in your root:

```yaml
services:
  - type: web
    name: ai-research-agent
    runtime: python310
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn app:app --host 0.0.0.0 --port $PORT
    envVars:
      - key: GROQ_API_KEY
        sync: false
    routes:
      - path: /
        matchType: prefix
```

### Step 3: Deploy on Render
1. Go to https://render.com
2. Sign up with GitHub
3. Click "New Web Service"
4. Connect your GitHub repo
5. Select your repository
6. Fill in:
   - **Name:** ai-research-agent
   - **Runtime:** Python 3.10
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `uvicorn app:app --host 0.0.0.0 --port $PORT`
7. Add Environment Variables:
   - **Key:** GROQ_API_KEY
   - **Value:** [Your Groq API Key]
8. Click "Deploy"
9. Wait ~5 minutes
10. Your app is live!

### Cost
- **Free tier:** 750 hours/month (enough for most use)
- **No credit card required** (but limits apply)

---

## Option 2: Railway.app

### Step 1: Connect GitHub
1. Go to https://railway.app
2. Sign up with GitHub
3. Click "New Project"
4. Select "Deploy from GitHub repo"
5. Choose your repository

### Step 2: Add Environment Variables
```
Variables → Add Variable
GROQ_API_KEY = [Your Groq API Key]
```

### Step 3: Configure Build
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `uvicorn app:app --host 0.0.0.0 --port $PORT`

### Step 4: Deploy
Click "Deploy" and wait!

### Cost
- **Free tier:** $5 credit/month
- **No charges** if you stay within credit
- Generous for small projects

---

## Option 3: Replit (Simplest)

### Step 1: Create Replit Project
1. Go to https://replit.com
2. Click "Create Replit"
3. Select "Import from GitHub"
4. Paste your repo URL

### Step 2: Add Secrets
1. Click "Secrets" (lock icon)
2. Add: `GROQ_API_KEY = [Your Groq API Key]`

### Step 3: Run
1. Click "Run"
2. Your app starts instantly!
3. Share the link with anyone

### Cost
- **Free tier:** Unlimited (with some limits)
- **Best for:** Quick testing
- **Downside:** Auto-sleeps after inactivity

---

## Option 4: Vercel + Backend Separation

### Frontend on Vercel
1. Create a new Next.js app
2. Deploy on Vercel (free)
3. Point to your backend API

### Backend on Render
1. Deploy FastAPI on Render
2. Frontend calls the backend

### This gives you:
- Fast frontend delivery
- Reliable backend
- 100% free!

---

## Option 5: Docker + Self-Hosted

### Create Dockerfile
```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Deploy with:
- **Digital Ocean** ($5/month)
- **Linode** (free $100 credit)
- **Vultr** (free $2.50/month trial)
- **AWS** (free tier)

---

## 🔄 Update Your Frontend for Online Deployment

Update `index.html` to work with deployed backend:

```javascript
// Change this:
// const API_BASE = 'http://localhost:8000';

// To this:
const API_BASE = process.env.REACT_APP_API_URL || 'http://localhost:8000';

// Or hardcode your deployed URL:
// const API_BASE = 'https://your-app.onrender.com';
```

---

## ✅ Post-Deployment Checklist

- [ ] App is accessible from public URL
- [ ] API is responding to requests
- [ ] Web searches are working
- [ ] Groq API connection is active
- [ ] Environment variables are set
- [ ] No errors in deployment logs
- [ ] Create documentation
- [ ] Share with others!

---

## 🚨 Common Deployment Issues

### "503 Service Unavailable"
- Wait longer (first deploy can take 5-10 mins)
- Check deployment logs
- Verify environment variables

### "GROQ_API_KEY not found"
- Go to your platform settings
- Add GROQ_API_KEY to environment variables
- Redeploy the app

### "Cannot connect to database"
- If using SQLite, ensure database is in the app directory
- For PostgreSQL, use managed database service
- Check connection string

### "Port already in use"
- Use environment variable: `$PORT` (done in code)
- Don't hardcode port 8000

### "Timeout errors"
- Increase timeout settings
- For Render: go to Settings → Health Check
- For Railway: increase timeout in config

---

## 🎯 Custom Domain (Optional)

### Add your own domain:

**Render.com:**
1. Settings → Custom Domain
2. Add your domain
3. Point DNS to Render

**Railway.app:**
1. Environment Settings
2. Add custom domain
3. Configure DNS

**Vercel:**
1. Settings → Domains
2. Add your domain
3. Follow DNS instructions

---

## 🔒 Security Tips

1. **Never commit .env file**
   ```bash
   echo ".env" >> .gitignore
   git add .gitignore
   ```

2. **Use environment variables** for all secrets
3. **Enable HTTPS** (all platforms do this automatically)
4. **Add rate limiting** to your API
5. **Log important events** for debugging

---

## 📊 Monitor Your App

### Render.com
- Dashboard → Logs
- View real-time logs
- Check resource usage

### Railway.app
- Logs tab
- Monitor metrics
- View error rates

### Replit
- Console output
- Execution logs
- Error tracking

---

## 💡 Performance Tips

1. **Add caching**
   ```python
   from functools import lru_cache
   
   @lru_cache(maxsize=100)
   def search_web(query):
       # Cache search results
   ```

2. **Compress responses**
   ```python
   from fastapi.middleware.gzip import GZIPMiddleware
   app.add_middleware(GZIPMiddleware, minimum_size=1000)
   ```

3. **Add async/await**
   ```python
   async def research(request):
       # Faster operations
   ```

4. **Optimize database queries** (if using DB)

---

## 🆘 Get Help

- **Render Support:** https://render.com/docs
- **Railway Docs:** https://docs.railway.app
- **Replit Help:** https://replit.com/bugs
- **FastAPI Docs:** https://fastapi.tiangolo.com

---

## 🎉 You Did It!

Your AI Research Agent is now **live on the internet**! 🚀

Share it with:
- Friends and family
- Social media
- Your portfolio
- GitHub showcase

**Congratulations on building something awesome!** 🎊
