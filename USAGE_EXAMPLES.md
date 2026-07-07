# Usage Examples

## Setup

```bash
# Clone the repository
cd ~/youtube-notes-generator

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
```

## Example 1: Single Video Notes

Process a single Python tutorial video:

```bash
python youtube_notes.py \
  --video "https://www.youtube.com/watch?v=rfscVS0vtbw" \
  --repo-path "~/learning-repos/python-course" \
  --output-dir "python-fundamentals" \
  --style academic
```

Output structure:
```
python-course/
└── python-fundamentals/
    ├── README.md                    # Course index
    └── 01-learn-python-full-course/
        ├── README.md                # Lesson notes
        └── diagrams/
            ├── 01-flowchart.mmd
            └── 02-mindmap.mmd
```

## Example 2: Multiple Videos from Playlist

Process first 3 videos from a playlist:

```bash
python youtube_notes.py \
  --playlist "https://www.youtube.com/playlist?list=PLZoTAELRMXVNUL99R4bDlVYsncUNvwUBB" \
  --videos 1,2,3 \
  --repo-path "~/learning-repos/python-mastery" \
  --output-dir "data-structures" \
  --style technical
```

## Example 3: Add More Videos to Existing Course

Add videos 4 and 5 to an existing course:

```bash
python youtube_notes.py \
  --playlist "https://www.youtube.com/playlist?list=PLZoTAELRMXVNUL99R4bDlVYsncUNvwUBB" \
  --videos 4,5 \
  --repo-path "~/learning-repos/python-mastery" \
  --output-dir "data-structures" \
  --start-number 4 \
  --branch learning-notes
```

## Example 4: Generate Without Committing

Test the output without committing to Git:

```bash
python youtube_notes.py \
  --video "https://www.youtube.com/watch?v=kqtD5dpn9C8" \
  --repo-path "~/learning-repos/test-repo" \
  --output-dir "test-notes" \
  --no-commit
```

## Example 5: Web Development Course

Process a complete web development series:

```bash
# Day 1: HTML basics (videos 1-3)
python youtube_notes.py \
  --playlist "https://www.youtube.com/playlist?list=PLr6-GrHUlVf_ZNmuQSXdS197Oyr1L9sPB" \
  --videos 1,2,3 \
  --repo-path "~/learning-repos/web-dev-bootcamp" \
  --output-dir "html-css-fundamentals" \
  --style casual

# Day 2: CSS (videos 4-6)
python youtube_notes.py \
  --playlist "https://www.youtube.com/playlist?list=PLr6-GrHUlVf_ZNmuQSXdS197Oyr1L9sPB" \
  --videos 4,5,6 \
  --repo-path "~/learning-repos/web-dev-bootcamp" \
  --output-dir "html-css-fundamentals" \
  --start-number 4 \
  --branch main
```

## Example 6: Using Different Note Styles

### Academic Style (detailed, formal)
```bash
python youtube_notes.py \
  --video "https://www.youtube.com/watch?v=VIDEO_ID" \
  --repo-path "~/learning-repos/cs-theory" \
  --output-dir "algorithms" \
  --style academic
```

### Casual Style (conversational, easier to read)
```bash
python youtube_notes.py \
  --video "https://www.youtube.com/watch?v=VIDEO_ID" \
  --repo-path "~/learning-repos/quick-tutorials" \
  --output-dir "tips-tricks" \
  --style casual
```

### Technical Style (code-focused, concise)
```bash
python youtube_notes.py \
  --video "https://www.youtube.com/watch?v=VIDEO_ID" \
  --repo-path "~/learning-repos/api-docs" \
  --output-dir "rest-api-design" \
  --style technical
```

## Example 7: Complete Learning Journey

Set up a comprehensive learning repository:

```bash
# Create learning repository
mkdir -p ~/learning-repos/full-stack-journey
cd ~/learning-repos/full-stack-journey
git init

# Week 1: JavaScript Fundamentals
python ~/youtube-notes-generator/youtube_notes.py \
  --playlist "https://www.youtube.com/playlist?list=PL4cUxeGkcC9i9Ae2D9Ee1RvylH38dKuET" \
  --videos 1,2,3,4,5 \
  --repo-path "~/learning-repos/full-stack-journey" \
  --output-dir "01-javascript-basics"

# Week 2: React Fundamentals
python ~/youtube-notes-generator/youtube_notes.py \
  --playlist "https://www.youtube.com/playlist?list=PL4cUxeGkcC9gZD-Tvwfod2gaISzfRiP9d" \
  --videos 1,2,3,4,5 \
  --repo-path "~/learning-repos/full-stack-journey" \
  --output-dir "02-react-fundamentals"

# Week 3: Node.js Backend
python ~/youtube-notes-generator/youtube_notes.py \
  --playlist "https://www.youtube.com/playlist?list=PL4cUxeGkcC9jsz4LDYc6kv3ymONOKxwBU" \
  --videos 1,2,3,4,5 \
  --repo-path "~/learning-repos/full-stack-journey" \
  --output-dir "03-nodejs-backend"
```

## Example 8: Study Multiple Sources

Compare different teaching styles for the same topic:

```bash
# Teacher A's approach
python youtube_notes.py \
  --video "https://www.youtube.com/watch?v=VIDEO_A" \
  --repo-path "~/learning-repos/react-comparison" \
  --output-dir "teacher-a-react" \
  --start-number 1

# Teacher B's approach
python youtube_notes.py \
  --video "https://www.youtube.com/watch?v=VIDEO_B" \
  --repo-path "~/learning-repos/react-comparison" \
  --output-dir "teacher-b-react" \
  --start-number 1
```

## Tips for Best Results

1. **Choose videos with good transcripts**: Auto-generated captions work, but manual transcripts are better

2. **Process related videos together**: Use playlists to maintain context and topic flow

3. **Use descriptive output directories**: Name folders by topic (e.g., "python-data-structures" not "course1")

4. **Incremental learning**: Process 2-5 videos at a time, review notes, then continue

5. **Branch strategy**: Use different branches for different learning tracks
   ```bash
   --branch frontend-track
   --branch backend-track
   --branch algorithms-track
   ```

6. **Review and customize**: After generation, review notes and add your own examples/clarifications

## Viewing Generated Diagrams

The tool generates Mermaid diagrams. To view them:

### Option 1: GitHub (automatic rendering)
Push to GitHub and view - GitHub renders Mermaid automatically

### Option 2: VS Code
Install "Markdown Preview Mermaid Support" extension

### Option 3: Online Viewer
Visit https://mermaid.live and paste diagram code

### Option 4: Markdown Preview
Many markdown preview tools support Mermaid (Typora, Obsidian, etc.)

## Troubleshooting

### No transcript available
```
Warning: No transcript available. Notes will be limited.
```
Solution: Choose a video with captions/subtitles enabled

### API errors
```
Error analyzing content: <error message>
```
Solution: Check your ANTHROPIC_API_KEY in .env file

### Git errors
```
Error: Repository path does not exist
```
Solution: Create the repository first or provide correct path

## Next Steps

After generating notes:

1. **Review and annotate**: Add your own insights and examples
2. **Practice**: Work through the practice questions
3. **Create summaries**: Make flashcards from key takeaways
4. **Build projects**: Apply concepts in real projects
5. **Share**: Push to GitHub to share with others or track your progress
