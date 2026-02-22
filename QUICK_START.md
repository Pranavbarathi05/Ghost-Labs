# 🚀 Quick Start Guide

## Directory Layout - Where to Work

```
Ghost-Labs/
│
├── 💻 WORK HERE - Main Development
│   ├── backend/           → Python/FastAPI backend code
│   ├── frontend/          → React/TypeScript frontend code
│   ├── ai-service/        → AI agent service code
│
├── 📚 READ THESE - Documentation  
│   ├── docs/              → Guides and API docs
│       ├── DIRECTORY_GUIDE.md   → Start here!
│       ├── GIT_WORKFLOW.md      → Git best practices
│       ├── API.md               → API documentation
│
├── ⚙️ CONFIG FILES - Usually don't modify
│   ├── docker-compose.yml       → Service orchestration
│   ├── .env.example            → Environment template
│   ├── .gitignore              → Git ignore rules
│
├── 📖 PROJECT DOCS - Read & follow
│   ├── README.md               → Main project readme
│   ├── CONTRIBUTING.md         → How to contribute
│   ├── CONTRIBUTORS.md         → Recognition
│
└── ⚠️  GITHUB CONFIG - Maintainers only
    └── .github/                → Templates & workflows
```

## 🎯 First Steps

### 1️⃣ Read This First
- [docs/DIRECTORY_GUIDE.md](docs/DIRECTORY_GUIDE.md) - Complete directory guide
- [README.md](README.md) - Project overview and setup

### 2️⃣ Setup Your Environment
```bash
# Clone and enter directory
cd Ghost-Labs

# Create your personal branch
git checkout -b your-name

# Copy environment file
cp .env.example .env

# Start development environment
docker-compose up --build
```

### 3️⃣ Start Coding

**Backend Development:**
```bash
cd backend/
# Add endpoints in: api/v1/
# Add models in: models/models.py
# Add schemas in: schemas/schemas.py
```

**Frontend Development:**
```bash
cd frontend/src/
# Add pages in: pages/
# Add components in: components/ (create this)
# Styles in: *.css files
```

### 4️⃣ Follow Git Workflow
- Read [docs/GIT_WORKFLOW.md](docs/GIT_WORKFLOW.md)
- Create feature branches: `your-name/feature-name`
- Commit often with clear messages
- Create PRs when ready

## ❓ Common Questions

**Q: Where do I add a new API endpoint?**  
A: `backend/api/v1/` - edit or create a new file

**Q: Where do I add a new page?**  
A: `frontend/src/pages/` - create a new `.tsx` file

**Q: How do imports work in backend?**  
A: Direct imports: `from models.models import User` (no `app.` prefix)

**Q: Can I modify .github/ files?**  
A: No, those are maintained by project leads

**Q: Where do I find documentation?**  
A: `docs/` directory - start with `DIRECTORY_GUIDE.md`

## 🆘 Need Help?

1. Check [docs/DIRECTORY_GUIDE.md](docs/DIRECTORY_GUIDE.md)
2. Read [CONTRIBUTING.md](CONTRIBUTING.md)
3. Ask in team chat or GitHub discussions
4. Open an issue with `question` label

## 🌐 Services & Ports

When running `docker-compose up`:

- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:8000
- **API Docs:** http://localhost:8000/docs
- **AI Service:** http://localhost:8001
- **PostgreSQL:** localhost:5432

Happy coding! 🎉
