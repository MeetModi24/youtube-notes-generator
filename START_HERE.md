# 🎥 YouTube Notes Generator - START HERE

Welcome! This tool transforms YouTube videos into comprehensive learning notes with diagrams.

## ⚡ Quick Navigation

**New User?** Start here:
1. [QUICKSTART.md](QUICKSTART.md) - Get running in 5 minutes
2. [SETUP.md](SETUP.md) - Detailed installation guide

**Ready to Use?** Check these:
- [USAGE_EXAMPLES.md](USAGE_EXAMPLES.md) - Real-world examples
- [FEATURES.md](FEATURES.md) - What this tool can do

**Want Overview?** Read:
- [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) - Complete overview
- [README.md](README.md) - Main documentation

## 🚀 Fastest Path to Your First Notes

```bash
# 1. Install (2 minutes)
cd ~/youtube-notes-generator
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 2. Configure (1 minute)
cp .env.example .env
# Edit .env: add your ANTHROPIC_API_KEY

# 3. Create repo (30 seconds)
mkdir -p ~/my-learning
cd ~/my-learning && git init

# 4. Process video (1 minute)
cd ~/youtube-notes-generator
python youtube_notes.py \
  --video "https://www.youtube.com/watch?v=kqtD5dpn9C8" \
  --repo-path ~/my-learning \
  --output-dir python-intro

# 5. View notes
cd ~/my-learning/python-intro
cat README.md
```

## 📚 What This Tool Does

**INPUT:** YouTube video URL or playlist  
**OUTPUT:** Structured markdown notes with diagrams

### You Get:
- ✅ Overview and key concepts
- ✅ Detailed notes organized by topics
- ✅ Visual diagrams (flowcharts, mind maps, etc.)
- ✅ Practice questions
- ✅ Key takeaways
- ✅ Git-tracked learning history

### Example Output:
```
your-repo/
└── python-basics/
    ├── README.md                    # Course index
    ├── 01-variables-and-types/
    │   ├── README.md               # Lesson notes
    │   └── diagrams/
    │       ├── 01-flowchart.mmd
    │       └── 02-mindmap.mmd
    ├── 02-control-flow/
    └── 03-functions/
```

## 🎯 Common Use Cases

### Student Taking Online Course
```bash
# Process 2 lectures per day
python youtube_notes.py \
  --playlist "COURSE_PLAYLIST" \
  --videos 1,2 \
  --repo-path ~/courses/cs101 \
  --output-dir data-structures
```

### Self-Learner Building Portfolio
```bash
# Document tutorial series
python youtube_notes.py \
  --playlist "TUTORIAL_SERIES" \
  --videos 1,2,3,4,5 \
  --repo-path ~/learning/web-dev \
  --output-dir react-fundamentals
```

### Team Creating Training Docs
```bash
# Convert training videos to docs
python youtube_notes.py \
  --video "INTERNAL_TRAINING_VIDEO" \
  --repo-path ~/team-docs/training \
  --output-dir new-hire-onboarding
```

## 🛠️ Installation Requirements

1. **Python 3.8+** - `python3 --version`
2. **Git** - `git --version`
3. **Anthropic API Key** - Get from https://console.anthropic.com/
4. *Optional:* FFmpeg - `brew install ffmpeg` (macOS)

## 📖 Documentation Guide

| Document | Best For |
|----------|----------|
| [QUICKSTART.md](QUICKSTART.md) | First-time setup (5 min) |
| [SETUP.md](SETUP.md) | Complete installation guide |
| [USAGE_EXAMPLES.md](USAGE_EXAMPLES.md) | Real-world usage patterns |
| [FEATURES.md](FEATURES.md) | Full feature list |
| [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) | Complete overview |
| [README.md](README.md) | Main documentation |

## 🆘 Quick Help

### Get Command Help
```bash
python youtube_notes.py --help
```

### Test Installation
```bash
./test_demo.sh
```

### Common Issues

**"No transcript available"**  
→ Choose videos with captions (look for [CC] icon)

**"API key not found"**  
→ Check `.env` file has `ANTHROPIC_API_KEY=your_key`

