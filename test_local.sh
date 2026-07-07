#!/bin/bash
# Test script for local version (DevBar/AWS Bedrock)

set -e

echo "================================================"
echo "YouTube Notes Generator - Local Version Test"
echo "================================================"
echo ""

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if Claude CLI is available
echo -e "${YELLOW}Checking Claude CLI...${NC}"
if command -v claude &> /dev/null; then
    echo -e "${GREEN}✓ Claude CLI found: $(which claude)${NC}"
    claude --version 2>/dev/null || echo "Claude CLI is accessible"
else
    echo -e "${RED}✗ Claude CLI not found in PATH${NC}"
    echo "Checking common locations..."

    if [ -f "$HOME/.devbar/bin/claude" ]; then
        echo -e "${GREEN}✓ Found at: $HOME/.devbar/bin/claude${NC}"
        echo "Add to PATH: export PATH=\"\$PATH:\$HOME/.devbar/bin\""
    else
        echo -e "${RED}Please ensure DevBar is installed and Claude CLI is accessible${NC}"
        exit 1
    fi
fi

echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo -e "${YELLOW}Creating virtual environment...${NC}"
    python3 -m venv venv
fi

# Activate virtual environment
echo -e "${GREEN}Activating virtual environment...${NC}"
source venv/bin/activate

# Install dependencies
echo -e "${GREEN}Installing dependencies (local version - no API key needed)...${NC}"
pip install -q -r requirements-local.txt

echo ""
echo "================================================"
echo "Setup complete! No API key required."
echo "================================================"
echo ""

# Create test repository
TEST_REPO="/tmp/youtube-notes-local-test"
echo -e "${GREEN}Creating test repository at: ${TEST_REPO}${NC}"
rm -rf "$TEST_REPO"
mkdir -p "$TEST_REPO"
cd "$TEST_REPO"
git init -q

# Return to tool directory
cd - > /dev/null

echo ""
echo "================================================"
echo "Testing with a short video"
echo "================================================"
echo ""

TEST_VIDEO="https://www.youtube.com/watch?v=kqtD5dpn9C8"

echo -e "${YELLOW}Processing video: ${TEST_VIDEO}${NC}"
echo "This uses your local Claude CLI (DevBar/AWS Bedrock)"
echo "May take 1-3 minutes..."
echo ""

python youtube_notes_local.py \
  --video "$TEST_VIDEO" \
  --repo-path "$TEST_REPO" \
  --output-dir "python-basics" \
  --no-commit

# Check output
if [ -d "$TEST_REPO/python-basics" ]; then
    echo ""
    echo -e "${GREEN}✓ Test PASSED${NC}"
    echo ""
    echo "Generated files:"
    find "$TEST_REPO/python-basics" -type f | head -10

    echo ""
    echo "================================================"
    echo "Sample Content Preview"
    echo "================================================"
    echo ""

    FIRST_README=$(find "$TEST_REPO/python-basics" -name "README.md" | head -1)
    if [ -f "$FIRST_README" ]; then
        echo "Preview of: $FIRST_README"
        echo "---"
        head -40 "$FIRST_README"
        echo "..."
        echo "(truncated)"
    fi

    echo ""
    echo "================================================"
    echo "✓ Local Version Test Complete!"
    echo "================================================"
    echo ""
    echo -e "${GREEN}✓ Successfully generated notes using local Claude CLI${NC}"
    echo -e "${GREEN}✓ No API key required${NC}"
    echo -e "${GREEN}✓ Uses your DevBar/AWS Bedrock setup${NC}"
    echo ""
    echo "Output location: $TEST_REPO/python-basics"
    echo ""
    echo "To use it yourself:"
    echo "  python youtube_notes_local.py \\"
    echo "    --video YOUR_VIDEO_URL \\"
    echo "    --repo-path ~/my-repo \\"
    echo "    --output-dir my-course"
    echo ""
else
    echo -e "${RED}✗ Test FAILED${NC}"
    echo "No output generated. Check errors above."
    exit 1
fi

echo -e "${YELLOW}Test repository: ${TEST_REPO}${NC}"
echo "To remove: rm -rf $TEST_REPO"
echo ""
