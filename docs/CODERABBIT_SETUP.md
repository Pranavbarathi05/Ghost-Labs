# 🤖 CodeRabbit Setup Guide

CodeRabbit is an AI-powered code review tool that helps maintain code quality and catches issues early.

## 📋 Setup Instructions

### 1. Install CodeRabbit App on GitHub

1. Go to the [CodeRabbit GitHub App](https://github.com/apps/coderabbitai)
2. Click **"Install"** or **"Configure"**
3. Select your organization or account
4. Choose **"Only select repositories"** and select `Ghost-Labs`
5. Click **"Install"** or **"Save"**

### 2. Verify Configuration

The repository already has CodeRabbit configured with:
- **Configuration file**: `.coderabbit.yaml`
- **GitHub integration**: `.github/coderabbit.yaml`

### 3. How It Works

Once installed, CodeRabbit will:

1. **Automatically review PRs** - Reviews code on every pull request
2. **Add comments** - Provides inline suggestions and feedback
3. **Create summaries** - Generates high-level summaries of changes
4. **Label PRs** - Auto-labels based on changed files
5. **Check quality** - Flags security, performance, and style issues

## 🎯 What CodeRabbit Reviews

### Backend (Python/FastAPI)
- ✅ Error handling and exception management
- ✅ SQLAlchemy query optimization (N+1 issues)
- ✅ Async/await patterns
- ✅ Security vulnerabilities (SQL injection, XSS)
- ✅ Input validation with Pydantic
- ✅ Proper logging practices
- ✅ Type hints usage

### Frontend (React/TypeScript)
- ✅ TypeScript type safety (avoids `any`)
- ✅ Error handling in async operations
- ✅ Accessibility (a11y) issues
- ✅ React hooks best practices
- ✅ Memory leak prevention
- ✅ Component architecture
- ✅ State management patterns

### General
- ✅ Code complexity and duplication
- ✅ Best practices compliance
- ✅ Documentation quality
- ✅ Test coverage

## 🔧 Configuration Details

### Review Profile
- **Mode**: Assertive (catches issues early)
- **Auto-review**: Enabled on push to PRs
- **Request changes**: Enabled for critical issues

### Path-Based Rules

Different rules apply to different parts of the codebase:

```yaml
backend/api/**/*.py     → API-specific checks
backend/tests/**/*.py   → Test quality checks
frontend/src/**/*.tsx   → Component and React checks
**/*.md                 → Documentation checks
```

### Labels Applied Automatically

- `backend` - Changes in backend/
- `frontend` - Changes in frontend/
- `documentation` - Changes to *.md files
- `tests` - Changes in test files
- `security` - Changes to auth/security files
- `database` - Changes to models/migrations

## 💬 Interacting with CodeRabbit

### In Pull Requests

**Ask questions:**
```
@coderabbitai Can you explain this suggestion?
@coderabbitai Is there a better way to implement this?
```

**Request specific reviews:**
```
@coderabbitai review security
@coderabbitai review performance
@coderabbitai review accessibility
```

**Resolve/dismiss comments:**
```
@coderabbitai resolve
@coderabbitai This is intentional because...
```

### Custom Review Prompts

Use these prompts in PR comments:

1. **Security Review**
   ```
   @coderabbitai security-review
   ```

2. **Performance Review**
   ```
   @coderabbitai performance-review
   ```

3. **Accessibility Review**
   ```
   @coderabbitai accessibility-review
   ```

## 📊 Review Statistics

CodeRabbit provides insights on:
- Issues found and fixed
- Code quality trends
- Common patterns
- Team productivity

Access these at: https://coderabbit.ai/dashboard

## ⚙️ Customizing Reviews

To customize CodeRabbit's behavior, edit `.coderabbit.yaml`:

```yaml
# Example: Change review aggressiveness
reviews:
  profile: chill  # or assertive, custom

# Example: Add custom path rules
path_instructions:
  - path: "your/path/**/*.py"
    instructions: "Your custom instructions"
```

## 🚫 Ignoring Files

Files already ignored:
- `node_modules/`, `venv/`, `__pycache__/`
- `dist/`, `build/`, `coverage/`
- Lock files, compiled files

To ignore additional paths, update `.coderabbit.yaml`:

```yaml
exclude:
  - "your/ignored/path/**"
```

## 🐛 Troubleshooting

### CodeRabbit Not Reviewing PRs

1. **Check installation**: Verify app is installed for this repo
2. **Check permissions**: Ensure app has read/write access
3. **Check branch**: Reviews only trigger on configured branches
4. **Check draft status**: Drafts may be excluded (configurable)

### Too Many/Few Comments

Adjust the review profile:
```yaml
reviews:
  profile: chill      # Fewer comments
  profile: assertive  # More comments
```

### False Positives

Dismiss specific comments:
```
@coderabbitai dismiss - This is intentional
```

Or update configuration to ignore specific patterns.

## 📚 Best Practices

1. **Address critical issues** - Fix security and bug issues immediately
2. **Discuss suggestions** - Engage with CodeRabbit's suggestions
3. **Update config** - Refine rules based on team preferences
4. **Learn patterns** - Use reviews as learning opportunities
5. **Don't auto-dismiss** - Consider all feedback carefully

## 🔗 Resources

- **CodeRabbit Docs**: https://docs.coderabbit.ai/
- **GitHub App**: https://github.com/apps/coderabbitai
- **Dashboard**: https://coderabbit.ai/dashboard
- **Support**: support@coderabbit.ai

## 📝 Configuration Files

- **Main config**: `.coderabbit.yaml` (root directory)
- **GitHub integration**: `.github/coderabbit.yaml`

## ✅ Checklist

After setup, verify:

- [ ] CodeRabbit app installed on GitHub
- [ ] `.coderabbit.yaml` exists in repository root
- [ ] Configuration matches team preferences
- [ ] Test PR shows CodeRabbit reviews
- [ ] Team members understand how to interact with it
- [ ] Labels are being applied correctly

---

**Setup Date**: February 22, 2026  
**Status**: Ready for use  
**Maintained by**: Ghost Labs Team
