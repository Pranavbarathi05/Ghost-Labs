"""
Room management endpoints
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db
from models.models import Room, RoomMember, User
from schemas.schemas import RoomCreate, RoomResponse
from api.v1.auth import get_current_user

router = APIRouter()


@router.post("/", response_model=RoomResponse, status_code=status.HTTP_201_CREATED)
async def create_room(
    room_data: RoomCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Create a new room"""
    new_room = Room(
        name=room_data.name,
        description=room_data.description,
        creator_id=current_user.id
    )
    
    db.add(new_room)
    db.commit()
    db.refresh(new_room)
    
    # Add creator as a member with control permissions
    room_member = RoomMember(
        room_id=new_room.id,
        user_id=current_user.id,
        can_control=True
    )
    db.add(room_member)
    db.commit()
    
    return new_room


@router.get("/", response_model=List[RoomResponse])
async def get_rooms(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get all active rooms"""
    rooms = db.query(Room).filter(Room.is_active == True).offset(skip).limit(limit).all()
    return rooms


@router.get("/{room_id}", response_model=RoomResponse)
async def get_room(
    room_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get room by ID"""
    room = db.query(Room).filter(Room.id == room_id).first()
    if not room:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Room not found"
        )
    return room


@router.post("/{room_id}/join")
async def join_room(
    room_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Join a room"""
    room = db.query(Room).filter(Room.id == room_id).first()
    if not room:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Room not found"
        )
    
    # Check if already a member
    existing = db.query(RoomMember).filter(
        RoomMember.room_id == room_id,
        RoomMember.user_id == current_user.id
    ).first()
    
    if existing:
        return {"message": "Already a member of this room"}
    
    # Add as member
    room_member = RoomMember(
        room_id=room_id,
        user_id=current_user.id,
        can_control=False
    )
    db.add(room_member)
    db.commit()
    
    return {"message": "Successfully joined room"}


@router.delete("/{room_id}/leave")
async def leave_room(
    room_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Leave a room"""
    membership = db.query(RoomMember).filter(
        RoomMember.room_id == room_id,
        RoomMember.user_id == current_user.id
    ).first()
    
    if not membership:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Not a member of this room"
        )
    
    db.delete(membership)
    db.commit()
    
    return {"message": "Successfully left room"}
