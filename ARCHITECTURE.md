# 🚀 Ghost Labs - Architecture Guide

## Overview

Ghost Labs combines the best of **SyncLab's collaborative features** with **persistent Docker workspaces** and **AI assistance**. This document outlines the complete project architecture.

---

## 🏗️ New Project Structure

```
Ghost-Labs/
│
├── backend/                      # FastAPI Backend (Python)
│   ├── api/
│   │   ├── __init__.py
│   │   ├── auth.py              # Authentication (JWT + optional Clerk)
│   │   ├── rooms.py             # Room management
│   │   ├── users.py             # User management
│   │   ├── workspaces.py        # Docker workspace operations
│   │   ├── snapshots.py         # Container snapshots
│   │   ├── files.py             # File upload/download
│   │   ├── whiteboard.py        # Whiteboard state management
│   │   ├── rtc.py               # Agora RTC token generation
│   │   └── ai.py                # AI agent integration
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py            # Environment config
│   │   ├── security.py          # JWT & encryption
│   │   └── redis_client.py      # Redis connection
│   │
│   ├── db/
│   │   ├── __init__.py
│   │   ├── database.py          # PostgreSQL connection
│   │   └── redis_db.py          # Redis for real-time features
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py              # User model
│   │   ├── room.py              # Room model
│   │   ├── workspace.py         # Workspace model
│   │   ├── snapshot.py          # Snapshot model
│   │   ├── room_member.py       # Room membership
│   │   └── whiteboard.py        # Whiteboard state
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user_schemas.py
│   │   ├── room_schemas.py
│   │   ├── workspace_schemas.py
│   │   ├── snapshot_schemas.py
│   │   └── file_schemas.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── docker_service.py    # Docker container management
│   │   ├── file_service.py      # File operations
│   │   ├── snapshot_service.py  # Snapshot management
│   │   ├── port_manager.py      # Port allocation (Redis)
│   │   ├── package_library.py   # Available packages for containers
│   │   └── ai_service.py        # AI integration
│   │
│   ├── websocket/
│   │   ├── __init__.py
│   │   ├── connection_manager.py  # WebSocket connections
│   │   ├── chat_handler.py        # Chat messages
│   │   ├── whiteboard_handler.py  # Whiteboard sync
│   │   └── code_sync_handler.py   # Code editor sync
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── helpers.py
│   │   └── validators.py
│   │
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── conftest.py          # Pytest fixtures
│   │   ├── test_auth.py
│   │   ├── test_rooms.py
│   │   ├── test_workspaces.py
│   │   └── test_snapshots.py
│   │
│   ├── main.py                  # FastAPI app entry
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env.example
│
├── frontend/                    # React + TypeScript
│   ├── public/
│   │   └── noVNC/               # NoVNC for VNC display
│   │
│   ├── src/
│   │   ├── assets/
│   │   │   └── images/
│   │   │
│   │   ├── components/
│   │   │   ├── common/
│   │   │   │   ├── Navbar.tsx
│   │   │   │   ├── ConditionalNavbar.tsx
│   │   │   │   ├── Loader.tsx
│   │   │   │   ├── MainLoader.tsx
│   │   │   │   └── ErrorBoundary.tsx
│   │   │   │
│   │   │   ├── room/
│   │   │   │   ├── VNCDesktop.tsx        # NoVNC viewer
│   │   │   │   ├── CodeEditor.tsx        # Monaco editor
│   │   │   │   ├── Whiteboard.tsx        # Excalidraw
│   │   │   │   ├── FileManager.tsx       # File upload/download
│   │   │   │   ├── FileTree.tsx          # File tree navigation
│   │   │   │   ├── Chat.tsx              # Text chat
│   │   │   │   ├── Chatbot.tsx           # AI chatbot
│   │   │   │   └── RoomControls.tsx      # Control panel
│   │   │   │
│   │   │   ├── video/
│   │   │   │   ├── VideoCall.tsx         # Agora video
│   │   │   │   ├── LocalUser.tsx         # Local video
│   │   │   │   ├── RemoteUser.tsx        # Remote video
│   │   │   │   └── VideoControls.tsx     # Mute/camera controls
│   │   │   │
│   │   │   ├── workspace/
│   │   │   │   ├── WorkspaceSelector.tsx # Switch workspaces
│   │   │   │   ├── SnapshotManager.tsx   # Manage snapshots
│   │   │   │   └── PackageSelector.tsx   # Select packages
│   │   │   │
│   │   │   └── auth/
│   │   │       ├── ProtectedRoute.tsx
│   │   │       └── UnauthenticatedRoute.tsx
│   │   │
│   │   ├── pages/
│   │   │   ├── Home.tsx                  # Landing page
│   │   │   ├── Login.tsx                 # Login page
│   │   │   ├── Register.tsx              # Registration
│   │   │   ├── Dashboard.tsx             # User dashboard
│   │   │   ├── CreateRoom.tsx            # Create room with options
│   │   │   ├── JoinRoom.tsx              # Join room by ID
│   │   │   ├── Meeting.tsx               # Main collaboration page
│   │   │   └── TempDashboard.tsx         # Registration redirect
│   │   │
│   │   ├── services/
│   │   │   ├── api.ts                    # Axios API client
│   │   │   ├── websocket.ts              # WebSocket client
│   │   │   ├── agoraService.ts           # Agora RTC
│   │   │   └── fileService.ts            # File operations
│   │   │
│   │   ├── utils/
│   │   │   ├── registerUser.ts
│   │   │   └── constants.ts
│   │   │
│   │   ├── hooks/
│   │   │   ├── useWebSocket.ts
│   │   │   ├── useAgora.ts
│   │   │   └── useFileUpload.ts
│   │   │
│   │   ├── styles/
│   │   │   ├── App.css
│   │   │   └── index.css
│   │   │
│   │   ├── App.tsx
│   │   ├── main.tsx
│   │   └── vite-env.d.ts
│   │
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   ├── tailwind.config.js
│   ├── .env.example
│   └── index.html
│
├── ai-service/                  # AI Agent Service (Optional)
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── Desktops/                    # Docker images for workspaces
│   ├── ubuntu/
│   │   └── Dockerfile
│   ├── debian/
│   │   └── Dockerfile
│   └── kali/
│       └── Dockerfile
│
├── scripts/
│   ├── init-db.sh               # Initialize database
│   ├── seed-data.py             # Seed test data
│   └── cleanup-containers.sh    # Cleanup orphaned containers
│
├── docs/
│   ├── API.md
│   ├── ARCHITECTURE.md          # Architecture explanation
│   ├── DIRECTORY_GUIDE.md
│   ├── GIT_WORKFLOW.md
│   ├── CONFIGURATION.md
│   ├── CODERABBIT_SETUP.md
│   └── DEPLOYMENT.md
│
├── .github/
│   ├── workflows/
│   │   ├── backend-tests.yml
│   │   ├── frontend-tests.yml
│   │   └── docker-build.yml
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── coderabbit.yaml
│
├── docker-compose.yml           # Complete stack orchestration
├── docker-compose.dev.yml       # Development overrides
├── .env.example
├── .gitignore
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── QUICK_START.md
└── CHANGELOG.md
```

