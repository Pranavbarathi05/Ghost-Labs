# 📂 Directory Guide for Contributors

This guide explains the simplified project structure and where you should work.

## 🎯 Quick Reference

### ✅ Work in These Directories

| Directory | Purpose | What to Do Here |
|-----------|---------|-----------------|
| **`backend/`** | Python FastAPI backend | Add API endpoints, database models, business logic |
| **`frontend/`** | React TypeScript frontend | Create UI components, pages, styles |
| **`ai-service/`** | AI agent service | Implement AI features, LLM integration |

### 📖 Read These Directories

| Directory | Purpose | What to Do |
|-----------|---------|------------|
| **`docs/`** | Documentation | Read guides, API docs, workflow instructions |

### 🚫 Don't Modify These

| Directory/File | Purpose | Why Not to Touch |
|----------------|---------|------------------|
| **`.github/`** | GitHub templates & workflows | Managed by maintainers |
| **`docker-compose.yml`** | Service orchestration | Configuration managed centrally |
| **`.gitignore`** | Git ignore rules | Project-wide settings |
| **`CONTRIBUTING.md`** | Contribution guidelines | Official project policies |

---

## 📁 Detailed Structure

### Backend Directory (`backend/`)

```
backend/
├── api/v1/              ← Add new API endpoints here
│   ├── auth.py         # Authentication endpoints
│   ├── rooms.py        # Room management
│   ├── users.py        # User management
│   └── workspaces.py   # Workspace management
│
├── core/               ← Core utilities
│   ├── config.py       # App configuration
│   └── security.py     # Security & JWT functions
│
├── db/                 ← Database setup
│   └── database.py     # SQLAlchemy connection
│
├── models/             ← Add database models here
│   └── models.py       # User, Room, Workspace models
│
├── schemas/            ← Add Pydantic schemas here
│   └── schemas.py      # Request/response schemas
│
├── services/           ← Add business logic here
│   └── docker_service.py  # Docker container management
│
├── websocket/          ← WebSocket handlers
│   └── connection_manager.py  # Real-time connections
│
├── main.py            # Application entry point
└── requirements.txt   # Python dependencies
```

**Import Pattern:**
```python
# All imports use flattened structure
from api.v1.auth import get_current_user
from models.models import User
from schemas.schemas import UserResponse
from core.config import settings
```

### Frontend Directory (`frontend/`)

```
frontend/
├── src/
│   ├── pages/          ← Add new pages here
│   │   ├── HomePage.tsx
│   │   ├── LoginPage.tsx
│   │   ├── RegisterPage.tsx
│   │   ├── DashboardPage.tsx
│   │   ├── RoomPage.tsx
│   │   └── WorkspacePage.tsx
│   │
│   ├── components/     ← Create reusable components here (you'll add this)
│   ├── hooks/          ← Custom React hooks (you'll add this)
│   ├── utils/          ← Utility functions (you'll add this)
│   ├── styles/         ← Additional styles (you'll add this)
│   │
│   ├── App.tsx         # Main app component
│   ├── App.css         # App-level styles
│   ├── main.tsx        # Entry point
│   └── index.css       # Global styles
│
├── index.html
├── package.json
├── vite.config.ts
└── tsconfig.json
```

### AI Service Directory (`ai-service/`)

```
ai-service/
├── main.py            ← Main AI service
├── requirements.txt   ← Python dependencies
└── Dockerfile
```

---

## 🛠️ Common Tasks

### Adding a New Backend Endpoint

1. Open appropriate file in `backend/api/v1/`
2. Add your endpoint function
3. Import necessary models from `models.models`
4. Import schemas from `schemas.schemas`
5. Test using http://localhost:8000/docs

Example:
```python
# backend/api/v1/rooms.py
from fastapi import APIRouter
from models.models import Room
from schemas.schemas import RoomResponse

@router.get("/rooms/{room_id}", response_model=RoomResponse)
async def get_room(room_id: int):
    # Your code here
    pass
```

### Adding a New Database Model

