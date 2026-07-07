# Local Setup Guide (DevBar/AWS Bedrock)

This version works with your local DevBar setup - **no API key required**!

## What's Different?

✅ **No API key needed** - Uses your local Claude installation  
✅ **Uses DevBar/AWS Bedrock** - Leverages your existing setup  
✅ **Same features** - All functionality, just different backend  
✅ **Lighter dependencies** - Fewer packages to install  

## Prerequisites

1. **Python 3.8+** 
   ```bash
   python3 --version
   ```

2. **Git**
   ```bash
   git --version
   ```

3. **DevBar with Claude CLI** (you already have this!)
   ```bash
   claude --version
   # or
   which claude
   ```

4. **FFmpeg** (optional, for audio processing)
   ```bash
   brew install ffmpeg  # macOS
   ```

## Quick Setup (3 Steps)

### Step 1: Install Dependencies

```bash
cd ~/youtube-notes-generator

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies (no API key packages!)
pip install -r requirements-local.txt
```

### Step 2: Verify Claude CLI

```bash
# Check if claude command is accessible
claude --version

# If not found, check DevBar installation
ls -la ~/.devbar/bin/
```

### Step 3: Test It!

```bash
# Create test repository
mkdir -p ~/test-youtube-notes
cd ~/test-youtube-notes
git init

# Process a short video
cd ~/youtube-notes-generator
python youtube_notes_local.py \
  --video "https://www.youtube.com/watch?v=kqtD5dpn9C8" \
  --repo-path ~/test-youtube-notes \
  --output-dir test-course \
  --no-commit
```

## Usage

### Basic Command

```bash
python youtube_notes_local.py \
  --video "VIDEO_URL" \
  --repo-path "/path/to/repo" \
  --output-dir "course-name"
```

### Process Playlist

```bash
python youtube_notes_local.py \
  --playlist "PLAYLIST_URL" \
  --videos 1,2,3 \
  --repo-path "~/learning/my-course" \
  --output-dir "python-basics"
```

### All Options

Same as the original version:
- `--video` - Single video URL
- `--playlist` - Playlist URL  
- `--videos` - Video indices (e.g., 1,2,3)
- `--repo-path` - Git repository path
- `--output-dir` - Output directory name
- `--style` - Note style (academic/casual/technical)
- `--no-commit` - Don't commit to Git
- `--branch` - Git branch name
- `--start-number` - Starting lesson number

## How It Works

Instead of calling Anthropic API directly, this version:

1. **Uses subprocess** to call `claude ask` command
2. **Leverages your DevBar setup** (AWS Bedrock/LLM Gateway)
3. **No authentication needed** - Uses your existing credentials
4. **Same AI quality** - Still using Claude models

## Differences from API Version

| Feature | API Version | Local Version |
|---------|-------------|---------------|
| API Key | Required | Not needed ✅ |
| Dependencies | More packages | Fewer packages ✅ |
| Speed | Fast | Slightly slower |
| Cost | Paid API calls | Uses your Bedrock setup ✅ |
| Features | Full | Full ✅ |

## Troubleshooting

### Error: "Claude CLI not found"

**Solution:**
```bash
# Check if claude is in PATH
which claude

# If not, find it
find ~ -name "claude" -type f 2>/dev/null

# Add to PATH if needed
export PATH="$PATH:$HOME/.devbar/bin"

# Or create symlink
ln -s ~/.devbar/bin/claude /usr/local/bin/claude
```

### Error: "Command timed out"

**Solution:**
- Long videos may take time to process
- The script has 2-minute timeout per AI call
- Process shorter videos or increase timeout in code

### Error: "No transcript available"

**Solution:**
- Same as original version
- Choose videos with captions enabled
- Look for [CC] icon on YouTube

## Examples

### Daily Learning Routine

```bash
# Monday: Process 2 videos
python youtube_notes_local.py \
  --playlist "YOUR_PLAYLIST" \
  --videos 1,2 \
  --repo-path ~/learning/course \
  --output-dir week1

# Tuesday: Add 2 more
python youtube_notes_local.py \
  --playlist "YOUR_PLAYLIST" \
  --videos 3,4 \
  --repo-path ~/learning/course \
  --output-dir week1 \
  --start-number 3
```

### Complete Course

```bash
# Process entire playlist
for i in {1..10}; do
  python youtube_notes_local.py \
    --playlist "PLAYLIST_URL" \
    --videos $i \
    --repo-path ~/learning/full-course \
    --output-dir complete-series \
    --start-number $i
  sleep 30  # Rate limiting
done
```

## Performance Tips

1. **Process 1-2 videos at a time** - Each AI call takes 30-120 seconds
2. **Use good transcripts** - Better input = better output
3. **Monitor first run** - Check if Claude CLI is responding
4. **Add sleep between batches** - Give system time to process

## Cost

**Free!** (Well, uses your existing AWS Bedrock/DevBar setup)
- No additional API charges
- Uses your company's infrastructure
- Same quality as paid API version

## Advanced: Customize Claude Command

If your Claude CLI is at a different location or requires special flags:

Edit `youtube_notes_local.py` line ~45:

```python
def _find_claude_command(self) -> str:
    possible_paths = [
        'claude',
        '/usr/local/bin/claude',
        '/path/to/your/claude',  # Add your path here
    ]
    # ...
```

Or set environment variable:

```bash
export CLAUDE_CMD="/path/to/your/claude"
```

## Next Steps

1. ✅ Dependencies installed
2. ✅ Claude CLI verified  
3. → Process your first video
4. → Build your learning library!

## Comparison Scripts

Both versions are available:

- `youtube_notes.py` - Original (needs API key)
- `youtube_notes_local.py` - Local (uses DevBar) ✅

Choose `youtube_notes_local.py` for your setup!

## Getting Help

```bash
# Command help
python youtube_notes_local.py --help

# Test Claude CLI
claude ask "Hello, are you working?"

# Check dependencies
pip list | grep -E "yt-dlp|youtube-transcript|GitPython"
```

## Success Indicators

When working correctly, you'll see:

```
YouTube Notes Generator - Local Version (DevBar/AWS Bedrock)
No API key required - using your local Claude setup

✓ Found Claude CLI at: /path/to/claude

============================================================
Processing video 1...
============================================================

1. Fetching video metadata...
   Title: Python Tutorial for Beginners

2. Fetching transcript...
   Transcript length: 15234 characters

3. Analyzing content with local Claude...

4. Building notes...
   Saved: /path/to/notes/README.md

5. Creating diagram placeholders...
   Created: /path/to/diagrams/01-concept-overview.mmd

============================================================
✓ Successfully processed 1 video(s)
============================================================
```

---

**Perfect for your local DevBar setup! No API keys, no external dependencies.** 🚀
