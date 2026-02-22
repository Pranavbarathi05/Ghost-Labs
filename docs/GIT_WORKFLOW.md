# Git Workflow Guide for Ghost Labs

This guide explains the Git workflow used in Ghost Labs, designed to help students learn professional development practices.

## Overview

We use a **Feature Branch Workflow** which is widely adopted in the industry. This workflow ensures:
- Clean, organized codebase
- Easy code review process
- Reduced merge conflicts
- Clear history of changes
- Safe experimentation

## Branch Structure

```
main (production-ready code)
  ├── pranav (personal branch)
  │   ├── pranav/user-auth (feature branch)
  │   └── pranav/docker-setup (feature branch)
  │
  └── alice (personal branch)
      ├── alice/chat-feature (feature branch)
      └── alice/workspace-ui (feature branch)
```

## Initial Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Ghost-Labs.git
cd Ghost-Labs
```

### 2. Create Your Personal Branch

```bash
# Replace <your-name> with your actual name (lowercase, no spaces)
git checkout -b <your-name>

# Example:
git checkout -b pranav

# Push your personal branch to remote
git push -u origin <your-name>
```

**Important**: Your personal branch acts as your main workspace. Create feature branches from here.

## Daily Workflow

### Starting a New Feature

```bash
# 1. Make sure you're on your personal branch
git checkout <your-name>

# 2. Pull latest changes from main
git pull origin main

# 3. Create a feature branch
git checkout -b <your-name>/<feature-description>

# Examples:
git checkout -b pranav/user-authentication
git checkout -b alice/websocket-chat
git checkout -b bob/docker-optimization
```

### Making Changes

```bash
# 1. Check what files you've changed
git status

# 2. View specific changes
git diff

# 3. Stage specific files
git add path/to/file1.py path/to/file2.ts

# Or stage all changes
git add .

# 4. Commit with a descriptive message
git commit -m "feat: Add JWT authentication for user login"

# 5. Push to your feature branch
git push origin <your-name>/<feature-name>
```

### Commit Message Convention

Follow the **Conventional Commits** specification:

#### Format
```
<type>(<scope>): <subject>

<body>

<footer>
```

#### Types
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation only changes
- `style:` - Code style (formatting, missing semi-colons, etc.)
- `refactor:` - Code refactoring without changing functionality
- `perf:` - Performance improvements
- `test:` - Adding or updating tests
- `chore:` - Maintenance tasks (dependencies, build config, etc.)
- `ci:` - CI/CD changes

#### Examples

```bash
# Simple commit
git commit -m "feat: Add user registration endpoint"

# With scope
git commit -m "fix(auth): Resolve token expiration issue"

# With body
git commit -m "feat: Add WebSocket connection manager

Implemented a connection manager class to handle WebSocket
connections across multiple rooms with proper cleanup."

# Breaking change
git commit -m "feat!: Change API authentication to OAuth2

BREAKING CHANGE: JWT tokens are no longer supported"
```

### Creating a Pull Request

#### 1. Push Your Feature Branch

```bash
git push origin <your-name>/<feature-name>
```

#### 2. Open PR on GitHub

1. Go to the repository on GitHub
2. Click "Pull Requests" tab
3. Click "New Pull Request"
4. Select:
   - **Base**: `main`
   - **Compare**: `<your-name>/<feature-name>`
5. Fill in the PR template
6. Click "Create Pull Request"

#### 3. PR Best Practices

**Title Format:**
```
[Type] Brief description of changes

Examples:
[Feature] Add user authentication with JWT
[Fix] Resolve WebSocket disconnection issue
[Docs] Update API documentation
```

**Description Should Include:**
- What changes were made
- Why the changes were necessary
- How to test the changes
- Screenshots (if UI changes)
- Related issues (e.g., "Fixes #42")

#### 4. Code Review

- Wait for at least one team member to review
- Address feedback promptly
- Make requested changes in new commits
- Don't force push after review (unless requested)
- Engage in constructive discussion

#### 5. Merging

Once approved:
- A maintainer will merge the PR
- Or you can merge if you have permissions
- Delete the feature branch after merging

## Keeping Your Branch Updated

### Update from Main

```bash
# Switch to your personal branch
git checkout <your-name>

# Fetch latest changes
git fetch origin

# Merge main into your branch
git merge origin/main

# Or use rebase for cleaner history
git rebase origin/main

# Push updated branch
git push origin <your-name>
```

### Update Feature Branch

```bash
# Switch to feature branch
git checkout <your-name>/<feature-name>

# Merge your personal branch
git merge <your-name>

# Or merge main directly
git merge origin/main

# Resolve conflicts if any (see below)

# Push updates
git push origin <your-name>/<feature-name>
```

## Handling Merge Conflicts

Conflicts occur when the same file is edited in different branches.

### Resolving Conflicts

```bash
# 1. Try to merge or rebase
git merge origin/main
# or
git rebase origin/main

# 2. Git will tell you which files have conflicts
# Example output:
# CONFLICT (content): Merge conflict in backend/main.py