---

## 🔑 Key Architecture Decisions

### 1. **Backend Structure**
- ✅ Separated models into individual files (user.py, room.py, etc.)
- ✅ Redis integration for real-time features and port management
- ✅ Dedicated websocket handlers for different features
- ✅ Port management service (Redis-based, inspired by SyncLab)
- ✅ Package library for container customization

### 2. **Frontend Structure**  
- ✅ Component organization by feature (room/, video/, workspace/)
- ✅ Agora video calling components
- ✅ Dedicated services layer for API calls
- ✅ Custom hooks for WebSocket, Agora, file uploads
- ✅ Proper separation of pages and components

### 3. **SyncLab-Inspired Features**
- ✅ Video/Audio calling (Agora SDK)
- ✅ Whiteboard integration (Excalidraw)
- ✅ Real-time chat in rooms
- ✅ File upload/download to containers
- ✅ Multiple workspace support per room
- ✅ Port management with Redis

### 4. **Ghost Labs Unique Features**
- ✅ Persistent Docker workspaces (not in SyncLab)
- ✅ Container snapshot/restore
- ✅ AI agent integration
- ✅ Terminal access (xterm.js)
- ✅ Full Linux environment customization

---

## 📦 Dependencies

### Backend (requirements.txt)
```txt
# Core Framework
fastapi==0.129.2
uvicorn[standard]==0.41.0
sqlalchemy==2.0.46
pydantic==2.12.5
pydantic-settings==2.13.1
psycopg2-binary==2.9.9
python-jose[cryptography]==3.5.0
passlib[bcrypt]==1.7.4
websockets==16.0
docker==7.1.0
python-dotenv==1.2.1
email-validator==2.3.0

# Redis for real-time features
redis==5.2.0
hiredis==3.0.0          # Faster Redis parser

# Agora tokens for video/audio
agora-token==1.0.0

# File handling
aiofiles==24.1.0

# AI Integration (Optional)
openai==1.58.1
anthropic==0.42.0
```

