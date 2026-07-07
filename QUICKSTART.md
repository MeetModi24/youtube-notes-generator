# Quick Start Guide

Get started with YouTube Notes Generator in 5 minutes.

## Installation

```bash
# Navigate to the tool directory
cd ~/youtube-notes-generator

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install FFmpeg (if not already installed)
# macOS:
brew install ffmpeg

# Ubuntu/Debian:
# sudo apt-get install ffmpeg

# Windows:
# Download from https://ffmpeg.org/download.html
```

## Configuration

```bash
# Copy example environment file
cp .env.example .env

# Edit .env and add your API key
# Get API key from: https://console.anthropic.com/
nano .env  # or use your preferred editor
```

Your `.env` should look like:
```
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxx
```

## First Run - Single Video

```bash
# Create a test repository
mkdir -p ~/learning-repos/my-first-notes
cd ~/learning-repos/my-first-notes
git init

# Process your first video
cd ~/youtube-notes-generator
python youtube_notes.py \
  --video "https://www.youtube.com/watch?v=rfscVS0vtbw" \
  --repo-path ~/learning-repos/my-first-notes \
  --output-dir python-tutorial
```

## What Just Happened?

The tool:
1. ✓ Downloaded video metadata and transcript
2. ✓ Analyzed content with Claude AI
3. ✓ Generated structured notes with diagrams
4. ✓ Organized everything in your repository
5. ✓ Committed changes to Git

## View Your Notes

```bash
cd ~/learning-repos/my-first-notes/python-tutorial
ls -la
```

You'll see:
```
python-tutorial/
├── README.md                          # Course index
└── 01-learn-python-full-course/
    ├── README.md                      # Detailed notes
    └── diagrams/                      # Visual diagrams
        └── *.mmd files
```

Open in your favorite markdown viewer or push to GitHub!

## Second Run - Multiple Videos

```bash
python youtube_notes.py \
  --playlist "https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID" \
  --videos 1,2,3 \
  --repo-path ~/learning-repos/my-first-notes \
  --output-dir complete-course
```

## Next Steps

1. Read [USAGE_EXAMPLES.md](USAGE_EXAMPLES.md) for more examples
2. Customize note style with `--style` option
3. Process your favorite tutorial playlists
4. Share your learning repository on GitHub

## Common Issues

**Issue: "No transcript available"**
- Solution: Choose videos with captions/subtitles

**Issue: "API key not found"**
- Solution: Check your .env file has ANTHROPIC_API_KEY set

**Issue: "Repository path does not exist"**
- Solution: Create the directory first with `mkdir -p path/to/repo`

## Tips

- Start with 1-2 videos to test
- Review generated notes and customize as needed
- Use playlists for organized learning
- Commit incrementally as you add more videos

Ready to learn? Pick a YouTube video and start generating notes!