# 3. Open conflicted files in your editor
# Look for conflict markers:
# <<<<<<< HEAD
# Your changes
# =======
# Changes from main
# >>>>>>> origin/main

# 4. Edit the file to resolve conflicts
# Remove conflict markers and keep the correct code

# 5. Stage resolved files
git add backend/main.py

# 6. Complete the merge
git commit -m "merge: Resolve conflicts with main"

# 7. Push changes
git push origin <your-name>/<feature-name>
```

### Avoiding Conflicts

- Pull changes from main frequently
- Coordinate with team on file ownership
- Keep features small and focused
- Communicate about overlapping work

## Advanced Git Commands

### Viewing History

```bash
# View commit history
git log

# One line per commit
git log --oneline

# With graph
git log --oneline --graph --all

# Specific file history
git log --follow path/to/file
```

### Undoing Changes

```bash
# Unstage a file (keep changes)
git reset HEAD file.py

# Discard local changes
git checkout -- file.py

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1

# Create a new commit that undoes a previous commit
git revert <commit-hash>
```

### Stashing Changes

```bash
# Save changes without committing
git stash

# List stashed changes
git stash list

# Apply most recent stash
git stash apply

# Apply and remove stash
git stash pop

# Stash with a message
git stash save "WIP: Working on auth feature"
```

### Interactive Rebase

Clean up commits before pushing:

```bash
# Rebase last 3 commits
git rebase -i HEAD~3

# Options in the editor:
# pick = keep commit
# reword = change commit message
# squash = combine with previous commit
# drop = remove commit
```

## Common Scenarios

### Scenario 1: Forgot to Create Feature Branch

```bash
# You made changes on personal branch
git stash
git checkout -b <your-name>/<feature-name>
git stash pop
git add .
git commit -m "feat: Your changes"
git push origin <your-name>/<feature-name>
```

### Scenario 2: Need to Switch Branches with Uncommitted Changes

```bash
# Option 1: Commit your changes
git add .
git commit -m "WIP: Temporary commit"
git checkout other-branch

# Option 2: Stash your changes
git stash
git checkout other-branch
# Later, go back and apply stash
git checkout original-branch
git stash pop
```

### Scenario 3: Accidentally Committed to Wrong Branch

```bash
# Copy the commit hash
git log

# Switch to correct branch
git checkout <correct-branch>

# Cherry-pick the commit
git cherry-pick <commit-hash>

# Go back to wrong branch
git checkout <wrong-branch>

# Remove the commit
git reset --hard HEAD~1
```

### Scenario 4: Need to Update PR After Review

```bash
# Make requested changes
# ... edit files ...

# Stage and commit
git add .
git commit -m "fix: Address review comments"

# Push to same branch
git push origin <your-name>/<feature-name>

# PR will automatically update
```

## Git Aliases (Optional)

Make Git easier with aliases:

```bash
# Add to ~/.gitconfig
[alias]
    st = status
    co = checkout
    br = branch
    cm = commit -m
    last = log -1 HEAD
    unstage = reset HEAD --
    visual = log --oneline --graph --all --decorate
    amend = commit --amend --no-edit
```

Usage:
```bash
git st              # instead of git status
git co main         # instead of git checkout main
git cm "message"    # instead of git commit -m "message"
```

## Best Practices Summary

1. **Always create feature branches** - Never commit directly to main
2. **Pull before you push** - Stay updated with latest changes
3. **Write meaningful commit messages** - Future you will thank present you
4. **Commit frequently** - Small, logical commits are easier to review
5. **Keep features small** - Easier to review and less likely to conflict
6. **Test before pushing** - Make sure your code works
7. **Review your own code first** - Check your changes before creating PR
8. **Be responsive to reviews** - Address feedback promptly
9. **Delete merged branches** - Keep repository clean
10. **Ask for help** - Don't struggle alone, reach out to the team

## Troubleshooting

### "Your branch is behind 'origin/main'"

```bash
git pull origin main
```

### "Your branch and 'origin/branch' have diverged"

```bash
# If you haven't pushed commits that others need
git pull --rebase origin <branch-name>

# If you have pushed and others might have pulled
git pull origin <branch-name>
```

### "Permission denied" when pushing

```bash
# Check remote URL
git remote -v

# Should use SSH
git remote set-url origin git@github.com:USERNAME/Ghost-Labs.git

# Or HTTPS
git remote set-url origin https://github.com/USERNAME/Ghost-Labs.git
```

### Need to change last commit message

```bash
# If not yet pushed
git commit --amend

# If already pushed (avoid if possible)
git commit --amend
git push --force-with-lease origin <branch-name>
```

## Resources

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Git Branching Tutorial](https://learngitbranching.js.org/)
- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials)

## Questions?

If you're stuck or unsure about something:
1. Check this guide
2. Ask in team chat
3. Create a discussion on GitHub
4. Reach out to a maintainer

Happy collaborating! 🚀
