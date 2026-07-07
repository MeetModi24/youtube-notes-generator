# Quick Reference: Work vs Personal Git

## ⚡ Before ANY Git Operation, Run This:

```bash
~/bin/git-check
```

This shows you:
- 📍 Which repository you're in
- 👤 Which name will be on commits
- 📧 Which email will be on commits  
- 🔗 Where your code will be pushed
- 🏢/🏠 Work or Personal indicator

---

## 🎯 Quick Decision Tree

### Where am I working?

**See 🏢 WORK repository?**
→ You're safe for Salesforce work  
→ Commits will show: mhiteshkumar@salesforce.com

**See 🏠 PERSONAL repository?**
→ You're safe for personal projects  
→ Commits will show: modimeet20@gmail.com

**See ❓ Unknown?**
→ STOP! Fix it first!

---

## 📋 Essential Commands

### Check Identity (Run First Always!)
```bash
~/bin/git-check
```

### Fix Wrong Identity
```bash
# For personal projects
git config user.name "Meet Modi"
git config user.email "modimeet20@gmail.com"

# For work projects
git config user.name "mhiteshkumar"
git config user.email "mhiteshkumar@salesforce.com"
```

### Safe Commit Workflow
```bash
# 1. Check identity
~/bin/git-check

# 2. If correct, commit
git add .
git commit -m "Your message"

# 3. Check again before push
~/bin/git-check

# 4. Push
git push
```

---

## 🔄 Repository Setup

### Personal Projects
```bash
cd ~/youtube-notes-generator  # Or any personal project

# Set identity
git config user.name "Meet Modi"
git config user.email "modimeet20@gmail.com"

# Verify
~/bin/git-check
```

### Work Projects
```bash
cd ~/your-work-project

# Set identity
git config user.name "mhiteshkumar"
git config user.email "mhiteshkumar@salesforce.com"

# Verify
~/bin/git-check
```

---

## 🚨 Emergency: I Committed to Wrong Account!

### Before Push (Easy Fix):
```bash
# 1. Fix identity
git config user.name "Meet Modi"
git config user.email "modimeet20@gmail.com"

# 2. Amend last commit
git commit --amend --reset-author --no-edit
```

### After Push (Requires Force Push):
```bash
# 1. Fix identity
git config user.name "Meet Modi"
git config user.email "modimeet20@gmail.com"

# 2. Amend commit
git commit --amend --reset-author --no-edit

# 3. Force push (CAREFUL!)
git push --force-with-lease
```

---

## 🎨 Visual Indicators

Add to your shell prompt - edit `~/.zshrc`:

```bash
# Add this function
git_repo_type() {
  if git rev-parse --is-inside-work-tree &>/dev/null 2>&1; then
    if git remote -v 2>/dev/null | grep -q "soma.salesforce"; then
      echo "🏢"
    elif git remote -v 2>/dev/null | grep -q "github.com"; then
      echo "🏠"
    fi
  fi
}

# Add to your prompt (find PROMPT= line and modify)
PROMPT='$(git_repo_type) '$PROMPT
```

After reload (`source ~/.zshrc`):
- Terminal shows: `🏢` when in work repos
- Terminal shows: `🏠` when in personal repos

---

## 📁 Recommended Directory Structure

```
~/
├── work-projects/           # All Salesforce work here
│   ├── project1/
│   └── project2/
│
└── personal-projects/       # All personal projects here
    ├── youtube-notes-generator/
    └── other-projects/
```

### Auto-Configure These Directories

```bash
# Create directories
mkdir -p ~/work-projects ~/personal-projects

# Auto-config for work projects
cat > ~/work-projects/.gitconfig << 'EOF'
[user]
  name = mhiteshkumar
  email = mhiteshkumar@salesforce.com
EOF

# Auto-config for personal projects
cat > ~/personal-projects/.gitconfig << 'EOF'
[user]
  name = Meet Modi
  email = modimeet20@gmail.com
EOF

# Add to global config
cat >> ~/.gitconfig << 'EOF'

[includeIf "gitdir:~/work-projects/"]
  path = ~/work-projects/.gitconfig

[includeIf "gitdir:~/personal-projects/"]
  path = ~/personal-projects/.gitconfig
EOF
```

Now any new repo in these folders automatically gets correct identity!

---

## 🎯 Golden Rules

1. **ALWAYS** run `~/bin/git-check` before commit/push
2. **NEVER** use global git config for user.name/email
3. **USE** different remote names: `origin` (work) vs `github` (personal)
4. **KEEP** projects in separate folders
5. **CHECK** the emoji: 🏢 vs 🏠

---

## 📞 Quick Help

### "Which account am I using right now?"
```bash
~/bin/git-check
```

### "Did I commit with wrong account?"
```bash
git log -1 --format="%an <%ae>"
```

### "Where will this push?"
```bash
git remote -v | grep push
```

### "Is this my current repo setup?"
```bash
~/bin/git-check
```

---

## ✅ Current Status

### ✅ Fixed:
- youtube-notes-generator → Personal (Meet Modi / modimeet20@gmail.com)
- Remote: github.com/MeetModi24

### ⚡ Next Steps:
1. Move to `~/personal-projects/youtube-notes-generator`
2. Always run `~/bin/git-check` before commits
3. Enjoy coding without worry! 🎉

---

**Remember: `~/bin/git-check` is your best friend!** 🎯
