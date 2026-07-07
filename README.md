# YouTube Notes Generator

Automatically transform YouTube videos into comprehensive, student-friendly learning notes with diagrams, flow charts, and organized structure.

## Features

- **Video Content Extraction**: Downloads and transcribes YouTube videos
- **Intelligent Summarization**: Creates structured notes with key concepts highlighted
- **Diagram Generation**: Automatically generates Mermaid diagrams for:
  - Flowcharts for processes
  - Sequence diagrams for step-by-step procedures
  - Mind maps for concept relationships
  - Architecture diagrams for system designs
- **GitHub Integration**: Automatically commits and organizes notes in your repository
- **Playlist Support**: Process multiple videos and maintain coherent structure
- **Incremental Updates**: Add new videos to existing note collections

## Installation

```bash
pip install -r requirements.txt
```

### Prerequisites

- Python 3.8+
- FFmpeg (for audio processing)
- Git configured with GitHub access
- OpenAI API key or Anthropic API key (for content processing)

## Usage

### Single Video

```bash
python youtube_notes.py \
  --video "https://www.youtube.com/watch?v=VIDEO_ID" \
  --repo-path "/path/to/your/github/repo" \
  --output-dir "course-name"
```

### Multiple Videos from Playlist

```bash
python youtube_notes.py \
  --playlist "https://www.youtube.com/playlist?list=PLAYLIST_ID" \
  --videos 1,2 \
  --repo-path "/path/to/your/github/repo" \
  --output-dir "course-name"
```

### Add to Existing Notes

```bash
python youtube_notes.py \
  --video "https://www.youtube.com/watch?v=VIDEO_ID" \
  --repo-path "/path/to/your/github/repo" \
  --output-dir "course-name" \
  --append
```

## Configuration

Create a `.env` file:

```env
ANTHROPIC_API_KEY=your_api_key_here
GITHUB_REPO_PATH=/path/to/your/repo
DEFAULT_OUTPUT_DIR=learning-notes
```

## Output Structure

```
your-repo/
├── course-name/
│   ├── README.md                 # Course overview and index
│   ├── 01-topic-name/
│   │   ├── README.md             # Lesson notes
│   │   ├── diagrams/
│   │   │   ├── concept-map.mmd
│   │   │   └── process-flow.mmd
│   │   └── resources.md          # Additional links and references
│   ├── 02-another-topic/
│   │   └── ...
│   └── SUMMARY.md                # Quick reference guide
```

## Note Structure

Each lesson note includes:

1. **Video Metadata**: Title, URL, duration, date
2. **Overview**: High-level summary (2-3 sentences)
3. **Key Concepts**: Bullet points of main ideas
4. **Detailed Notes**: Structured by topics with:
   - Explanations
   - Code examples (if applicable)
   - Visual diagrams
5. **Practice Questions**: Self-check questions
6. **Additional Resources**: Related links and readings

## Example

```bash
# Process first two videos of a Python course
python youtube_notes.py \
  --playlist "https://www.youtube.com/playlist?list=PLZoTAELRMXVNUL99R4bDlVYsncUNvwUBB" \
  --videos 1,2 \
  --repo-path "~/learning-repos/python-mastery" \
  --output-dir "python-basics"
```

## Advanced Options

- `--language`: Transcript language (default: en)
- `--style`: Note style (academic, casual, technical)
- `--diagram-types`: Comma-separated list (flowchart, sequence, mindmap, class)
- `--max-length`: Maximum note length in words
- `--no-commit`: Generate notes without committing to Git
- `--branch`: Target Git branch (default: main)

## Architecture

1. **Video Processor**: Downloads video metadata and transcript
2. **Content Analyzer**: Uses AI to understand and structure content
3. **Diagram Generator**: Creates visual representations using Mermaid
4. **Markdown Builder**: Assembles formatted notes
5. **Git Manager**: Organizes and commits to repository

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development guidelines.

## License

MIT License - See [LICENSE](LICENSE)
