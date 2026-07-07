#!/usr/bin/env python3
"""
YouTube Notes Generator - Transform YouTube videos into comprehensive learning notes
"""

import os
import sys
import argparse
import json
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from datetime import datetime
import re

from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
import yt_dlp
from anthropic import Anthropic
import git


class VideoProcessor:
    """Handles YouTube video metadata and transcript extraction"""

    def __init__(self):
        self.ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'extract_flat': True,
        }

    def extract_video_id(self, url: str) -> str:
        """Extract video ID from various YouTube URL formats"""
        patterns = [
            r'(?:youtube\.com\/watch\?v=|youtu\.be\/)([^&\n?]*)',
            r'youtube\.com\/embed\/([^&\n?]*)',
        ]

        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)

        raise ValueError(f"Could not extract video ID from URL: {url}")

    def get_video_metadata(self, video_url: str) -> Dict:
        """Fetch video metadata using yt-dlp"""
        try:
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                info = ydl.extract_info(video_url, download=False)
                return {
                    'title': info.get('title', 'Unknown'),
                    'description': info.get('description', ''),
                    'duration': info.get('duration', 0),
                    'upload_date': info.get('upload_date', ''),
                    'uploader': info.get('uploader', ''),
                    'thumbnail': info.get('thumbnail', ''),
                    'url': video_url,
                    'video_id': self.extract_video_id(video_url),
                }
        except Exception as e:
            print(f"Error fetching metadata: {e}")
            return {
                'title': 'Unknown',
                'url': video_url,
                'video_id': self.extract_video_id(video_url),
            }

    def get_transcript(self, video_url: str, language: str = 'en') -> str:
        """Fetch video transcript"""
        try:
            video_id = self.extract_video_id(video_url)
            transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])

            # Combine transcript segments
            full_transcript = ' '.join([item['text'] for item in transcript_list])
            return full_transcript

        except Exception as e:
            print(f"Error fetching transcript: {e}")
            print("Attempting to fetch auto-generated captions...")
            try:
                transcript_list = YouTubeTranscriptApi.get_transcript(
                    self.extract_video_id(video_url),
                    languages=['en-US', 'en']
                )
                full_transcript = ' '.join([item['text'] for item in transcript_list])
                return full_transcript
            except Exception as e2:
                print(f"Could not fetch transcript: {e2}")
                return ""

    def get_playlist_videos(self, playlist_url: str, video_indices: Optional[List[int]] = None) -> List[str]:
        """Get video URLs from a playlist"""
        ydl_opts = {
            'quiet': True,
            'extract_flat': True,
            'force_generic_extractor': False,
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                playlist_info = ydl.extract_info(playlist_url, download=False)

                if 'entries' not in playlist_info:
                    raise ValueError("No videos found in playlist")

                video_urls = []
                for idx, entry in enumerate(playlist_info['entries'], start=1):
                    if video_indices and idx not in video_indices:
                        continue

                    video_id = entry.get('id') or entry.get('url')
                    if video_id:
                        video_urls.append(f"https://www.youtube.com/watch?v={video_id}")

                return video_urls

        except Exception as e:
            print(f"Error fetching playlist: {e}")
            return []


class ContentAnalyzer:
    """Uses AI to analyze and structure video content"""

    def __init__(self, api_key: str, model: str = "claude-sonnet-4-20250514"):
        self.client = Anthropic(api_key=api_key)
        self.model = model

    def analyze_content(self, transcript: str, metadata: Dict, style: str = "academic") -> Dict:
        """Analyze transcript and generate structured notes"""

        prompt = f"""You are an expert educational content creator. Analyze this YouTube video transcript and create comprehensive, student-friendly learning notes.

Video Title: {metadata.get('title', 'Unknown')}
Duration: {metadata.get('duration', 0) // 60} minutes

Transcript:
{transcript}

Create structured notes following this format:

1. OVERVIEW (2-3 sentences summarizing the main topic)

2. KEY CONCEPTS (bullet points of main ideas - 5-8 points)

3. DETAILED NOTES
   Organize by major topics/sections. For each section:
   - Clear explanations
   - Examples (with code blocks if applicable)
   - Important definitions or formulas
   - Common pitfalls or misconceptions

4. VISUAL DIAGRAMS NEEDED
   Identify what diagrams would help learning:
   - List each diagram with: type (flowchart/sequence/mindmap/class/er), title, and brief description of what it should show

5. PRACTICE QUESTIONS (3-5 questions to test understanding)

6. KEY TAKEAWAYS (3-5 bullet points of most important points)

7. ADDITIONAL TOPICS TO EXPLORE (related concepts to learn next)

Style: {style}
Make the content engaging, clear, and suitable for self-study. Use markdown formatting."""

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=8000,
                temperature=0.7,
                messages=[{
                    "role": "user",
                    "content": prompt
                }]
            )

            content = response.content[0].text
            return self._parse_structured_notes(content, metadata)

        except Exception as e:
            print(f"Error analyzing content: {e}")
            return {
                'overview': 'Error generating notes',
                'key_concepts': [],
                'detailed_notes': '',
                'diagrams': [],
                'practice_questions': [],
                'key_takeaways': [],
                'additional_topics': [],
            }

    def _parse_structured_notes(self, content: str, metadata: Dict) -> Dict:
        """Parse the AI-generated content into structured sections"""

        sections = {
            'overview': '',
            'key_concepts': [],
            'detailed_notes': '',
            'diagrams': [],
            'practice_questions': [],
            'key_takeaways': [],
            'additional_topics': [],
            'raw_content': content,
        }

        # Simple parsing - in production, you'd want more robust parsing
        sections['raw_content'] = content

        return sections

    def generate_diagram_spec(self, diagram_description: str, diagram_type: str) -> str:
        """Generate Mermaid diagram specification"""

        prompt = f"""Generate a Mermaid diagram specification for the following:

Type: {diagram_type}
Description: {diagram_description}

Return ONLY the Mermaid code, starting with the diagram type declaration (e.g., 'flowchart TD', 'sequenceDiagram', 'mindmap', 'classDiagram').

Make it clear, well-organized, and educational. Use descriptive node names."""

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=2000,
                temperature=0.5,
                messages=[{
                    "role": "user",
                    "content": prompt
                }]
            )

            return response.content[0].text.strip()

        except Exception as e:
            print(f"Error generating diagram: {e}")
            return f"{diagram_type}\n    A[Diagram generation failed]"


