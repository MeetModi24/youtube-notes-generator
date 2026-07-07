# YouTube Notes Generator - Project Summary

## What Is This?

A powerful tool that automatically transforms YouTube videos into comprehensive, student-friendly learning notes with diagrams, organized in a Git repository.

**In Simple Terms:** Point it at YouTube videos → Get structured markdown notes with diagrams → Automatically organized in your GitHub repo.

## Key Features at a Glance

✅ **Automatic Transcript Extraction** - Fetches video captions/transcripts  
✅ **AI-Powered Analysis** - Uses Claude AI to understand and structure content  
✅ **Diagram Generation** - Creates flowcharts, mind maps, sequence diagrams  
✅ **Smart Organization** - Clean folder structure with numbered lessons  
✅ **Git Integration** - Auto-commits with descriptive messages  
✅ **Playlist Support** - Process entire playlists or specific videos  
✅ **Incremental Updates** - Add new videos to existing notes  
✅ **Multiple Styles** - Academic, casual, or technical writing styles  

## Quick Start (5 Minutes)

```bash
# 1. Setup
cd ~/youtube-notes-generator
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY

# 2. Create learning repo
mkdir -p ~/learning-repos/my-course
cd ~/learning-repos/my-course
git init

# 3. Process your first video
cd ~/youtube-notes-generator
python youtube_notes.py \
  --video "https://www.youtube.com/watch?v=YOUR_VIDEO_ID" \
  --repo-path ~/learning-repos/my-course \
  --output-dir python-basics

# 4. View your notes
cd ~/learning-repos/my-course/python-basics
cat README.md
```

## What You Get

### Input
- YouTube video URL or playlist

### Output
```
your-repo/
└── course-name/
    ├── README.md                    # Course overview & index
    ├── 01-first-topic/
    │   ├── README.md               # Detailed lesson notes
    │   └── diagrams/
    │       ├── 01-flowchart.mmd
    │       ├── 02-sequence.mmd
    │       └── 03-mindmap.mmd
    ├── 02-second-topic/
    │   └── ...
    └── SUMMARY.md                   # Quick reference
```

### Each Lesson Note Includes
1. **Overview** - 2-3 sentence summary
2. **Key Concepts** - 5-8 main points
3. **Detailed Notes** - Organized by topics with examples
4. **Visual Diagrams** - Mermaid diagrams for key concepts
5. **Practice Questions** - Self-check questions
6. **Key Takeaways** - Most important points
7. **Additional Topics** - What to learn next

## Use Cases

### For Students
📚 Automatically create course notes  
📝 Generate study guides for exams  
🔖 Build personal knowledge base  
✅ Track learning progress with Git  

### For Self-Learners
🎓 Document online courses  
📖 Organize tutorial playlists  
🗂️ Create reference materials  
📊 Visualize concepts with diagrams  

### For Teams/Organizations
👥 Create training documentation  
📘 Onboarding materials generation  
🔄 Knowledge base building  
📚 Technical documentation  

## Project Structure

```
youtube-notes-generator/
├── README.md              # Main documentation
├── SETUP.md              # Complete setup instructions
├── QUICKSTART.md         # 5-minute quick start
├── USAGE_EXAMPLES.md     # Common usage patterns
├── FEATURES.md           # Detailed feature list
├── youtube_notes.py      # Main application
├── requirements.txt      # Python dependencies
├── .env.example          # Configuration template
├── test_demo.sh         # Demo/test script
└── LICENSE              # MIT License
```

## Technology Stack

- **Python 3.8+** - Core language
- **Anthropic Claude** - AI content analysis
- **yt-dlp** - YouTube metadata extraction
- **youtube-transcript-api** - Transcript fetching
- **GitPython** - Git operations
- **Mermaid** - Diagram generation

## Command Line Interface

### Basic Usage
```bash
python youtube_notes.py \
  --video "VIDEO_URL" \
  --repo-path "/path/to/repo" \
  --output-dir "course-name"
```

### Playlist Processing
```bash
python youtube_notes.py \
  --playlist "PLAYLIST_URL" \
  --videos 1,2,3 \
  --repo-path "/path/to/repo" \
  --output-dir "course-name"
```

