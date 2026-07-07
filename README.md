# 🎥 YouTube Notes Generator

Transform YouTube videos into comprehensive, student-friendly learning notes with diagrams - automatically!

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## ✨ Features

- 🤖 **AI-Powered Analysis** - Uses Claude AI to understand and structure content
- 📊 **Auto-Diagram Generation** - Creates flowcharts, mind maps, sequence diagrams
- 📁 **Smart Organization** - Clean folder structure with numbered lessons  
- 🔄 **Git Integration** - Automatic commits with descriptive messages
- 📝 **Multiple Styles** - Academic, casual, or technical writing styles
- 🎯 **Playlist Support** - Process entire playlists or specific videos
- ➕ **Incremental Updates** - Add new videos to existing course notes

## 🚀 Two Versions Available

### Local Version (DevBar/AWS Bedrock) - Recommended for Internal Use
✅ No API key required  
✅ Uses your existing infrastructure  
✅ Free (uses company resources)  

### API Version - For External Users
✅ Fast and reliable  
✅ Works anywhere  
✅ ~$0.10-0.50 per video  

**👉 [Compare Versions](LOCAL_VS_API.md)**

## 📦 Quick Start

### Local Version (No API Key!)

```bash
# 1. Clone repository
git clone https://github.com/MeetModi24/youtube-notes-generator.git
cd youtube-notes-generator

# 2. Install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements-local.txt

# 3. Process your first video
python youtube_notes_local.py \
  --video "https://www.youtube.com/watch?v=VIDEO_ID" \
  --repo-path ~/my-learning-repo \
  --output-dir course-name
```

**📚 [Local Setup Guide](SETUP_LOCAL.md) | [Quick Start](START_HERE_LOCAL.md)**

### API Version

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Configure API key
echo "ANTHROPIC_API_KEY=your_key_here" > .env

# 3. Process video
python youtube_notes.py \
  --video "https://www.youtube.com/watch?v=VIDEO_ID" \
  --repo-path ~/my-learning-repo \
  --output-dir course-name
```

**📚 [API Setup Guide](SETUP.md) | [Quick Start](QUICKSTART.md)**

## 📖 What You Get

### Input
YouTube video URL or playlist

### Output
```
your-repo/
└── course-name/
    ├── README.md                    # Course overview
    ├── 01-first-lesson/
    │   ├── README.md               # Detailed notes
    │   └── diagrams/
    │       ├── 01-flowchart.mmd
    │       ├── 02-mindmap.mmd
    │       └── 03-sequence.mmd
    ├── 02-second-lesson/
    └── ...
```

### Each Lesson Includes
- 📝 Overview and key concepts
- 📚 Detailed notes with examples
- 📊 Visual diagrams (Mermaid format)
- ❓ Practice questions
- 💡 Key takeaways
- 🔗 Additional topics to explore

## 💻 Usage Examples

### Process Single Video
```bash
python youtube_notes_local.py \
  --video "https://www.youtube.com/watch?v=kqtD5dpn9C8" \
  --repo-path ~/learning/python-course \
  --output-dir fundamentals
```

### Process Playlist
```bash
python youtube_notes_local.py \
  --playlist "https://www.youtube.com/playlist?list=PLAYLIST_ID" \
  --videos 1,2,3 \
  --repo-path ~/learning/complete-course \
  --output-dir full-series
```

### Add More Videos Later
```bash
python youtube_notes_local.py \
  --playlist "https://www.youtube.com/playlist?list=PLAYLIST_ID" \
  --videos 4,5 \
  --repo-path ~/learning/complete-course \
  --output-dir full-series \
  --start-number 4
```

**📚 [More Examples](USAGE_EXAMPLES.md)**

## 🎯 Use Cases

- 👨‍🎓 **Students** - Automate course note-taking
- 📖 **Self-Learners** - Document tutorial series
- 👥 **Teams** - Create training documentation
- 🏫 **Educators** - Generate study materials
- 🔬 **Researchers** - Analyze video content

## 📋 Requirements

- Python 3.8+
- Git
- Claude CLI (for local version) OR Anthropic API key (for API version)
- FFmpeg (optional)

## 🛠️ Installation

### Local Version
```bash
pip install -r requirements-local.txt
```

### API Version
```bash
pip install -r requirements.txt
```

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [START_HERE_LOCAL.md](START_HERE_LOCAL.md) | Quick start for local version |
| [START_HERE.md](START_HERE.md) | Quick start for API version |
| [SETUP_LOCAL.md](SETUP_LOCAL.md) | Local version setup guide |
| [SETUP.md](SETUP.md) | API version setup guide |
| [LOCAL_VS_API.md](LOCAL_VS_API.md) | Compare both versions |
| [FEATURES.md](FEATURES.md) | Complete feature list |
| [USAGE_EXAMPLES.md](USAGE_EXAMPLES.md) | Real-world examples |
| [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) | Project overview |

## 🎨 Customization

### Note Styles
```bash
--style academic   # Formal, detailed
--style casual     # Conversational, easy
--style technical  # Code-focused, concise
```

### Options
```bash
--video URL                    # Single video
--playlist URL --videos 1,2,3  # Multiple videos
--start-number 4               # Continue numbering
--no-commit                    # Don't commit to Git
--branch learning-notes        # Use specific branch
```

## 🧪 Testing

### Local Version
```bash
./test_local.sh
```

### API Version
```bash
./test_demo.sh
```

## 💰 Cost

### Local Version
**Free!** Uses your existing DevBar/AWS Bedrock setup.

### API Version
- Short video (5-10 min): ~$0.10-0.20
- Medium video (20-30 min): ~$0.30-0.50
- Long video (60+ min): ~$0.50-1.00

## 🤝 Contributing

Contributions welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🌟 Features Roadmap

- [ ] Multi-language transcript support
- [ ] Interactive quiz generation
- [ ] Flashcard export (Anki format)
- [ ] Video timestamp linking
- [ ] Progress analytics
- [ ] Web interface
- [ ] Browser extension

## 🙏 Acknowledgments

Built with:
- [Anthropic Claude](https://anthropic.com) - AI analysis
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - YouTube metadata
- [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api) - Transcript extraction
- [Mermaid](https://mermaid.js.org/) - Diagram generation

## 📞 Support

- 📖 Check [documentation](START_HERE_LOCAL.md)
- 🐛 [Report issues](https://github.com/MeetModi24/youtube-notes-generator/issues)
- 💬 [Discussions](https://github.com/MeetModi24/youtube-notes-generator/discussions)

## ⭐ Star History

If you find this useful, please star the repository!

---

**Transform your YouTube learning into organized, searchable knowledge!** 🚀📚