class NotesBuilder:
    """Builds formatted markdown notes"""

    def build_lesson_notes(self, metadata: Dict, analysis: Dict, lesson_number: int) -> str:
        """Build complete lesson notes in markdown"""

        title = metadata.get('title', 'Unknown')
        video_url = metadata.get('url', '')
        duration = metadata.get('duration', 0)
        upload_date = metadata.get('upload_date', '')

        # Format duration
        duration_str = f"{duration // 60}:{duration % 60:02d}" if duration else "Unknown"

        # Format date
        date_str = upload_date
        if upload_date and len(upload_date) == 8:
            date_str = f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:]}"

        notes = f"""# Lesson {lesson_number}: {title}

## Video Information

- **URL**: [{video_url}]({video_url})
- **Duration**: {duration_str}
- **Published**: {date_str}
- **Created**: {datetime.now().strftime('%Y-%m-%d')}

---

## Overview

{analysis.get('raw_content', 'Content generation in progress...')}

---

## Diagrams

See the `diagrams/` directory for visual representations of key concepts.

---

## Notes

This lesson covers the concepts outlined above. Review the diagrams and practice questions to reinforce your understanding.

---

*Generated automatically by YouTube Notes Generator*
"""

        return notes

    def build_course_index(self, course_name: str, lessons: List[Dict]) -> str:
        """Build course overview/index README"""

        index = f"""# {course_name}

## Course Overview

This directory contains comprehensive notes from the {course_name} video series.

## Lessons

"""

        for idx, lesson in enumerate(lessons, start=1):
            title = lesson.get('title', f'Lesson {idx}')
            folder = lesson.get('folder', f'{idx:02d}-lesson')
            index += f"{idx}. [{title}](./{folder}/README.md)\n"

        index += f"""

## How to Use These Notes

1. **Start with the overview** of each lesson to understand the main concepts
2. **Study the diagrams** to visualize the concepts
3. **Read the detailed notes** with examples
4. **Test yourself** with practice questions
5. **Explore additional topics** for deeper learning

## Progress Tracking

- [ ] Lesson 1
- [ ] Lesson 2
- [ ] ... (add checkboxes as you complete lessons)

---

*Last updated: {datetime.now().strftime('%Y-%m-%d')}*
"""

        return index


