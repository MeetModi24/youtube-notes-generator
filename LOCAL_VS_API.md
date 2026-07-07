# Local Version vs API Version

Two versions available - choose based on your setup!

## Quick Comparison

| Feature | Local Version ✅ | API Version |
|---------|------------------|-------------|
| **API Key Required** | ❌ No | ✅ Yes |
| **Setup Complexity** | 🟢 Simple | 🟡 Moderate |
| **Dependencies** | Minimal | More packages |
| **Speed** | 🟡 Good | 🟢 Fast |
| **Cost** | 🟢 Free* | 💰 Pay per use |
| **Authentication** | Uses DevBar | API key in .env |
| **Best For** | Salesforce internal | External users |

*Uses your existing DevBar/AWS Bedrock setup

## Local Version (Recommended for You!)

### Files
- `youtube_notes_local.py` - Main script
- `requirements-local.txt` - Dependencies
- `SETUP_LOCAL.md` - Setup guide
- `test_local.sh` - Test script

### Setup

```bash
# Install
pip install -r requirements-local.txt

# Run (no API key needed!)
python youtube_notes_local.py \
  --video "VIDEO_URL" \
  --repo-path ~/my-repo \
  --output-dir course
```

### How It Works

```
Your Request
    ↓
youtube_notes_local.py
    ↓
Calls: claude ask (subprocess)
    ↓
DevBar/AWS Bedrock/LLM Gateway
    ↓
Claude AI Response
    ↓
Formatted Notes + Diagrams
```

### Pros
✅ No API key setup  
✅ Uses your existing credentials  
✅ Fewer dependencies  
✅ Same AI quality  
✅ No additional cost  

### Cons
⚠️ Slightly slower (subprocess overhead)  
⚠️ Requires Claude CLI in PATH  
⚠️ Depends on DevBar infrastructure  

## API Version

### Files
- `youtube_notes.py` - Main script
- `requirements.txt` - Dependencies
- `.env` - API key configuration

### Setup

```bash
# Install
pip install -r requirements.txt

# Configure
echo "ANTHROPIC_API_KEY=sk-ant-..." > .env

# Run
python youtube_notes.py \
  --video "VIDEO_URL" \
  --repo-path ~/my-repo \
  --output-dir course
```

### How It Works

```
Your Request
    ↓
youtube_notes.py
    ↓
Direct API call to Anthropic
    ↓
Claude AI Response
    ↓
Formatted Notes + Diagrams
```

### Pros
✅ Faster (direct API calls)  
✅ No local infrastructure needed  
✅ Works anywhere  
✅ Better error handling  

### Cons
⚠️ Requires API key  
⚠️ Costs money ($0.10-1.00 per video)  
⚠️ More dependencies  
⚠️ Need internet access  

## Which Should You Use?

### Use Local Version If:
- ✅ You have DevBar installed
- ✅ You want to use internal infrastructure
- ✅ You don't want to manage API keys
- ✅ You're okay with slightly slower processing
- ✅ You're at Salesforce (internal user)

### Use API Version If:
- ✅ You need maximum speed
- ✅ You don't have DevBar
- ✅ You're an external user
- ✅ You want predictable performance
- ✅ You're willing to pay for API calls

## Performance Comparison

| Metric | Local Version | API Version |
|--------|---------------|-------------|
| Startup time | ~2 seconds | ~1 second |
| Per video (short) | 1-2 minutes | 45-90 seconds |
| Per video (long) | 2-4 minutes | 90-180 seconds |
| Batch processing | Good | Better |
| Reliability | Depends on DevBar | High |

## Feature Parity

Both versions support:
- ✅ Single video processing
- ✅ Playlist processing
- ✅ Multiple note styles
- ✅ Diagram generation
- ✅ Git integration
- ✅ Incremental updates
- ✅ Custom branches

## Cost Comparison

### Local Version
```
Cost: $0* per video
*Uses your existing AWS Bedrock/DevBar allocation
No additional charges
```

### API Version
```
Short video (5-10 min):  $0.10-0.20
Medium video (20-30 min): $0.30-0.50
Long video (60+ min):     $0.50-1.00

100 videos/month: ~$30-50
```

## Setup Difficulty

### Local Version
```
1. Install dependencies (1 min)
2. Verify Claude CLI (30 sec)
3. Done! ✅

Total: ~2 minutes
```

### API Version
```
1. Install dependencies (1 min)
2. Get API key from Anthropic (2 min)
3. Configure .env file (30 sec)
4. Done! ✅

Total: ~4 minutes
```

## Troubleshooting Comparison

### Local Version - Common Issues

**"Claude CLI not found"**
```bash
# Solution
which claude
export PATH="$PATH:$HOME/.devbar/bin"
```

**"Timeout error"**
```bash
# Solution: Increase timeout in code
# Or process shorter videos
```

### API Version - Common Issues

**"Invalid API key"**
```bash
# Solution
cat .env  # Check key format
# Get new key from console.anthropic.com
```

**"Rate limit exceeded"**
```bash
# Solution
# Wait a few minutes
# Or upgrade API tier
```

## Migration Guide

### From API → Local

```bash
# 1. Install local dependencies
pip install -r requirements-local.txt

# 2. Remove API dependencies (optional)
pip uninstall anthropic openai tiktoken

# 3. Use local script
python youtube_notes_local.py \
  --video "URL" \
  --repo-path ~/repo \
  --output-dir course
```

### From Local → API

```bash
# 1. Install API dependencies
pip install -r requirements.txt

# 2. Get API key
# Visit console.anthropic.com

# 3. Configure
echo "ANTHROPIC_API_KEY=your_key" > .env

# 4. Use API script
python youtube_notes.py \
  --video "URL" \
  --repo-path ~/repo \
  --output-dir course
```

## Recommendations

### For Salesforce Internal Users (You!)
👉 **Use Local Version** (`youtube_notes_local.py`)
- No API key hassle
- Free (uses company resources)
- Integrates with existing tools

### For External/Personal Use
👉 **Use API Version** (`youtube_notes.py`)
- No corporate dependencies
- Predictable performance
- Works anywhere

### For Development/Testing
👉 **Use Local Version**
- Faster iteration
- No API costs during dev
- Switch to API for production if needed

## Example Workflows

### Local Version Workflow

```bash
# Daily learning routine
cd ~/youtube-notes-generator
source venv/bin/activate

# Process today's videos
python youtube_notes_local.py \
  --playlist "COURSE_PLAYLIST" \
  --videos 3,4 \
  --repo-path ~/learning/python-course \
  --output-dir fundamentals \
  --start-number 3

# Review notes
cd ~/learning/python-course/fundamentals
cat 03-*/README.md
```

### API Version Workflow

```bash
# Batch processing
cd ~/youtube-notes-generator
source venv/bin/activate

# Process entire playlist
for i in {1..10}; do
  python youtube_notes.py \
    --playlist "PLAYLIST" \
    --videos $i \
    --repo-path ~/learning/course \
    --output-dir complete \
    --start-number $i
  sleep 30
done
```

## Summary

| Your Situation | Recommended Version |
|----------------|---------------------|
| Salesforce employee with DevBar | **Local Version** ✅ |
| External developer/student | API Version |
| Want zero setup | **Local Version** ✅ |
| Need maximum speed | API Version |
| Limited budget | **Local Version** ✅ |
| Commercial use | API Version |

---

**For your setup: Use `youtube_notes_local.py` with DevBar!** 🚀

No API key, no hassle, just works with your existing infrastructure.
