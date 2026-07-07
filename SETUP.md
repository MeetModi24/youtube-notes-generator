# Complete Setup Guide

## Prerequisites

Before you begin, ensure you have:

1. **Python 3.8 or higher**
   ```bash
   python3 --version
   ```

2. **Git** (for repository management)
   ```bash
   git --version
   ```

3. **FFmpeg** (for audio processing, though we primarily use transcripts)
   ```bash
   ffmpeg -version
   ```

4. **Anthropic API Key** (get from https://console.anthropic.com/)

## Installation Steps

### Step 1: Clone or Download the Tool

```bash
cd ~
# If you have it in a Git repo:
# git clone https://github.com/yourusername/youtube-notes-generator.git
# Otherwise, it should already be at:
cd ~/youtube-notes-generator
```

### Step 2: Create Virtual Environment

```bash
python3 -m venv venv
```

Activate it:
- **macOS/Linux**: `source venv/bin/activate`
- **Windows**: `venv\Scripts\activate`

You should see `(venv)` in your terminal prompt.

### Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

This installs:
- `anthropic` - Claude AI SDK
- `yt-dlp` - YouTube metadata fetcher
- `youtube-transcript-api` - Transcript extraction
- `GitPython` - Git operations
- Other supporting libraries

### Step 4: Install FFmpeg (if needed)

**macOS** (using Homebrew):
```bash
brew install ffmpeg
```

**Ubuntu/Debian**:
```bash
sudo apt update
sudo apt install ffmpeg
```

**Windows**:
1. Download from https://ffmpeg.org/download.html
2. Extract and add to PATH
3. Or use Chocolatey: `choco install ffmpeg`

### Step 5: Configure API Key

```bash
# Copy example configuration
cp .env.example .env

# Edit the file
nano .env  # or vim, code, etc.
```

Add your Anthropic API key:
```env
ANTHROPIC_API_KEY=sk-ant-api03-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Save and exit.

### Step 6: Verify Installation

```bash
python youtube_notes.py --help
```

You should see the help message with all available options.

## Quick Verification Test

Let's test with a short video:

```bash
# Create test repository
mkdir -p ~/test-youtube-notes
cd ~/test-youtube-notes
git init

# Process a short video (5 min Python tutorial)
cd ~/youtube-notes-generator
python youtube_notes.py \
  --video "https://www.youtube.com/watch?v=kqtD5dpn9C8" \
  --repo-path ~/test-youtube-notes \
  --output-dir test-course \
  --no-commit
```

Expected output:
```
============================================================
Processing video 1...
============================================================

1. Fetching video metadata...
   Title: Python Tutorial for Beginners

2. Fetching transcript...
   Transcript length: XXXX characters

3. Analyzing content with AI...

4. Building notes...
   Saved: /Users/yourusername/test-youtube-notes/test-course/01-python-tutorial/README.md

5. Generating diagrams...
   Generated X diagrams

============================================================
✓ Successfully processed 1 video(s)
============================================================
```

Check the output:
```bash
ls -la ~/test-youtube-notes/test-course/
cat ~/test-youtube-notes/test-course/README.md
```

## Creating Your Learning Repository

### Recommended Structure

```bash
# Create your main learning repository
mkdir -p ~/learning-repos
cd ~/learning-repos

# Create course-specific repositories
mkdir python-mastery
mkdir web-development
mkdir data-science

# Initialize Git in each
cd python-mastery && git init
cd ../web-development && git init
cd ../data-science && git init
```

### GitHub Integration (Optional)

To sync with GitHub:

```bash
cd ~/learning-repos/python-mastery

# Create repo on GitHub first, then:
git remote add origin https://github.com/yourusername/python-mastery.git

# After generating notes:
git push -u origin main
```

## Usage Patterns

### Pattern 1: Daily Learning Routine

```bash
# Monday: Watch and process 2 videos
python ~/youtube-notes-generator/youtube_notes.py \
  --playlist "YOUR_PLAYLIST" \
  --videos 1,2 \
  --repo-path ~/learning-repos/current-course \
  --output-dir week-1

# Tuesday: Add 2 more videos
python ~/youtube-notes-generator/youtube_notes.py \
  --playlist "YOUR_PLAYLIST" \
  --videos 3,4 \
  --repo-path ~/learning-repos/current-course \
  --output-dir week-1 \
  --start-number 3
```

### Pattern 2: Playlist Processing

```bash
# Process entire playlist in batches
for i in 1 3 5 7 9; do
  python ~/youtube-notes-generator/youtube_notes.py \
    --playlist "YOUR_PLAYLIST" \
    --videos $i,$((i+1)) \
    --repo-path ~/learning-repos/complete-course \
    --output-dir full-series \
    --start-number $i
  sleep 60  # Rate limiting
done
```

### Pattern 3: Multi-Source Learning

```bash
# Source 1: FreeCodeCamp
python ~/youtube-notes-generator/youtube_notes.py \
  --video "https://www.youtube.com/watch?v=VIDEO1" \
  --repo-path ~/learning-repos/react-study \
  --output-dir freecodecamp-react

# Source 2: Traversy Media
python ~/youtube-notes-generator/youtube_notes.py \
  --video "https://www.youtube.com/watch?v=VIDEO2" \
  --repo-path ~/learning-repos/react-study \
  --output-dir traversy-react

# Source 3: Net Ninja
python ~/youtube-notes-generator/youtube_notes.py \
  --video "https://www.youtube.com/watch?v=VIDEO3" \
  --repo-path ~/learning-repos/react-study \
  --output-dir netninja-react
```

## Troubleshooting

### Issue: "No module named 'anthropic'"

**Solution:**
```bash
# Make sure virtual environment is activated
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Reinstall dependencies
pip install -r requirements.txt
```

### Issue: "No transcript available"

**Solution:**
- Choose a different video with captions enabled
- Look for the [CC] icon on YouTube videos
- Try videos from educational channels (they usually have good transcripts)

### Issue: "API key not found"

**Solution:**
```bash
# Check .env file exists
ls -la .env

# Verify content
cat .env

# Should show:
# ANTHROPIC_API_KEY=sk-ant-api03-...

# If missing, copy from example:
cp .env.example .env
# Then edit and add your key
```

### Issue: "Rate limit exceeded"

**Solution:**
```bash
# Wait a few minutes between large batches
# Or process fewer videos at once

# The API has rate limits:
# - 50 requests per minute (Tier 1)
# - 1000 requests per minute (Tier 2+)
```

### Issue: Git errors

**Solution:**
```bash
# Ensure repo exists and is initialized
mkdir -p ~/learning-repos/my-course
cd ~/learning-repos/my-course
git init

# Configure Git if needed
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

### Issue: FFmpeg not found

**Solution:**
```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt install ffmpeg

# Verify installation
which ffmpeg
ffmpeg -version
```

## Advanced Configuration

### Custom Output Templates

Create custom note templates by modifying `NotesBuilder` class in `youtube_notes.py`.

### Using Different AI Models

Edit `.env`:
```env
AI_MODEL=claude-opus-4-20250514  # More capable, more expensive
# or
AI_MODEL=claude-haiku-4-20250514  # Faster, cheaper
```

### Batch Processing Script

Create `batch_process.sh`:
```bash
#!/bin/bash
REPO_PATH="$HOME/learning-repos/my-course"
PLAYLIST="YOUR_PLAYLIST_URL"

for i in {1..10}; do
  python youtube_notes.py \
    --playlist "$PLAYLIST" \
    --videos $i \
    --repo-path "$REPO_PATH" \
    --output-dir course-notes \
    --start-number $i
  
  echo "Processed video $i, sleeping 30 seconds..."
  sleep 30
done
```

## Maintenance

### Keeping Dependencies Updated

```bash
cd ~/youtube-notes-generator
source venv/bin/activate

# Check for updates
pip list --outdated

# Update specific package
pip install --upgrade anthropic

# Or update all
pip install --upgrade -r requirements.txt
```

### Backing Up Your Notes

```bash
# Method 1: Git push to remote
cd ~/learning-repos/my-course
git push origin main

# Method 2: Archive locally
tar -czf notes-backup-$(date +%Y%m%d).tar.gz ~/learning-repos/

# Method 3: Cloud sync (Dropbox, Google Drive, etc.)
# Just put ~/learning-repos/ in your synced folder
```

## Next Steps

1. ✓ Installation complete
2. ✓ Test run successful
3. → Read [USAGE_EXAMPLES.md](USAGE_EXAMPLES.md) for more examples
4. → Check [FEATURES.md](FEATURES.md) for all capabilities
5. → Start processing your first real course!

## Getting Help

- Check [USAGE_EXAMPLES.md](USAGE_EXAMPLES.md) for common patterns
- Review [FEATURES.md](FEATURES.md) for capabilities
- Read [QUICKSTART.md](QUICKSTART.md) for quick reference
- Run `python youtube_notes.py --help` for options

Happy learning! 📚