class GitManager:
    """Manages Git operations for the notes repository"""

    def __init__(self, repo_path: str):
        self.repo_path = Path(repo_path)

        if not self.repo_path.exists():
            raise ValueError(f"Repository path does not exist: {repo_path}")

        try:
            self.repo = git.Repo(self.repo_path)
        except git.InvalidGitRepositoryError:
            print(f"Initializing new Git repository at {repo_path}")
            self.repo = git.Repo.init(self.repo_path)

    def create_branch_if_needed(self, branch_name: str):
        """Create and checkout branch if it doesn't exist"""
        current_branch = self.repo.active_branch.name

        if branch_name != current_branch:
            if branch_name in self.repo.heads:
                self.repo.heads[branch_name].checkout()
            else:
                self.repo.create_head(branch_name)
                self.repo.heads[branch_name].checkout()

    def commit_changes(self, message: str, files: List[str] = None):
        """Commit changes to repository"""
        if files:
            self.repo.index.add(files)
        else:
            self.repo.git.add(A=True)

        if self.repo.is_dirty():
            self.repo.index.commit(message)
            print(f"✓ Committed: {message}")
        else:
            print("No changes to commit")


class YouTubeNotesGenerator:
    """Main orchestrator for the YouTube notes generation process"""

    def __init__(self, api_key: str, repo_path: str, output_dir: str):
        self.video_processor = VideoProcessor()
        self.content_analyzer = ContentAnalyzer(api_key)
        self.notes_builder = NotesBuilder()
        self.git_manager = GitManager(repo_path)
        self.output_dir = Path(repo_path) / output_dir

    def process_video(self, video_url: str, lesson_number: int, style: str = "academic") -> Dict:
        """Process a single video and generate notes"""

        print(f"\n{'='*60}")
        print(f"Processing video {lesson_number}...")
        print(f"{'='*60}\n")

        # Fetch metadata
        print("1. Fetching video metadata...")
        metadata = self.video_processor.get_video_metadata(video_url)
        print(f"   Title: {metadata.get('title')}")

        # Fetch transcript
        print("2. Fetching transcript...")
        transcript = self.video_processor.get_transcript(video_url)

        if not transcript:
            print("   Warning: No transcript available. Notes will be limited.")
            transcript = f"No transcript available for: {metadata.get('title')}"
        else:
            print(f"   Transcript length: {len(transcript)} characters")

        # Analyze content
        print("3. Analyzing content with AI...")
        analysis = self.content_analyzer.analyze_content(transcript, metadata, style)

        # Create lesson folder
        lesson_folder_name = self._create_folder_name(metadata.get('title', ''), lesson_number)
        lesson_path = self.output_dir / lesson_folder_name
        lesson_path.mkdir(parents=True, exist_ok=True)

        diagrams_path = lesson_path / "diagrams"
        diagrams_path.mkdir(exist_ok=True)

        # Build and save notes
        print("4. Building notes...")
        notes_content = self.notes_builder.build_lesson_notes(metadata, analysis, lesson_number)
        notes_file = lesson_path / "README.md"
        notes_file.write_text(notes_content)
        print(f"   Saved: {notes_file}")

        # Generate diagrams (if specified in analysis)
        diagram_count = 0
        if 'diagrams' in analysis and analysis['diagrams']:
            print("5. Generating diagrams...")
            for idx, diagram_info in enumerate(analysis['diagrams'][:5], start=1):  # Limit to 5 diagrams
                diagram_type = diagram_info.get('type', 'flowchart')
                diagram_desc = diagram_info.get('description', 'Concept diagram')

                diagram_spec = self.content_analyzer.generate_diagram_spec(diagram_desc, diagram_type)
                diagram_file = diagrams_path / f"{idx:02d}-{diagram_type}.mmd"
                diagram_file.write_text(diagram_spec)
                diagram_count += 1

            print(f"   Generated {diagram_count} diagrams")

        return {
            'title': metadata.get('title'),
            'folder': lesson_folder_name,
            'path': str(lesson_path),
        }

    def process_videos(self, video_urls: List[str], style: str = "academic",
                      start_number: int = 1, commit: bool = True, branch: str = "main"):
        """Process multiple videos"""

        lessons = []

        for idx, video_url in enumerate(video_urls, start=start_number):
            try:
                lesson_info = self.process_video(video_url, idx, style)
                lessons.append(lesson_info)
            except Exception as e:
                print(f"Error processing video {idx}: {e}")
                continue

        # Build course index
        print("\n6. Building course index...")
        course_name = self.output_dir.name.replace('-', ' ').title()
        index_content = self.notes_builder.build_course_index(course_name, lessons)
        index_file = self.output_dir / "README.md"
        index_file.write_text(index_content)
        print(f"   Saved: {index_file}")

        # Commit to Git
        if commit:
            print("\n7. Committing to Git...")
            self.git_manager.create_branch_if_needed(branch)
            commit_message = f"Add notes for {len(lessons)} lesson(s) in {course_name}"
            self.git_manager.commit_changes(commit_message)

        print(f"\n{'='*60}")
        print(f"✓ Successfully processed {len(lessons)} video(s)")
        print(f"{'='*60}\n")

    def _create_folder_name(self, title: str, number: int) -> str:
        """Create a clean folder name from video title"""
        # Remove special characters and convert to lowercase
        clean_title = re.sub(r'[^\w\s-]', '', title.lower())
        clean_title = re.sub(r'[-\s]+', '-', clean_title)
        clean_title = clean_title[:50]  # Limit length

        return f"{number:02d}-{clean_title}"


