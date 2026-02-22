# 🎯 Initial Issues for Contributors

These are the first 6 issues to get started with Ghost Labs development. Each issue is designed to be approachable for individual contributors.

---

## Issue #1: Add Loading States to Frontend Components
**Label:** `good first issue`, `frontend`, `enhancement`  
**Difficulty:** Easy  
**Estimated Time:** 2-3 hours

### Description
Currently, the frontend components don't show loading states when data is being fetched. Add loading spinners/skeletons to improve user experience.

### Tasks
- [ ] Add loading state to Login/Register pages during authentication
- [ ] Add loading spinner component in `src/components/Loading.tsx`
- [ ] Show loading state in Dashboard while fetching rooms
- [ ] Add skeleton loaders for room cards

### Files to Modify
- `frontend/src/pages/LoginPage.tsx`
- `frontend/src/pages/RegisterPage.tsx`
- `frontend/src/pages/DashboardPage.tsx`
- Create: `frontend/src/components/Loading.tsx`

### Acceptance Criteria
- Loading states appear during API calls
- No broken UI during loading
- Consistent loading indicators across pages

---

## Issue #2: Implement Backend Input Validation
**Label:** `good first issue`, `backend`, `security`  
**Difficulty:** Easy  
**Estimated Time:** 3-4 hours

### Description
Add comprehensive input validation to backend API endpoints to ensure data integrity and security.

### Tasks
- [ ] Add email format validation in auth endpoints
- [ ] Validate room name length (3-50 characters)
- [ ] Add password strength requirements (min 8 chars, 1 uppercase, 1 number)
- [ ] Validate workspace names and descriptions
- [ ] Return meaningful error messages for validation failures

### Files to Modify
- `backend/schemas/schemas.py` (add validators)
- `backend/api/v1/auth.py` (add validation logic)
- `backend/api/v1/rooms.py` (validate room data)

### Acceptance Criteria
- Invalid inputs return 422 status with clear error messages
- Password requirements enforced
- Email validation working
- All endpoints validated

---

## Issue #3: Create Unit Tests for Authentication
**Label:** `good first issue`, `backend`, `testing`  
**Difficulty:** Medium  
**Estimated Time:** 4-5 hours

### Description
Set up pytest and create unit tests for authentication endpoints to ensure reliability.

### Tasks
- [ ] Set up pytest configuration (`pytest.ini`)
- [ ] Create test fixtures for database and test client
- [ ] Write tests for `/api/v1/auth/register` endpoint
- [ ] Write tests for `/api/v1/auth/login` endpoint
- [ ] Test JWT token generation and validation
- [ ] Add tests for invalid credentials

### Files to Create
- `backend/tests/__init__.py`
- `backend/tests/conftest.py` (fixtures)
- `backend/tests/test_auth.py`

### Files to Modify
- `backend/requirements.txt` (add pytest, pytest-asyncio)

### Acceptance Criteria
- All tests pass with `pytest`
- Test coverage > 80% for auth endpoints
- Tests run in CI/CD ready format

---

## Issue #4: Add Dark Mode Support to Frontend
**Label:** `good first issue`, `frontend`, `enhancement`  
**Difficulty:** Easy  
**Estimated Time:** 3-4 hours

### Description
Implement dark mode toggle for better user experience and accessibility.

### Tasks
- [ ] Create theme context in `src/contexts/ThemeContext.tsx`
- [ ] Add dark mode styles to `src/styles/App.css`
- [ ] Create theme toggle button component
- [ ] Save theme preference to localStorage
- [ ] Add dark mode variables for colors

### Files to Create
- `frontend/src/contexts/ThemeContext.tsx`

### Files to Modify
- `frontend/src/App.tsx` (wrap with ThemeProvider)
- `frontend/src/styles/App.css` (add dark theme)
- `frontend/src/components/Header.tsx` (add toggle button)

### Acceptance Criteria
- Toggle switches between light/dark mode
- Theme preference persists on page reload
- All pages styled consistently in both modes

---

## Issue #5: Add Environment Configuration Documentation
**Label:** `good first issue`, `documentation`  
**Difficulty:** Easy  
**Estimated Time:** 2 hours

### Description
Create comprehensive documentation for environment variables and configuration setup.

### Tasks
- [ ] Document all backend environment variables
- [ ] Document frontend environment variables
- [ ] Create `.env.example` files for both backend and frontend
- [ ] Add configuration guide in `docs/CONFIGURATION.md`
- [ ] Document Docker environment setup
- [ ] Add Cloudflare Tunnel configuration examples

### Files to Create
- `backend/.env.example`
- `frontend/.env.example`
- `docs/CONFIGURATION.md`

### Files to Modify
- `README.md` (add link to configuration guide)

### Acceptance Criteria
- All environment variables documented
- Clear examples provided
- Instructions for local and production setup

---

## Issue #6: Implement WebSocket Error Handling
**Label:** `good first issue`, `backend`, `enhancement`  
**Difficulty:** Medium  
**Estimated Time:** 3-4 hours

### Description
Add proper error handling and reconnection logic for WebSocket connections.

### Tasks
- [ ] Add try-catch blocks in WebSocket message handlers
- [ ] Implement connection timeout handling
- [ ] Add automatic reconnection logic on frontend
- [ ] Log WebSocket errors properly
- [ ] Send error messages to clients on failure
- [ ] Add heartbeat/ping-pong to detect dead connections

### Files to Modify
- `backend/websocket/connection_manager.py`
- `backend/main.py` (WebSocket endpoint)
- `frontend/src/services/websocket.ts` (reconnection logic)

### Acceptance Criteria
- WebSocket errors don't crash the server
- Clients auto-reconnect on connection loss
- Proper error messages displayed to users
- Connection stability improved

---

## 📝 How to Claim an Issue

1. **Read the docs**: Check `CONTRIBUTING.md` and `docs/GIT_WORKFLOW.md`
2. **Comment on the issue**: Let others know you're working on it
3. **Create a branch**: Follow the naming convention `feature/issue-number-description`
4. **Work on it**: Implement the changes and test thoroughly
5. **Submit PR**: Reference the issue number in your pull request

## 🎓 Tips for Contributors

- Start with issues labeled `good first issue`
- Ask questions in the issue comments if unclear
- Test your changes locally before submitting PR
- Follow the code style of existing files
- Update documentation if you change functionality

---

**Created:** February 22, 2026  
**Status:** Ready for assignment