**"No module named 'anthropic'"**  
→ Activate venv: `source venv/bin/activate`

## 💡 Pro Tips

1. **Start small** - Test with 1-2 videos first
2. **Choose quality videos** - Look for good transcripts
3. **Organize by topic** - Use descriptive `--output-dir` names
4. **Review and customize** - Add your own notes and examples
5. **Push to GitHub** - Track your learning journey

## 🎨 Customization Options

### Note Styles
```bash
--style academic   # Formal, detailed
--style casual     # Conversational, easy
--style technical  # Code-focused, concise
```

### Processing Options
```bash
--video URL                    # Single video
--playlist URL --videos 1,2,3  # Multiple videos
--start-number 4               # Continue numbering
--no-commit                    # Don't commit to Git
--branch learning-notes        # Use specific branch
```

## 📊 Cost Estimate

**Anthropic API Usage:**
- Short video (5-10 min): ~$0.10-0.20
- Medium video (20-30 min): ~$0.30-0.50
- Long video (60+ min): ~$0.50-1.00

*Costs vary based on transcript length and content complexity*

## 🚀 Next Steps

### Beginner Path
1. ✅ Read [QUICKSTART.md](QUICKSTART.md)
2. ✅ Run test: `./test_demo.sh`
3. ✅ Process your first video
4. ✅ Review generated notes
5. ✅ Start your learning journey!

### Advanced Path
1. ✅ Read [FEATURES.md](FEATURES.md)
2. ✅ Check [USAGE_EXAMPLES.md](USAGE_EXAMPLES.md)
3. ✅ Set up batch processing
4. ✅ Customize note templates
5. ✅ Integrate with your workflow

## 📝 Example Commands

### Single Video
```bash
python youtube_notes.py \
  --video "https://www.youtube.com/watch?v=VIDEO_ID" \
  --repo-path ~/learning/my-course \
  --output-dir lesson-notes
```

### Playlist (First 3 Videos)
```bash
python youtube_notes.py \
  --playlist "https://www.youtube.com/playlist?list=PLAYLIST_ID" \
  --videos 1,2,3 \
  --repo-path ~/learning/full-course \
  --output-dir course-notes
```

### Add More Videos Later
```bash
python youtube_notes.py \
  --playlist "https://www.youtube.com/playlist?list=PLAYLIST_ID" \
  --videos 4,5 \
  --repo-path ~/learning/full-course \
  --output-dir course-notes \
  --start-number 4
```

## 🎓 Learning Resources

### Understand the Output
- **README.md** in each lesson folder = Your notes
- **diagrams/*.mmd** = Mermaid diagram files
- View on GitHub for automatic rendering

### Mermaid Diagram Viewing
- **GitHub**: Auto-renders (just push and view)
- **VS Code**: Install "Markdown Preview Mermaid Support"
- **Online**: https://mermaid.live
- **Apps**: Obsidian, Typora, etc.

## 🌟 Success Tips

1. **Consistency** - Process videos regularly
2. **Review** - Don't just generate, actually read the notes
3. **Practice** - Do the practice questions
4. **Customize** - Add your own examples and insights
5. **Share** - Push to GitHub to track progress

## 🔗 Quick Links

- Get Anthropic API Key: https://console.anthropic.com/
- Mermaid Diagram Editor: https://mermaid.live
- Example Playlists: Search YouTube for "Python course", "Web dev tutorial", etc.

## 📞 Support

- **Command help**: `python youtube_notes.py --help`
- **Test script**: `./test_demo.sh`
- **Documentation**: Check all `.md` files
- **Issues**: File on GitHub

## ✨ Ready to Start?

Pick your path:

- 🏃 **Quick Start**: [QUICKSTART.md](QUICKSTART.md) → Process first video in 5 minutes
- 📚 **Deep Dive**: [SETUP.md](SETUP.md) → Complete installation and configuration
- 💡 **Learn More**: [FEATURES.md](FEATURES.md) → Discover all capabilities

**Happy Learning! 🚀📚**

Transform your YouTube watching into structured knowledge!

---

*Built with ❤️ for lifelong learners*
