"""
WebSocket connection manager for real-time communication
"""
from fastapi import WebSocket
from typing import Dict, List
import json
import logging

logger = logging.getLogger(__name__)


class ConnectionManager:
    """Manages WebSocket connections for rooms"""
    
    def __init__(self):
        # Dictionary mapping room_id to list of (user_id, websocket) tuples
        self.active_connections: Dict[str, List[tuple[str, WebSocket]]] = {}
    
    async def connect(self, websocket: WebSocket, room_id: str, user_id: str):
        """Accept and register a new WebSocket connection"""
        await websocket.accept()
        
        if room_id not in self.active_connections:
            self.active_connections[room_id] = []
        
        self.active_connections[room_id].append((user_id, websocket))
        logger.info(f"User {user_id} connected to room {room_id}")
        
        # Notify others in the room
        await self.broadcast(
            room_id,
            {
                "type": "user_joined",
                "user_id": user_id,
                "message": f"User {user_id} joined the room"
            },
            exclude_user=user_id
        )
    
    def disconnect(self, room_id: str, user_id: str):
        """Remove a WebSocket connection"""
        if room_id in self.active_connections:
            self.active_connections[room_id] = [
                (uid, ws) for uid, ws in self.active_connections[room_id]
                if uid != user_id
            ]
            
            # Clean up empty rooms
            if not self.active_connections[room_id]:
                del self.active_connections[room_id]
            
            logger.info(f"User {user_id} disconnected from room {room_id}")
    
    async def send_personal_message(self, message: dict, websocket: WebSocket):
        """Send a message to a specific client"""
        await websocket.send_json(message)
    
    async def broadcast(self, room_id: str, message: dict, exclude_user: str = None):
        """Broadcast a message to all clients in a room"""
        if room_id not in self.active_connections:
            return
        
        disconnected = []
        for user_id, connection in self.active_connections[room_id]:
            if exclude_user and user_id == exclude_user:
                continue
            
            try:
                await connection.send_json(message)
            except Exception as e:
                logger.error(f"Error sending message to {user_id}: {e}")
                disconnected.append(user_id)
        
        # Clean up disconnected clients
        for user_id in disconnected:
            self.disconnect(room_id, user_id)


# Global connection manager instance
manager = ConnectionManager()