1. Open `backend/models/models.py`
2. Add your SQLAlchemy model
3. Import Base: `from db.database import Base`
4. Run migrations (after setup)

Example:
```python
# backend/models/models.py
from db.database import Base

class YourModel(Base):
    __tablename__ = "your_table"
    # Your fields here
```

### Adding a New Frontend Page

1. Create file in `frontend/src/pages/`
2. Add route in `frontend/src/App.tsx`
3. Style in component or `App.css`

Example:
```typescript
// frontend/src/pages/NewPage.tsx
export default function NewPage() {
  return <div>Your page content</div>
}

// frontend/src/App.tsx
import NewPage from './pages/NewPage'

<Route path="/new" element={<NewPage />} />
```

---

## 📝 File Naming Conventions

### Python (Backend)
- **Files:** `snake_case.py` (e.g., `docker_service.py`)
- **Classes:** `PascalCase` (e.g., `WorkspaceManager`)
- **Functions:** `snake_case` (e.g., `get_current_user`)
- **Constants:** `UPPER_SNAKE_CASE` (e.g., `MAX_RETRIES`)

### TypeScript/React (Frontend)
- **Components:** `PascalCase.tsx` (e.g., `DashboardPage.tsx`)
- **Utilities:** `camelCase.ts` (e.g., `apiClient.ts`)
- **Types/Interfaces:** `PascalCase` (e.g., `interface UserProps`)
- **Variables:** `camelCase` (e.g., `const userName`)

---

## 🔍 Finding Things

### "Where do I add X?"

| What | Where |
|------|-------|
| API endpoint | `backend/api/v1/*.py` |
| Database model | `backend/models/models.py` |
| Request/response validation | `backend/schemas/schemas.py` |
| Business logic | `backend/services/*.py` |
| React page | `frontend/src/pages/*.tsx` |
| React component | `frontend/src/components/*.tsx` (create this dir) |
| Styles | `frontend/src/*.css` or component file |
| Documentation | `docs/*.md` |

### "Where is X defined?"

| Looking for | Found in |
|-------------|----------|
| Database connection | `backend/db/database.py` |
| App settings | `backend/core/config.py` |
| JWT auth | `backend/core/security.py` |
| WebSocket manager | `backend/websocket/connection_manager.py` |
| App routes | `frontend/src/App.tsx` |
| Environment variables | `.env` (copy from `.env.example`) |

---

## 🚀 Getting Started

### First Time Setup

```bash
# 1. Navigate to project
cd Ghost-Labs

# 2. Create your branch
git checkout -b your-name

# 3. Copy environment file
cp .env.example .env

# 4. Start services
docker-compose up --build
```

### Daily Development

```bash
# 1. Create feature branch
git checkout -b your-name/feature-name

# 2. Make changes in backend/ or frontend/

# 3. Test your changes
# Backend: http://localhost:8000/docs
# Frontend: http://localhost:3000

# 4. Commit and push
git add .
git commit -m "feat: your changes"
git push origin your-name/feature-name
```

---

## 💡 Tips

### For Backend Developers
- Use FastAPI's automatic docs: http://localhost:8000/docs
- All imports use the flattened structure (no `app.` prefix)
- Add type hints to all functions
- Write docstrings for complex functions

### For Frontend Developers
- Component files go in `src/pages/` or create `src/components/`
- Use TypeScript for type safety
- Keep components small and focused
- Test in browser DevTools

### For Everyone
- Read `docs/GIT_WORKFLOW.md` for Git best practices
- Check `docs/API.md` for API documentation
- Follow coding standards in `CONTRIBUTING.md`
- Ask questions by opening an issue or discussion

---

## 🆘 Help

**Can't find something?**
1. Check this guide
2. Search the codebase: `grep -r "thing_you're_looking_for"`
3. Ask in team chat or GitHub discussions
4. Open an issue with the `question` label

**Confused about imports?**
Remember: The `backend/app/` directory was removed for simplicity.
- ❌ Old: `from app.models.models import User`
- ✅ New: `from models.models import User`

---

Happy coding! 🎉
