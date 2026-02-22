# 🚀 Ghost Labs

**Next-Generation Collaborative Development Platform with Persistent Linux Labs + AI Agent**


A cutting-edge platform where developers can collaborate in real-time with video calling, whiteboard brainstorming, and shared code editing - all while working in persistent Linux environments that save your progress. Perfect for pair programming, coding interviews, hackathons, and remote teaching.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

> **🚀 New to the project?** Start with [QUICK_START.md](QUICK_START.md) for a visual guide!
> **🏗️ Architecture Details:** Check [ARCHITECTURE.md](ARCHITECTURE.md)

---

## 🎯 Overview

Ghost Labs is a revolutionary collaborative development platform that combines the real-time features with powerful persistent workspace capabilities. Each user gets:

- 🎥 **High-quality video/audio calling** for pair programming
- 🎨 **Interactive whiteboard** for system design and brainstorming  
- 💻 **Real-time code editor** with syntax highlighting and IntelliSense
- 🖥️ **Persistent Linux workspaces** that save your progress
- 📸 **Workspace snapshots** to resume exactly where you left off
- 🤖 **AI-powered assistant** for coding help and explanations
- 👥 **Multi-user collaboration** with role-based permissions
- 🔒 **Enterprise-grade security** with encrypted communication

Perfect for **coding interviews**, **hackathons**, **remote teaching**, **code reviews**, and **team projects**.

---