### All Options
- `--video` - Single video URL
- `--playlist` - Playlist URL
- `--videos` - Video indices (e.g., 1,2,3)
- `--repo-path` - Git repository path
- `--output-dir` - Output directory name
- `--style` - Note style (academic/casual/technical)
- `--language` - Transcript language
- `--no-commit` - Don't commit to Git
- `--branch` - Git branch name
- `--start-number` - Starting lesson number

## Example Workflows

### Workflow 1: Daily Learning
```bash
# Monday
python youtube_notes.py --playlist "URL" --videos 1,2 --repo-path ~/learning --output-dir week1

# Tuesday
python youtube_notes.py --playlist "URL" --videos 3,4 --repo-path ~/learning --output-dir week1 --start-number 3
```

### Workflow 2: Complete Course
```bash
# Process all videos in a playlist
for i in {1..10}; do
  python youtube_notes.py \
    --playlist "URL" \
    --videos $i \
    --repo-path ~/learning/full-course \
    --output-dir complete-series \
    --start-number $i
  sleep 30
done
```

### Workflow 3: Multiple Sources
```bash
# Compare different instructors
python youtube_notes.py --video "URL1" --repo-path ~/learning/topic --output-dir instructor-a
python youtube_notes.py --video "URL2" --repo-path ~/learning/topic --output-dir instructor-b
```

## Configuration

### Environment Variables (.env)
```env
ANTHROPIC_API_KEY=your_key_here
GITHUB_REPO_PATH=/default/repo/path
DEFAULT_OUTPUT_DIR=learning-notes
AI_MODEL=claude-sonnet-4-20250514
```

## Costs

### API Usage
- Uses Anthropic Claude API (paid service)
- Cost per video: ~$0.10-0.50 (depending on length)
- Optimized prompts to minimize token usage

### Free Alternatives
- YouTube transcripts are free
- Can modify to use OpenAI or local LLMs

## Limitations

⚠️ **Requires video transcripts** (captions/subtitles)  
⚠️ **Best with English content** (other languages vary)  
⚠️ **API costs** (Anthropic API usage)  
⚠️ **Processing time** increases with video length  

## Best Practices

✅ Choose videos with quality transcripts  
✅ Process 2-5 videos at a time  
✅ Review and customize generated notes  
✅ Add personal annotations  
✅ Commit incrementally  
✅ Use descriptive folder names  

## Documentation Quick Links

- [SETUP.md](SETUP.md) - Complete installation guide
- [QUICKSTART.md](QUICKSTART.md) - Get started in 5 minutes
- [USAGE_EXAMPLES.md](USAGE_EXAMPLES.md) - Real-world examples
- [FEATURES.md](FEATURES.md) - All capabilities explained
- [LICENSE](LICENSE) - MIT License

## Getting Help

```bash
# Command help
python youtube_notes.py --help

# Test installation
./test_demo.sh

# Check documentation
cat README.md
cat QUICKSTART.md
```

## Future Enhancements

Planned features:
- [ ] Multi-language support
- [ ] Interactive quiz generation
- [ ] Flashcard export (Anki)
- [ ] Video timestamp links
- [ ] Progress analytics
- [ ] Web interface
- [ ] Browser extension
- [ ] Notion/Obsidian integration

## Contributing

This is a personal tool, but contributions are welcome:
1. Fork the repository
2. Create feature branch
3. Test your changes
4. Submit pull request

## License

MIT License - Free to use, modify, and distribute.

See [LICENSE](LICENSE) for details.

## Success Stories

This tool helps:
- **Students** take better notes from lecture recordings
- **Self-learners** organize online course content
- **Teams** document training videos
- **Teachers** create study materials
- **Researchers** analyze video content

## System Requirements

- Python 3.8+
- 2GB+ RAM
- Git
- Internet connection
- Anthropic API key

## Platform Support

✅ macOS  
✅ Linux  
✅ Windows (WSL recommended)  

## Performance

- Average processing time: 1-3 minutes per video
- Depends on: video length, API response time, transcript availability
- Can process in parallel (multiple videos)

## Security & Privacy

🔒 API keys stored in `.env` (gitignored)  
🔒 No video downloads (transcripts only)  
🔒 All processing done locally  
🔒 Notes stored in your repositories  

## Support & Contact

- Issues: File an issue on GitHub
- Questions: Check documentation first
- Improvements: Submit a pull request

---

**Built with ❤️ for learners everywhere**

Transform your YouTube learning into organized, searchable, shareable knowledge.

Start building your learning library today! 🚀
