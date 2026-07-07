# Setup Personal GitHub Account (Safe - Won't Affect Salesforce)

## Current Setup
✅ You have: `git.soma.salesforce.com` (Salesforce internal)  
➕ We'll add: `github.com` (Personal - MeetModi24)

**Both will work independently!**

## Method 1: Add GitHub.com via gh CLI (Recommended)

### Step 1: Login to GitHub.com

```bash
# This adds GitHub.com WITHOUT affecting git.soma
GH_HOST=github.com gh auth login
```

**Follow the prompts:**
1. What account do you want to log into? → **GitHub.com**
2. What is your preferred protocol? → **HTTPS** (or SSH if you prefer)
3. Authenticate Git with your GitHub credentials? → **Yes**
4. How would you like to authenticate? → **Login with a web browser**
5. Copy the one-time code shown
6. Press Enter to open browser
7. Login with your Google account (MeetModi24)
8. Paste the code
9. Authorize

### Step 2: Verify Both Accounts

```bash
# Check Salesforce account (should still work)
gh auth status

# Check GitHub.com account
GH_HOST=github.com gh auth status
```

You should see BOTH accounts listed!

## Method 2: Manual Setup via Personal Access Token

### Step 1: Create Token on GitHub.com

1. Login to **https://github.com** (with your Google/MeetModi24 account)
2. Go to: **https://github.com/settings/tokens/new**
3. Token name: `laptop-access`
4. Expiration: 90 days (or your preference)
5. Select scopes:
   - ✅ `repo` (all sub-options)
   - ✅ `workflow`
   - ✅ `gist`
6. Click **"Generate token"**
7. **Copy the token immediately** (starts with `ghp_...`)

### Step 2: Configure Git for GitHub.com

```bash
# Add GitHub.com credentials (won't touch Salesforce)
git config --global credential.https://github.com.helper store

# Test with a simple command (will prompt for credentials)
GH_HOST=github.com gh auth login --with-token < your_token_file
```

## Method 3: SSH Keys (Most Secure)

### Step 1: Generate SSH Key for GitHub.com

```bash
# Generate new SSH key (separate from Salesforce)
ssh-keygen -t ed25519 -C "your_email@gmail.com" -f ~/.ssh/id_ed25519_github

# Start ssh-agent
eval "$(ssh-agent -s)"

# Add key to agent
ssh-add ~/.ssh/id_ed25519_github
```

### Step 2: Add SSH Key to GitHub.com

```bash
# Copy public key
cat ~/.ssh/id_ed25519_github.pub
# Copy the output
```

1. Go to: **https://github.com/settings/keys**
2. Click **"New SSH key"**
3. Title: `MacBook - Personal`
4. Key type: **Authentication Key**
5. Paste your public key
6. Click **"Add SSH key"**

### Step 3: Test SSH Connection

```bash
# Test GitHub.com (should work)
ssh -T git@github.com

# Test Salesforce (should still work)
ssh -T git@git.soma.salesforce.com
```

### Step 4: Configure SSH Config

```bash
cat >> ~/.ssh/config << 'EOF'

# GitHub.com (Personal)
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_github
    IdentitiesOnly yes

# Salesforce GitHub (Work)
Host git.soma.salesforce.com
    HostName git.soma.salesforce.com
    User git
    IdentityFile ~/.ssh/id_rsa
    IdentitiesOnly yes
EOF
```

## Verify Everything Works

### Check Authentication Status

```bash
# Salesforce GitHub (should show your work account)
gh auth status

# Public GitHub (should show MeetModi24)
GH_HOST=github.com gh auth status
```

### Check Git Config

```bash
# Should show both configurations
git config --list | grep -E "github|soma"
```

## Now Create Your Repository!

### Option A: Via gh CLI

```bash
cd ~/youtube-notes-generator

# Create on GitHub.com (your personal account)
GH_HOST=github.com gh repo create youtube-notes-generator \
  --public \
  --source=. \
  --description="Transform YouTube videos into comprehensive learning notes" \
  --remote=github

# Push
git push -u github main
```

### Option B: Manually

1. Go to: **https://github.com/new**
2. Login with MeetModi24 (Google account)
3. Create repository: `youtube-notes-generator`
4. Don't initialize with any files

```bash
cd ~/youtube-notes-generator

# Add remote
git remote add github https://github.com/MeetModi24/youtube-notes-generator.git

# Or with SSH:
# git remote add github git@github.com:MeetModi24/youtube-notes-generator.git

# Push
git push -u github main
```

## Important: Keep Both Accounts Separate

### When using Salesforce GitHub:
```bash
# Default - uses git.soma
git push origin main
gh repo list  # Shows Salesforce repos
```

### When using Personal GitHub:
```bash
# Specify GitHub.com
git push github main
GH_HOST=github.com gh repo list  # Shows personal repos
```

## Safety Check

```bash
# Before any git operation, check which remote:
git remote -v

# You should see:
# github    https://github.com/MeetModi24/... (personal)
# origin    https://git.soma.salesforce.com/... (work)
```

## What WON'T Be Affected

✅ Your Salesforce GitHub access remains unchanged  
✅ Your work repositories are untouched  
✅ Your work SSH keys work as before  
✅ Your work gh CLI commands work as before  
✅ Your work Git credentials are separate  

## What Changes

✅ You can now use: `GH_HOST=github.com gh ...`  
✅ You can push to personal GitHub repos  
✅ You have a second remote called `github`  
✅ You can switch between work and personal easily  

## Quick Reference

| Action | Salesforce | Personal GitHub |
|--------|-----------|-----------------|
| Auth status | `gh auth status` | `GH_HOST=github.com gh auth status` |
| List repos | `gh repo list` | `GH_HOST=github.com gh repo list` |
| Create repo | `gh repo create` | `GH_HOST=github.com gh repo create` |
| Push code | `git push origin main` | `git push github main` |

## Troubleshooting

### "Permission denied"
→ Make sure you're authenticated: `GH_HOST=github.com gh auth status`

### "Repository not found"
→ Create the repo on GitHub.com first via web interface

### "Remote already exists"
→ `git remote remove github` then add again

## Ready to Proceed?

Once you're authenticated with GitHub.com, run:

```bash
# Verify you're logged in
GH_HOST=github.com gh auth status

# Create repository
cd ~/youtube-notes-generator
GH_HOST=github.com gh repo create youtube-notes-generator --public --source=. --remote=github --push
```

---

**Your Salesforce account is 100% safe and separate!** 🔒