### Frontend (package.json)
```json
{
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.20.0",
    
    "axios": "^1.6.2",
    "@tanstack/react-query": "^5.12.2",
    
    "zustand": "^4.4.7",
    
    "xterm": "^5.3.0",
    "xterm-addon-fit": "^0.8.0",
    "xterm-addon-web-links": "^0.9.0",
    
    "socket.io-client": "^4.6.1",
    
    "@monaco-editor/react": "^4.6.0",
    
    "@excalidraw/excalidraw": "^0.17.0",
    
    "agora-rtc-react": "^2.3.1",
    "agora-rtc-sdk-ng": "^4.21.0",
    
    "@clerk/clerk-react": "^5.0.0",
    
    "framer-motion": "^11.0.0",
    "react-toastify": "^10.0.0",
    "lucide-react": "^0.445.0",
    "react-icons": "^5.0.0"
  },
  "devDependencies": {
    "@types/react": "^18.2.43",
    "@types/react-dom": "^18.2.17",
    "@vitejs/plugin-react": "^4.2.1",
    "typescript": "^5.2.2",
    "vite": "^5.0.8",
    "tailwindcss": "^3.4.0",
    "autoprefixer": "^10.4.16",
    "postcss": "^8.4.32"
  }
}
```

---

## 🎨 Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Backend** | FastAPI (Python) | High-performance API framework |
| **Frontend** | React + TypeScript | Modern UI with type safety |
| **Database** | PostgreSQL + Redis | Persistent data + real-time features |
| **Auth** | JWT + Optional Clerk | Secure authentication |
| **Video/Audio** | Agora SDK | Crystal-clear communication |
| **Whiteboard** | Excalidraw | Visual collaboration |
| **Code Editor** | Monaco Editor | VS Code's editor engine |
| **Real-time** | WebSocket + Socket.io | Live updates |
| **Styling** | Tailwind CSS | Modern, responsive design |
| **Containers** | Docker | Isolated workspaces |
| **Terminal** | xterm.js + VNC | Browser-based terminal |
| **AI** | OpenAI/Anthropic | Coding assistant |

---

## 🚀 Quick Start

### 1. Clone and Setup
```bash
git clone https://github.com/your-org/Ghost-Labs.git
cd Ghost-Labs

# Copy environment files
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env

# Edit .env files with your credentials
```

### 2. Start with Docker Compose
```bash
# Start all services
docker-compose up --build

# Or start specific services
docker-compose up -d db redis
```

### 3. Install Dependencies

**Backend:**
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

**Frontend:**
```bash
cd frontend
npm install
```

### 4. Run Development Servers

**Backend:**
```bash
cd backend
source venv/bin/activate
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Frontend:**
```bash
cd frontend
npm run dev
```

### 5. Access the Application
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **Redis**: localhost:6379
- **PostgreSQL**: localhost:5432

---

## 🔐 Environment Variables

### Backend (.env)
```env
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/ghostlabs
REDIS_URL=redis://localhost:6379/0

# Security
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Agora (for video/audio)
AGORA_APP_ID=your-agora-app-id
AGORA_APP_CERTIFICATE=your-agora-certificate

# Optional: Clerk Authentication
CLERK_API_KEY=your-clerk-api-key

# Optional: AI Services
OPENAI_API_KEY=your-openai-key
ANTHROPIC_API_KEY=your-anthropic-key

# Docker
DOCKER_HOST=unix:///var/run/docker.sock

# Ports
BASE_VNC_PORT=5900
END_VNC_PORT=5999
```

### Frontend (.env)
```env
# API
VITE_API_URL=http://localhost:8000
VITE_WS_URL=ws://localhost:8000

# Agora
VITE_AGORA_APP_ID=your-agora-app-id

# Optional: Clerk
VITE_CLERK_PUBLISHABLE_KEY=your-clerk-publishable-key
```

---

## 📚 Documentation Structure

All documentation is in the `docs/` directory:

1. **[API.md](docs/API.md)** - Complete API reference
2. **[ARCHITECTURE.md](docs/ARCHITECTURE.md)** - System architecture
3. **[DIRECTORY_GUIDE.md](docs/DIRECTORY_GUIDE.md)** - Directory structure
4. **[GIT_WORKFLOW.md](docs/GIT_WORKFLOW.md)** - Git workflow
5. **[CONFIGURATION.md](docs/CONFIGURATION.md)** - Configuration guide
6. **[DEPLOYMENT.md](docs/DEPLOYMENT.md)** - Deployment instructions

---

## 🎯 Implementation Roadmap

1. **Review** this architecture document
2. **Set up** development environment
3. **Check** [INITIAL_ISSUES.md](INITIAL_ISSUES.md) for starter tasks
**Inspired by:** SyncLab architecture + unique persistent workspace features  
**Status:** Ready for contributor implementation
