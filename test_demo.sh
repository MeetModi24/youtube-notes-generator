#!/bin/bash
# Demo script to test the YouTube Notes Generator

set -e

echo "================================================"
echo "YouTube Notes Generator - Demo Test"
echo "================================================"
echo ""

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo -e "${YELLOW}Creating virtual environment...${NC}"
    python3 -m venv venv
fi

# Activate virtual environment
echo -e "${GREEN}Activating virtual environment...${NC}"
source venv/bin/activate

# Install dependencies
echo -e "${GREEN}Installing dependencies...${NC}"
pip install -q -r requirements.txt

# Check for .env file
if [ ! -f ".env" ]; then
    echo -e "${RED}Error: .env file not found${NC}"
    echo "Please copy .env.example to .env and add your ANTHROPIC_API_KEY"
    exit 1
fi

# Create test repository
TEST_REPO="/tmp/youtube-notes-test-repo"
echo -e "${GREEN}Creating test repository at: ${TEST_REPO}${NC}"
rm -rf "$TEST_REPO"
mkdir -p "$TEST_REPO"
cd "$TEST_REPO"
git init -q

# Return to tool directory
cd - > /dev/null

# Test 1: Process a single short video
echo ""
echo "================================================"
echo "Test 1: Processing a single video"
echo "================================================"
echo ""

# Using a short Python tutorial video
TEST_VIDEO="https://www.youtube.com/watch?v=kqtD5dpn9C8"

echo -e "${YELLOW}Processing video: ${TEST_VIDEO}${NC}"
echo "This may take 1-2 minutes..."
echo ""

python youtube_notes.py \
  --video "$TEST_VIDEO" \
  --repo-path "$TEST_REPO" \
  --output-dir "python-basics" \
  --style casual \
  --no-commit

# Check output
if [ -d "$TEST_REPO/python-basics" ]; then
    echo ""
    echo -e "${GREEN}✓ Test 1 PASSED${NC}"
    echo ""
    echo "Generated files:"
    find "$TEST_REPO/python-basics" -type f -name "*.md" -o -name "*.mmd" | head -10
else
    echo -e "${RED}✗ Test 1 FAILED${NC}"
    exit 1
fi

# Show sample content
echo ""
echo "================================================"
echo "Sample Content Preview"
echo "================================================"
echo ""

FIRST_README=$(find "$TEST_REPO/python-basics" -name "README.md" | head -1)
if [ -f "$FIRST_README" ]; then
    echo "Preview of: $FIRST_README"
    echo "---"
    head -30 "$FIRST_README"
    echo "..."
    echo "(truncated)"
fi

# Summary
echo ""
echo "================================================"
echo "Demo Complete!"
echo "================================================"
echo ""
echo -e "${GREEN}✓ Successfully generated notes${NC}"
echo ""
echo "Check the output at: $TEST_REPO/python-basics"
echo ""
echo "To view the notes:"
echo "  cd $TEST_REPO/python-basics"
echo "  cat 01-*/README.md"
echo ""
echo "To run your own test:"
echo "  python youtube_notes.py --video YOUR_VIDEO_URL --repo-path ~/my-repo --output-dir my-course"
echo ""

# Cleanup option
echo -e "${YELLOW}Test repository will remain at: ${TEST_REPO}${NC}"
echo "To remove it: rm -rf $TEST_REPO"
echo ""
