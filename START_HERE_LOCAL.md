# 🚀 Quick Start - Local Version (No API Key!)

**Perfect for your DevBar setup!**

## ⚡ 3-Minute Setup

```bash
# 1. Install dependencies (1 minute)
cd ~/youtube-notes-generator
python3 -m venv venv
source venv/bin/activate
pip install -r requirements-local.txt

# 2. Verify Claude CLI (30 seconds)
claude --version
# or
which claude

# 3. Test it! (1 minute)
python youtube_notes_local.py \
  --video "https://www.youtube.com/watch?v=kqtD5dpn9C8" \
  --repo-path ~/test-notes \
  --output-dir python-test \
  --no-commit
```

## ✨ Key Advantages

✅ **No API key needed** - Uses your DevBar setup  
✅ **Free** - Leverages your AWS Bedrock/LLM Gateway  
✅ **Simple** - Fewer dependencies, less setup  
✅ **Familiar** - Uses your existing Claude CLI  

## 📝 Basic Usage

### Process Single Video

```bash
python youtube_notes_local.py \
  --video "https://www.youtube.com/watch?v=VIDEO_ID" \
  --repo-path ~/learning-repos/my-course \
  --output-dir course-notes
```

### Process Playlist

```bash
python youtube_notes_local.py \
  --playlist "https://www.youtube.com/playlist?list=PLAYLIST_ID" \
  --videos 1,2,3 \
  --repo-path ~/learning-repos/my-course \
  --output-dir course-notes
```

## 🎯 What You Get

```
your-repo/
└── course-notes/
    ├── README.md              # Course index
    ├── 01-first-lesson/
    │   ├── README.md         # Lesson notes
    │   └── diagrams/
    │       └── *.mmd files
    └── 02-second-lesson/
        └── ...
```

Each lesson includes:
- Overview and key concepts
- Detailed notes with examples
- Visual diagrams
- Practice questions
- Key takeaways

## 🔧 Troubleshooting

### Can't find Claude CLI?

```bash
# Check location
which claude

# If not in PATH, add it
export PATH="$PATH:$HOME/.devbar/bin"

# Or test directly
~/.devbar/bin/claude --version
```

### Permission denied?

```bash
chmod +x youtube_notes_local.py
```

## 📚 Documentation

- **[SETUP_LOCAL.md](SETUP_LOCAL.md)** - Complete setup guide
- **[LOCAL_VS_API.md](LOCAL_VS_API.md)** - Compare versions
- **[USAGE_EXAMPLES.md](USAGE_EXAMPLES.md)** - Real examples

## 🚀 Next Steps

1. ✅ Run test: `./test_local.sh`
2. ✅ Process your first video
3. ✅ Build your learning library!

## 💡 Pro Tips

- Start with 1-2 videos to test
- Choose videos with good captions
- Review and customize generated notes
- Push to GitHub to track progress

---

**Ready? Start with `./test_local.sh` to verify everything works!** 🎉
