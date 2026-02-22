# API Documentation

## Overview

Ghost Labs provides a RESTful API built with FastAPI. This document covers the available endpoints, authentication, and usage examples.

## Base URL

```
http://localhost:8000/api/v1
```

## Authentication

Most endpoints require authentication using JWT (JSON Web Tokens).

### Getting a Token

**Endpoint:** `POST /auth/login`

**Request:**
```json
{
  "username": "john_doe",
  "password": "securepassword123"
}
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### Using the Token

Include the token in the Authorization header:
```
Authorization: Bearer <your_token>
```

## Endpoints

### Authentication

#### Register a New User

**Endpoint:** `POST /auth/register`

**Request:**
```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "full_name": "John Doe",
  "password": "securepassword123"
}
```

**Response:** `201 Created`
```json
{
  "id": 1,
  "username": "john_doe",
  "email": "john@example.com",
  "full_name": "John Doe",
  "role": "user",
  "is_active": true,
  "created_at": "2024-02-22T10:00:00Z"
}
```

#### Login

See [Getting a Token](#getting-a-token) above.

#### Get Current User

**Endpoint:** `GET /auth/me`

**Headers:** Authorization required

**Response:** `200 OK`
```json
{
  "id": 1,
  "username": "john_doe",
  "email": "john@example.com",
  "full_name": "John Doe",
  "role": "user",
  "is_active": true,
  "created_at": "2024-02-22T10:00:00Z"
}
```

### Users

#### Get All Users

**Endpoint:** `GET /users?skip=0&limit=100`

**Headers:** Authorization required

**Response:** `200 OK`
```json
[
  {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    "full_name": "John Doe",
    "role": "user",
    "is_active": true,
    "created_at": "2024-02-22T10:00:00Z"
  }
]
```

#### Get User by ID

**Endpoint:** `GET /users/{user_id}`

**Headers:** Authorization required

**Response:** `200 OK` (same as user object above)

### Rooms

#### Create Room

**Endpoint:** `POST /rooms`

**Headers:** Authorization required

**Request:**
```json
{
  "name": "Project Alpha",
  "description": "Development room for Project Alpha"
}
```

**Response:** `201 Created`
```json
{
  "id": 1,
  "name": "Project Alpha",
  "description": "Development room for Project Alpha",
  "creator_id": 1,
  "is_active": true,
  "created_at": "2024-02-22T10:00:00Z"
}
```

#### Get All Rooms

**Endpoint:** `GET /rooms?skip=0&limit=100`

**Headers:** Authorization required

**Response:** `200 OK`
```json
[
  {
    "id": 1,
    "name": "Project Alpha",
    "description": "Development room for Project Alpha",
    "creator_id": 1,
    "is_active": true,
    "created_at": "2024-02-22T10:00:00Z"
  }
]
```

#### Get Room by ID

**Endpoint:** `GET /rooms/{room_id}`

**Headers:** Authorization required

**Response:** `200 OK` (same as room object above)

#### Join Room

**Endpoint:** `POST /rooms/{room_id}/join`

**Headers:** Authorization required

**Response:** `200 OK`
```json
{
  "message": "Successfully joined room"
}
```

#### Leave Room

**Endpoint:** `DELETE /rooms/{room_id}/leave`

**Headers:** Authorization required

**Response:** `200 OK`
```json
{
  "message": "Successfully left room"
}
```

### Workspaces

#### Create Workspace

**Endpoint:** `POST /workspaces`

**Headers:** Authorization required

**Request:**
```json
{
  "name": "Dev Environment"
}
```

**Response:** `201 Created`
```json
{
  "id": 1,
  "name": "Dev Environment",
  "owner_id": 1,
  "container_id": null,
  "status": "stopped",
  "tunnel_url": null,
  "created_at": "2024-02-22T10:00:00Z"
}
```

#### Get All Workspaces

**Endpoint:** `GET /workspaces`

**Headers:** Authorization required

**Response:** `200 OK`
```json
[
  {
    "id": 1,
    "name": "Dev Environment",
    "owner_id": 1,
    "container_id": "abc123def456",
    "status": "running",
    "tunnel_url": "https://abc-123.trycloudflare.com",
    "created_at": "2024-02-22T10:00:00Z"
  }
]
```

#### Get Workspace by ID

**Endpoint:** `GET /workspaces/{workspace_id}`

**Headers:** Authorization required

**Response:** `200 OK` (same as workspace object above)

#### Workspace Actions

**Endpoint:** `POST /workspaces/{workspace_id}/action`

**Headers:** Authorization required

**Actions:**

##### Start Workspace

**Request:**
```json
{
  "action": "start"
}
```

##### Stop Workspace

**Request:**
```json
{
  "action": "stop"
}
```

##### Create Snapshot

**Request:**
```json
{
  "action": "snapshot",
  "snapshot_name": "my-snapshot-v1"
}
```

##### Restore Snapshot

**Request:**
```json
{
  "action": "restore"
}
```

**Response:** `200 OK` (returns updated workspace object)

#### Delete Workspace

**Endpoint:** `DELETE /workspaces/{workspace_id}`

**Headers:** Authorization required

**Response:** `204 No Content`

## WebSocket API

### Connect to Room

**Endpoint:** `ws://localhost:8000/ws/{room_id}/{user_id}`