def main():
    parser = argparse.ArgumentParser(
        description="Transform YouTube videos into comprehensive learning notes"
    )

    parser.add_argument('--video', type=str, help='Single YouTube video URL')
    parser.add_argument('--playlist', type=str, help='YouTube playlist URL')
    parser.add_argument('--videos', type=str, help='Comma-separated video indices (e.g., 1,2,3)')
    parser.add_argument('--repo-path', type=str, required=True, help='Path to Git repository')
    parser.add_argument('--output-dir', type=str, required=True, help='Output directory name within repo')
    parser.add_argument('--style', type=str, default='academic', choices=['academic', 'casual', 'technical'],
                       help='Note style')
    parser.add_argument('--language', type=str, default='en', help='Transcript language code')
    parser.add_argument('--no-commit', action='store_true', help='Generate notes without committing')
    parser.add_argument('--branch', type=str, default='main', help='Git branch to use')
    parser.add_argument('--start-number', type=int, default=1, help='Starting lesson number')

    args = parser.parse_args()

    # Load environment variables
    load_dotenv()
    api_key = os.getenv('ANTHROPIC_API_KEY')

    if not api_key:
        print("Error: ANTHROPIC_API_KEY not found in environment")
        print("Please set it in .env file or environment variables")
        sys.exit(1)

    # Initialize generator
    generator = YouTubeNotesGenerator(api_key, args.repo_path, args.output_dir)

    # Get video URLs
    video_urls = []

    if args.video:
        video_urls = [args.video]
    elif args.playlist:
        video_indices = None
        if args.videos:
            video_indices = [int(x.strip()) for x in args.videos.split(',')]

        print("Fetching playlist videos...")
        video_urls = generator.video_processor.get_playlist_videos(args.playlist, video_indices)

        if not video_urls:
            print("Error: No videos found in playlist")
            sys.exit(1)

        print(f"Found {len(video_urls)} video(s)")
    else:
        print("Error: Must provide either --video or --playlist")
        parser.print_help()
        sys.exit(1)

    # Process videos
    generator.process_videos(
        video_urls,
        style=args.style,
        start_number=args.start_number,
        commit=not args.no_commit,
        branch=args.branch
    )


if __name__ == '__main__':
    main()
