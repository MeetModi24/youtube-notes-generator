# Git Account Management - Work vs Personal

## Quick Check: Which Account Am I Using?

### Before ANY commit, run this:

```bash
# Check current directory's git config
git config user.name
git config user.email

# Check which remote you're about to push to
git remote -v
```

**Expected outputs:**

**Work Repository (Salesforce):**
```
Name: mhiteshkumar
Email: mhiteshkumar@salesforce.com
Remote: git.soma.salesforce.com
```

**Personal Repository (GitHub.com):**
```
Name: Meet Modi (or MeetModi24)
Email: modimeet20@gmail.com
Remote: github.com
```

## Solution: Per-Repository Git Config

Instead of global config, set git user **per repository**:

### For Personal Projects (like youtube-notes-generator):

```bash
cd ~/youtube-notes-generator

# Set personal identity for THIS repo only
git config user.name "Meet Modi"
git config user.email "modimeet20@gmail.com"

# Verify
git config user.name
git config user.email
```

### For Work Projects:

```bash
cd ~/work-project

# Set work identity for THIS repo only
git config user.name "mhiteshkumar"
git config user.email "mhiteshkumar@salesforce.com"

# Verify
git config user.name
git config user.email
```

## Visual Cues in Your Shell

### Add to your `~/.zshrc` or `~/.bashrc`:

```bash
# Git prompt helper
git_identity() {
  if git rev-parse --is-inside-work-tree &>/dev/null; then
    local name=$(git config user.name)
    local email=$(git config user.email)
    local remote=$(git remote get-url origin 2>/dev/null || git remote get-url github 2>/dev/null || echo "no-remote")
    
    if [[ $remote == *"soma.salesforce"* ]]; then
      echo "🏢 WORK ($name)"
    elif [[ $remote == *"github.com"* ]]; then
      echo "🏠 PERSONAL ($name)"
    else
      echo "❓ UNKNOWN ($name)"
    fi
  fi
}

# Add to your prompt
PS1='$(git_identity) '$PS1
```

After adding, reload: `source ~/.zshrc`

Your terminal will show:
- `🏢 WORK (mhiteshkumar)` - When in work repos
- `🏠 PERSONAL (Meet Modi)` - When in personal repos

## Foolproof Workflow

### 1. Before Starting Work in ANY Repo:

```bash
# Step 1: Check where you are
pwd

# Step 2: Check git identity
git config user.name
git config user.email

# Step 3: Check remote
git remote -v

# Step 4: If wrong, fix it!
```

### 2. Safe Commit Checklist:

```bash
# ✅ ALWAYS run before committing:
echo "Repository: $(basename $(pwd))"
echo "Identity: $(git config user.name) <$(git config user.email)>"
echo "Remote: $(git remote -v | grep push)"
echo ""
read -p "Is this correct? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
  echo "❌ Aborting. Fix your config first!"
  exit 1
fi
```

Save this as `~/bin/git-check.sh` and run before commits:
```bash
source ~/bin/git-check.sh && git commit -m "your message"
```

## Directory-Based Auto Config

### Create separate directories:

```bash
# Work projects
mkdir -p ~/work-projects

# Personal projects  
mkdir -p ~/personal-projects
```

### Setup directory defaults:

**For ~/personal-projects/.gitconfig:**
```bash
cat > ~/personal-projects/.gitconfig << 'EOF'
[user]
  name = Meet Modi
  email = modimeet20@gmail.com
EOF
```

**For ~/work-projects/.gitconfig:**
```bash
cat > ~/work-projects/.gitconfig << 'EOF'
[user]
  name = mhiteshkumar
  email = mhiteshkumar@salesforce.com
EOF
```

**Update your global ~/.gitconfig:**
```bash
cat >> ~/.gitconfig << 'EOF'

[includeIf "gitdir:~/personal-projects/"]
  path = ~/personal-projects/.gitconfig

[includeIf "gitdir:~/work-projects/"]
  path = ~/work-projects/.gitconfig
EOF
```

Now:
- Any repo in `~/personal-projects/` automatically uses MeetModi24
- Any repo in `~/work-projects/` automatically uses mhiteshkumar

## Remote Names Convention

Always use different remote names:

**Work repos:**
```bash
origin → git.soma.salesforce.com
```

**Personal repos:**
```bash
github → github.com/MeetModi24
```

Check with: `git remote -v`

## Quick Commands Reference

### Check Current Setup:
```bash
# Who am I in this repo?
git config user.name && git config user.email

# Where does this push to?
git remote -v | grep push

# What's my last commit author?
git log -1 --format="%an <%ae>"
```

### Fix Wrong Identity:
```bash
# Set correct identity for THIS repo
git config user.name "Meet Modi"
git config user.email "modimeet20@gmail.com"

# Amend last commit with new author
git commit --amend --reset-author --no-edit
```

### Before Pushing:
```bash
# Double check everything
echo "Pushing as: $(git config user.name)"
echo "Pushing to: $(git remote get-url github || git remote get-url origin)"
read -p "Proceed? (y/n) " -n 1 -r
```

## GitHub CLI Commands

### Salesforce GitHub:
```bash
gh repo list                    # Lists Salesforce repos
gh pr create                    # Creates PR on Salesforce
```

### Personal GitHub:
```bash
GH_HOST=github.com gh repo list              # Lists personal repos  
GH_HOST=github.com gh pr create              # Creates PR on GitHub.com
```

## Safety Aliases

Add to `~/.zshrc` or `~/.bashrc`:

```bash
# Safe git push - always shows what you're doing
alias gp='echo "📤 Pushing as: $(git config user.name) <$(git config user.email)>" && echo "📤 Pushing to: $(git remote -v | grep push)" && git push'

# Safe git commit - always shows identity
alias gc='echo "✍️  Committing as: $(git config user.name) <$(git config user.email)>" && git commit'

# Check identity quickly
alias whoami-git='echo "Name: $(git config user.name)" && echo "Email: $(git config user.email)" && echo "Remote: $(git remote -v | grep push | head -1)"'
```

Then use:
- `whoami-git` - Check before working
- `gc -m "message"` - Safe commit
- `gp` - Safe push

## Emergency: Undo Wrong Commit

### If you committed with wrong author (before push):
```bash
# Fix identity
git config user.name "Meet Modi"
git config user.email "modimeet20@gmail.com"

# Rewrite last commit
git commit --amend --reset-author --no-edit

# Push (force if already pushed)
git push --force-with-lease
```

### If you pushed to wrong repo:
```bash
# Delete from wrong repo
git push origin :branch-name  # Deletes branch

# Push to correct repo
git push github branch-name
```

## Summary: Golden Rules

1. ✅ **Check before every commit:** `whoami-git`
2. ✅ **Use directory separation:** `~/work-projects/` vs `~/personal-projects/`
3. ✅ **Different remote names:** `origin` vs `github`
4. ✅ **Per-repo config:** Not global
5. ✅ **Visual indicators:** Shell prompt shows which account

---

**Remember:** When in doubt, run `whoami-git` first! 🎯