**Authentication:** Pass JWT token as query parameter or in initial message

### Message Format

#### Send Message

```json
{
  "type": "chat_message",
  "content": "Hello everyone!",
  "timestamp": "2024-02-22T10:00:00Z"
}
```

#### Receive Message

```json
{
  "type": "chat_message",
  "user_id": "1",
  "content": "Hello everyone!",
  "timestamp": "2024-02-22T10:00:00Z"
}
```

#### User Joined

```json
{
  "type": "user_joined",
  "user_id": "2",
  "message": "User 2 joined the room"
}
```

#### User Disconnected

```json
{
  "type": "user_disconnected",
  "user_id": "2"
}
```

## Error Responses

All errors follow this format:

```json
{
  "detail": "Error message describing what went wrong"
}
```

### Common Status Codes

- `200 OK` - Request successful
- `201 Created` - Resource created successfully
- `204 No Content` - Request successful, no content to return
- `400 Bad Request` - Invalid request data
- `401 Unauthorized` - Authentication required or failed
- `403 Forbidden` - Authenticated but not authorized
- `404 Not Found` - Resource not found
- `422 Unprocessable Entity` - Validation error
- `500 Internal Server Error` - Server error

## Rate Limiting

Currently not implemented. Will be added in future versions.

## Pagination

List endpoints support pagination:
- `skip` - Number of records to skip (default: 0)
- `limit` - Maximum records to return (default: 100)

Example:
```
GET /users?skip=20&limit=10
```

## Interactive Documentation

Visit these URLs for interactive API documentation:

- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

## Code Examples

### Python

```python
import requests

# Login
response = requests.post(
    "http://localhost:8000/api/v1/auth/login",
    data={
        "username": "john_doe",
        "password": "securepassword123"
    }
)
token = response.json()["access_token"]

# Use token
headers = {"Authorization": f"Bearer {token}"}

# Get workspaces
workspaces = requests.get(
    "http://localhost:8000/api/v1/workspaces",
    headers=headers
).json()

# Create workspace
new_workspace = requests.post(
    "http://localhost:8000/api/v1/workspaces",
    headers=headers,
    json={"name": "My Workspace"}
).json()
```

### JavaScript/TypeScript

```typescript
// Login
const loginResponse = await fetch('http://localhost:8000/api/v1/auth/login', {
  method: 'POST',
  headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
  body: new URLSearchParams({
    username: 'john_doe',
    password: 'securepassword123'
  })
});
const { access_token } = await loginResponse.json();

// Use token
const headers = { 'Authorization': `Bearer ${access_token}` };

// Get workspaces
const workspaces = await fetch('http://localhost:8000/api/v1/workspaces', {
  headers
}).then(res => res.json());

// Create workspace
const newWorkspace = await fetch('http://localhost:8000/api/v1/workspaces', {
  method: 'POST',
  headers: { ...headers, 'Content-Type': 'application/json' },
  body: JSON.stringify({ name: 'My Workspace' })
}).then(res => res.json());
```

### cURL

```bash
# Login
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=john_doe&password=securepassword123"

# Get workspaces (replace TOKEN with actual token)
curl -X GET "http://localhost:8000/api/v1/workspaces" \
  -H "Authorization: Bearer TOKEN"

# Create workspace
curl -X POST "http://localhost:8000/api/v1/workspaces" \
  -H "Authorization: Bearer TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name": "My Workspace"}'
```

## Changelog

### Version 1.0.0 (Current)
- Initial API release
- User authentication
- Room management
- Workspace CRUD operations
- WebSocket chat

## Support

For API-related questions:
1. Check this documentation
2. Try the interactive docs at `/docs`
3. Open an issue on GitHub
4. Contact the maintainers