## ✨ Features
- ✨ **Video/Audio Calling** - Agora SDK integration for crystal-clear communication
- ✨ **Whiteboard Collaboration** - Excalidraw for visual brainstorming
- ✨ **Real-time Code Editor** - Monaco Editor (VS Code's engine) with live sync
- ✨ **File Upload/Download** - Seamlessly transfer files to/from containers
- ✨ **Real-time Chat** - Text messaging alongside voice
- ✨ **Modular Architecture** - Clean component structure and service layers
- 💾 **Persistent Workspaces** - Containers that persist between sessions
- 📸 **Advanced Snapshots** - Save/restore entire workspace states
- 🤖 **AI Agent Integration** - Built-in coding assistant
- ⚡ **Terminal Access** - Full Linux terminal via xterm.js
- 🔧 **Package Management** - Customize container with dev tools
- 🔄 **Multiple Workspaces** - Up to 2 workspaces per room

### Real-Time Collaboration
- **Video/Audio Calling** - HD video and audio with Agora SDK
- **Screen Sharing** - Share your screen for presentations
- **Whiteboard** - Draw diagrams, flowcharts, and system designs
- **Code Editor** - Monaco Editor with real-time synchronization
- **Text Chat** - Instant messaging with file sharing
- **Presence Indicators** - See who's online and active

### Workspace Management
- **Persistent Linux Environments** - Your workspace saves automatically
- **Docker Containers** - Ubuntu/Debian/Kali Linux options
- **Snapshot/Restore** - Save workspace states and resume anytime
- **File Manager** - Upload/download files directly to containers
- **Package Selection** - Choose dev tools, editors, databases
- **Multiple Workspaces** - Create up to 2 workspaces per room

### Development Tools
- **Terminal Access** - Full bash terminal in your browser
- **Code Editor** - Syntax highlighting for 50+ languages
- **File Tree Navigation** - Browse container filesystem
- **AI Coding Assistant** - Get code suggestions and explanations
- **Version Control** - Git pre-installed in containers

### Security & Permissions
- **JWT Authentication** - Secure token-based auth
- **Role-Based Access** - Owner, Admin, Member, Viewer roles
- **Encrypted Communication** - All data encrypted in transit
- **Isolated Containers** - Each workspace is sandboxed
- **Cloudflare Tunnel** - Secure external access (optional)

---

## 🛠️ Tech Stack

### Frontend
- **React 18** + **TypeScript** - Modern UI framework
- **Vite** - Lightning-fast build tool
- **Tailwind CSS** - Utility-first CSS framework
- **Monaco Editor** - VS Code's editor engine
- **Excalidraw** - Collaborative whiteboard
- **Agora SDK** - Video/audio calling
- **xterm.js** - Terminal emulation
- **Socket.io Client** - Real-time communication
- **TanStack Query** - Data fetching and state management
- **Framer Motion** - Smooth animations

### Backend
- **FastAPI** - High-performance Python web framework
- **PostgreSQL** - Relational database for user data
- **Redis** - In-memory store for real-time features
- **SQLAlchemy** - ORM for database operations
- **WebSockets** - Bidirectional real-time communication
- **JWT** - Secure authentication tokens
- **Pydantic** - Data validation and settings management

### Infrastructure
- **Docker** - Container runtime for workspaces
- **Docker Compose** - Multi-container orchestration
- **Ubuntu/Debian/Kali** - Workspace container images
- **Cloudflare Tunnel** - Secure access (optional)
- **Nginx** - Reverse proxy (production)

### AI & Integration
- **OpenAI API** - GPT models for coding assistance
- **Anthropic Claude** - Alternative LLM option
- **Agora RTC** - Real-time communication platform

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

### Required
- **Git** - Version control
- **Docker** - Container runtime (20.10+)
- **Docker Compose** - Multi-container orchestration
- **Python** - 3.11 or higher
- **Node.js** - 20.x or higher
- **npm** - 10.x or higher

### Recommended
- **VS Code** - Code editor with Docker extension
- **PostgreSQL Client** - For database management (optional)
- **Postman/Insomnia** - API testing (optional)

### Verify Installation
```bash
git --version
docker --version
docker-compose --version
python --version
node --version
npm --version
```

---

## 🚀 Quick Start

### Option 1: Docker Compose (Recommended)

```bash
# Clone the repository
git clone https://github.com/Pranavbarathi05/Ghost-Labs.git
cd Ghost-Labs

# Copy environment files
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env

# Edit with your credentials (Agora, OpenAI, etc.)
nano backend/.env
nano frontend/.env

# Start all services
docker-compose up --build

# Access the application
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

### Option 2: Local Development

**Backend:**
```bash
cd backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# or: venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Copy and edit environment file
cp .env.example .env
nano .env

# Run backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Frontend:**
```bash
cd frontend

# Install dependencies
npm install

# Copy and edit environment file
cp .env.example .env
nano .env

# Run frontend
npm run dev
```

**Services:**
```bash
# Start PostgreSQL and Redis
docker-compose up -d db redis
```

### Get API Keys

#### Agora (Video/Audio)
1. Sign up at https://www.agora.io/
2. Create a project
3. Copy **App ID** and **App Certificate**
4. Add to `backend/.env` and `frontend/.env`

#### OpenAI (AI Assistant) - Optional
1. Get API key from https://platform.openai.com/
2. Add to `backend/.env`

### 4. Access the Application

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [QUICK_START.md](QUICK_START.md) | Visual quick start guide for contributors |
| [ARCHITECTURE.md](ARCHITECTURE.md) | Complete architecture and structure |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to contribute to the project |
| [docs/GIT_WORKFLOW.md](docs/GIT_WORKFLOW.md) | Git workflow and best practices |
| [docs/DIRECTORY_GUIDE.md](docs/DIRECTORY_GUIDE.md) | Directory structure explained |
| [docs/API.md](docs/API.md) | API endpoint documentation |
| [docs/CONFIGURATION.md](docs/CONFIGURATION.md) | Environment configuration guide |
| [docs/CODERABBIT_SETUP.md](docs/CODERABBIT_SETUP.md) | AI code review setup |
| [INITIAL_ISSUES.md](INITIAL_ISSUES.md) | Beginner-friendly starter tasks |

---

## 🎯 Use Cases

### 1. Coding Interviews
- Video call with candidate
- Share whiteboard for system design
- Code together in Monaco editor
- Review code in real-time
- Save workspace for later review

### 2. Pair Programming
- Work together on the same codebase
- Video/audio for communication
- Screen sharing for debugging
- Persistent workspace saves progress

### 3. Hackathons
- Quick team setup with rooms
- Multiple workspaces for different services
- Whiteboard for planning
- File sharing for assets

### 4. Remote Teaching
- Teach Linux commands in real terminal
- Show code examples in editor
- Draw diagrams on whiteboard
- Students can follow along in their workspace

### 5. Code Reviews
- Review code together with video
- Discuss architecture on whiteboard
- Test changes in live environment
- Leave comments in chat

---

## 🤝 Contributing

We welcome contributions! Here's how to get started:

### For Beginners
1. Check [INITIAL_ISSUES.md](INITIAL_ISSUES.md) for beginner-friendly tasks
2. Read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines
3. Follow [docs/GIT_WORKFLOW.md](docs/GIT_WORKFLOW.md) for Git best practices

### For Experienced Contributors
1. Review [ARCHITECTURE.md](ARCHITECTURE.md) for architecture details
2. Check [INITIAL_ISSUES.md](INITIAL_ISSUES.md) for implementation tasks
3. Set up [docs/CODERABBIT_SETUP.md](docs/CODERABBIT_SETUP.md) for AI code review

### Development Workflow
```bash
# Create your feature branch
git checkout -b your-name/feature-description

# Make your changes
# Test thoroughly

# Commit with clear messages
git commit -m "feat: add video calling feature"

# Push to your branch
git push origin your-name/feature-description

# Create a Pull Request on GitHub
```

---

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest tests/ -v --cov=.
```

### Frontend Tests
```bash
cd frontend
npm run test
```

### Integration Tests
```bash
docker-compose up -d
# Run integration test suite
```

---

## 🚀 Deployment

### Production Deployment
See detailed guide in `docs/DEPLOYMENT.md` (coming soon)

### Quick Deploy with Docker
```bash
# Build production images
docker-compose -f docker-compose.prod.yml build

# Start services
docker-compose -f docker-compose.prod.yml up -d

# Check logs
docker-compose logs -f
```

---

## 🛠️ Troubleshooting

### Common Issues

**Q: Redis connection failed**
```bash
# Ensure Redis is running
docker-compose up -d redis
redis-cli ping  # Should return PONG
```

**Q: Port already in use**
```bash
# Find process using port 8000
lsof -i :8000
# Kill process or change port in .env
```

**Q: Frontend can't connect to backend**
```bash
# Check VITE_API_URL in frontend/.env
# Should be http://localhost:8000
```

**Q: Video calling not working**
```bash
# Verify Agora credentials in .env
# Check browser console for errors
# Ensure HTTPS or localhost (required by browsers)
```

For more troubleshooting, check the API documentation at http://localhost:8000/docs

---

## 📊 Project Status

- **Version**: 1.0.0
- **Status**: Active Development
- **License**: MIT (see LICENSE)

### Roadmap
- [x] Basic authentication and rooms
- [x] Docker workspace management
- [x] Snapshot system
- [x] Real-time chat
- [ ] Video/audio calling
- [ ] Whiteboard collaboration
- [ ] Code editor sync
- [ ] File upload/download
- [ ] Mobile app
- [ ] VS Code extension
- [ ] Advanced AI features
- [ ] Kubernetes deployment

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📧 Contact

- **Project Lead**: Pranav Barathi
- **GitHub**: [@Pranavbarathi05](https://github.com/Pranavbarathi05)
- **Issues**: [GitHub Issues](https://github.com/Pranavbarathi05/Ghost-Labs/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Pranavbarathi05/Ghost-Labs/discussions)

---

## ⭐ Show Your Support

If you find Ghost Labs useful, please consider:
- ⭐ Starring the repository
- 🍴 Forking and contributing
- 📢 Sharing with your network
- 🐛 Reporting bugs
- 💡 Suggesting features

---

**Built with ❤️ by the Ghost Labs Team**

*Empowering developers to collaborate anywhere, anytime.*

**Note**: Your team member will handle PostgreSQL setup. Once configured, the connection details should be added to `.env`.

Default configuration (for local development):
```
DATABASE_URL=postgresql://postgres:postgres@db:5432/ghostlabs
```

### 4. Start the Application

```bash
# Build and start all services
docker-compose up --build

# Or run in detached mode
docker-compose up -d --build
```

This will start:
- **Frontend** - http://localhost:3000
- **Backend API** - http://localhost:8000
- **AI Service** - http://localhost:8001
- **PostgreSQL** - localhost:5432

### 5. Verify Services

Open your browser and check:
- Frontend: http://localhost:3000
- Backend API Docs: http://localhost:8000/docs
- AI Service Docs: http://localhost:8001/docs

### 6. Stop Services

```bash
# Stop all services
docker-compose down

# Stop and remove volumes (clean slate)
docker-compose down -v
```

---

## 📁 Project Structure

> **🎯 New to the project?** Check out [docs/DIRECTORY_GUIDE.md](docs/DIRECTORY_GUIDE.md) for a detailed guide on where to work!

### Quick Overview

- **`backend/`** - Work here for API development (Python/FastAPI)
- **`frontend/`** - Work here for UI development (React/TypeScript)
- **`ai-service/`** - Work here for AI features
- **`docs/`** - Read documentation here
- **`.github/`** - GitHub templates (don't modify)

### Detailed Structure

```
Ghost-Labs/
├── backend/                # FastAPI backend (WORK HERE)
│   ├── api/v1/            # API endpoints
│   │   ├── auth.py        # Authentication endpoints
│   │   ├── rooms.py       # Room management
│   │   ├── users.py       # User management
│   │   └── workspaces.py  # Workspace endpoints
│   ├── core/              # Core functionality
│   │   ├── config.py      # Configuration
│   │   └── security.py    # Security & auth
│   ├── db/                # Database
│   │   └── database.py    # DB connection
│   ├── models/            # Database models
│   │   └── models.py      # SQLAlchemy models
│   ├── schemas/           # API schemas
│   │   └── schemas.py     # Pydantic schemas
│   ├── services/          # Business logic
│   │   └── docker_service.py
│   ├── websocket/         # Real-time communication
│   │   └── connection_manager.py
│   ├── main.py            # Application entry point
│   ├── requirements.txt   # Python dependencies
│   └── Dockerfile
│
├── frontend/              # React frontend (WORK HERE)
│   ├── src/
│   │   ├── pages/        # Page components
│   │   │   ├── HomePage.tsx
│   │   │   ├── LoginPage.tsx
│   │   │   ├── RegisterPage.tsx
│   │   │   ├── DashboardPage.tsx
│   │   │   ├── RoomPage.tsx
│   │   │   └── WorkspacePage.tsx
│   │   ├── App.tsx       # Main app component
│   │   ├── App.css       # App styles
│   │   ├── main.tsx      # Entry point
│   │   └── index.css     # Global styles
│   ├── index.html
│   ├── package.json
│   ├── vite.config.ts
│   ├── tsconfig.json
│   └── Dockerfile
│
├── ai-service/           # AI agent service (WORK HERE)
│   ├── main.py           # AI service entry point
│   ├── requirements.txt  # Python dependencies
│   └── Dockerfile
│
├── docs/                 # Documentation (READ ONLY)
│   ├── API.md           # API documentation
│   └── GIT_WORKFLOW.md  # Git workflow guide
│
├── .github/             # GitHub config (DON'T MODIFY)
│   ├── ISSUE_TEMPLATE/  # Issue templates
│   └── pull_request_template.md
│
├── docker-compose.yml   # Service orchestration
├── .env.example         # Environment template
├── .gitignore
├── CONTRIBUTING.md
├── CONTRIBUTORS.md
├── LICENSE
└── README.md
```

---

## 💻 Development Workflow

### Branching Strategy

We follow a **feature branch workflow** for clean, organized development:

#### 1. Create Your Personal Branch

```bash
# Create and switch to your branch
git checkout -b <your-name>

# Example:
git checkout -b pranav
git checkout -b yashas
```

#### 2. Create Feature Branches

For each feature/task, create a branch from your personal branch:

```bash
# Make sure you're on your personal branch
git checkout <your-name>

# Create feature branch
git checkout -b <your-name>/<feature-name>

# Examples:
git checkout -b pranav/user-authentication
git checkout -b yashas/workspace-snapshots
```

#### 3. Make Your Changes

```bash
# Check status
git status

# Add changes
git add .

# Commit with descriptive message
git commit -m "feat: Add user authentication with JWT"
```

#### Commit Message Format

Follow **Conventional Commits** for clarity:

- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting, etc.)
- `refactor:` - Code refactoring
- `test:` - Adding or updating tests
- `chore:` - Maintenance tasks

Examples:
```bash
git commit -m "feat: Add WebSocket chat functionality"
git commit -m "fix: Resolve database connection timeout"
git commit -m "docs: Update API documentation"
git commit -m "refactor: Improve Docker service error handling"
```

#### 4. Push Your Changes

```bash
# Push feature branch to remote
git push origin <your-name>/<feature-name>

# Example:
git push origin pranav/user-authentication
```

#### 5. Create Pull Request

1. Go to GitHub repository
2. Click "Pull Requests" → "New Pull Request"
3. Select your feature branch
4. Fill in the PR template:
   - **Title**: Brief description of changes
   - **Description**: Detailed explanation
   - **Related Issues**: Link any related issues
   - **Screenshots**: If applicable
5. Request review from team members
6. Wait for approval before merging

#### 6. Merge and Clean Up

Once your PR is approved:

```bash
# Switch to main branch
git checkout main

# Pull latest changes
git pull origin main

# Delete local feature branch (optional)
git branch -d <your-name>/<feature-name>

# Update your personal branch
git checkout <your-name>
git merge main
```

### Code Review Guidelines

When reviewing PRs:
- ✅ Check code quality and style
- ✅ Test functionality locally
- ✅ Verify documentation is updated
- ✅ Ensure no merge conflicts
- ✅ Provide constructive feedback

---

## 🤝 Contributing Guidelines

### How to Contribute

1. **Find an Issue**: Check the [Issues](https://github.com/Pranavbarathi05/Ghost-Labs/issues) page
2. **Assign Yourself**: Comment on the issue to claim it
3. **Create Branch**: Follow the branching strategy above
4. **Make Changes**: Write clean, documented code
5. **Test**: Ensure your changes work as expected
6. **Submit PR**: Create a pull request with detailed description

### Code Standards

#### Python (Backend)
- Follow **PEP 8** style guide
- Use type hints
- Write docstrings for functions/classes
- Keep functions small and focused
- Handle errors gracefully

```python
def create_workspace(user_id: int, name: str) -> Workspace:
    """
    Create a new workspace for a user.
    
    Args:
        user_id: The ID of the workspace owner
        name: Name of the workspace
        
    Returns:
        Workspace: The created workspace object
        
    Raises:
        ValueError: If name is invalid
    """
    # Implementation
```

#### TypeScript/React (Frontend)
- Use **functional components** with hooks
- Follow **ESLint** rules
- Use TypeScript for type safety
- Keep components small and reusable
- Use meaningful variable names

```typescript
interface WorkspaceProps {
  id: number;
  name: string;
  status: 'running' | 'stopped';
}

const WorkspaceCard: React.FC<WorkspaceProps> = ({ id, name, status }) => {
  // Implementation
};
```

#### General
- Write self-documenting code
- Add comments for complex logic
- Update documentation with changes
- Write tests when possible
- Keep commits atomic and focused

---

## 🐛 Issue Management

### Creating Issues

When creating a new issue, use the appropriate template:

#### Bug Report Template

```markdown
## Bug Description
Clear and concise description of the bug.

## Steps to Reproduce
1. Go to '...'
2. Click on '...'
3. Scroll down to '...'
4. See error

## Expected Behavior
What should happen.

## Actual Behavior
What actually happens.

## Environment
- OS: [e.g., Ubuntu 22.04]
- Browser: [e.g., Chrome 120]
- Docker Version: [e.g., 24.0.0]

## Screenshots
If applicable, add screenshots.

## Additional Context
Any other relevant information.
```

#### Feature Request Template

```markdown
## Feature Description
Clear description of the proposed feature.

## Problem it Solves
What problem does this feature address?

## Proposed Solution
How should this feature work?

## Alternatives Considered
Other solutions you've thought about.

## Additional Context
Any mockups, diagrams, or references.
```

### Issue Labels

We use the following labels:

- `bug` - Something isn't working
- `feature` - New feature or request
- `enhancement` - Improvement to existing feature
- `documentation` - Documentation updates
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention needed
- `priority: high` - High priority
- `priority: medium` - Medium priority
- `priority: low` - Low priority
- `in progress` - Currently being worked on
- `blocked` - Blocked by another issue

### Tackling Issues

1. **Choose an Issue**: Browse open issues, prefer `good first issue` for beginners
2. **Comment**: Let others know you're working on it
3. **Assign Yourself**: Or ask a maintainer to assign you
4. **Create Branch**: `git checkout -b <your-name>/issue-<number>-<description>`
5. **Work on Solution**: Follow coding standards
6. **Reference Issue**: In commit messages: `fix: Resolve #123 - Fix login error`
7. **Create PR**: Link the issue in your PR description

---

## 💡 Feature Proposals

### Proposing New Features

We welcome innovative ideas! Here's how to propose features:

#### 1. Check Existing Issues
Search to see if someone already proposed it.

#### 2. Create a Discussion (Optional)
For major features, start a discussion first to get feedback.

#### 3. Submit Feature Request
Use the feature request template.

#### 4. Wait for Feedback
Maintainers and community will discuss feasibility.

#### 5. Get Approval
Once approved, it will be labeled and prioritized.

#### 6. Implementation
You can volunteer to implement it or others may pick it up.

### Feature Evaluation Criteria

Features are evaluated based on:
- **Alignment**: Does it fit the project vision?
- **Value**: How many users will benefit?
- **Feasibility**: Is it technically achievable?
- **Maintenance**: What's the ongoing maintenance cost?
- **Complexity**: How complex is the implementation?

### Architecture Decisions

For major architectural changes:
1. Create an **Architecture Decision Record (ADR)**
2. Document the decision in `docs/adr/`
3. Include:
   - Context and problem statement
   - Considered options
   - Decision and rationale
   - Consequences

---

## 📚 Additional Resources

### Documentation
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [Docker Documentation](https://docs.docker.com/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

### Learning Resources
- [Docker for Beginners](https://docker-curriculum.com/)
- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [React TypeScript Cheatsheet](https://react-typescript-cheatsheet.netlify.app/)
- [Git Branching Strategy](https://www.atlassian.com/git/tutorials/comparing-workflows)

### Project Communication
- **Issues**: Technical problems and bugs
- **Discussions**: General questions and ideas
- **Pull Requests**: Code review and feedback

---

## 🔧 Troubleshooting

### Common Issues

#### Docker Build Fails
```bash
# Clean Docker cache
docker system prune -a

# Rebuild without cache
docker-compose build --no-cache
```

#### Database Connection Error
```bash
# Check if PostgreSQL is running
docker-compose ps

# View database logs
docker-compose logs db

# Reset database
docker-compose down -v
docker-compose up -d db
```

#### Port Already in Use
```bash
# Find process using port
lsof -i :8000  # or :3000, :5432

# Kill the process
kill -9 <PID>
```

#### Frontend Not Loading
```bash
# Clear node_modules and reinstall
cd frontend
rm -rf node_modules package-lock.json
npm install
```

---

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest
```

### Frontend Tests
```bash
cd frontend
npm test
```

### Integration Tests
```bash
# Run all tests
docker-compose -f docker-compose.test.yml up
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 Team

- **Project Lead**: Pranav Barathi
- **Contributors**: See [CONTRIBUTORS.md](CONTRIBUTORS.md)

---

## 🙏 Acknowledgments

- Thanks to all contributors who help improve Ghost Labs
- Inspired by the need for secure, collaborative development environments
- Built with ❤️ for students and developers

---

## 📞 Support

If you encounter issues or have questions:

1. Check the [Troubleshooting](#troubleshooting) section
2. Search [existing issues](https://github.com/YOUR_USERNAME/Ghost-Labs/issues)
3. Create a new issue with detailed information
4. Join our community discussions

---

**Happy Coding! 🚀**
Secure zero-trust collaboration with containerized Linux labs, snapshot restore, remote desktop, and MCP-powered AI coding agent.
