"""
Workspace management endpoints
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db
from models.models import Workspace, User, WorkspaceStatus
from schemas.schemas import WorkspaceCreate, WorkspaceResponse, WorkspaceAction
from api.v1.auth import get_current_user
from services.docker_service import docker_service

router = APIRouter()


@router.post("/", response_model=WorkspaceResponse, status_code=status.HTTP_201_CREATED)
async def create_workspace(
    workspace_data: WorkspaceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Create a new workspace"""
    new_workspace = Workspace(
        name=workspace_data.name,
        owner_id=current_user.id,
        status=WorkspaceStatus.STOPPED
    )
    
    db.add(new_workspace)
    db.commit()
    db.refresh(new_workspace)
    
    return new_workspace


@router.get("/", response_model=List[WorkspaceResponse])
async def get_workspaces(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get all workspaces for current user"""
    workspaces = db.query(Workspace).filter(
        Workspace.owner_id == current_user.id
    ).all()
    return workspaces


@router.get("/{workspace_id}", response_model=WorkspaceResponse)
async def get_workspace(
    workspace_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get workspace by ID"""
    workspace = db.query(Workspace).filter(
        Workspace.id == workspace_id,
        Workspace.owner_id == current_user.id
    ).first()
    
    if not workspace:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Workspace not found"
        )
    return workspace


@router.post("/{workspace_id}/action", response_model=WorkspaceResponse)
async def workspace_action(
    workspace_id: int,
    action: WorkspaceAction,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Perform action on workspace (start, stop, snapshot, restore)"""
    workspace = db.query(Workspace).filter(
        Workspace.id == workspace_id,
        Workspace.owner_id == current_user.id
    ).first()
    
    if not workspace:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Workspace not found"
        )
    
    # Perform action based on type
    if action.action == "start":
        container_id = await docker_service.start_workspace(workspace_id, current_user.id)
        workspace.container_id = container_id
        workspace.status = WorkspaceStatus.RUNNING
    
    elif action.action == "stop":
        await docker_service.stop_workspace(workspace.container_id)
        workspace.status = WorkspaceStatus.STOPPED
    
    elif action.action == "snapshot":
        snapshot_path = await docker_service.create_snapshot(
            workspace.container_id,
            action.snapshot_name or f"snapshot_{workspace_id}"
        )
        workspace.snapshot_path = snapshot_path
    
    elif action.action == "restore":
        if not workspace.snapshot_path:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No snapshot available"
            )
        await docker_service.restore_snapshot(workspace.container_id, workspace.snapshot_path)
    
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unknown action: {action.action}"
        )
    
    db.commit()
    db.refresh(workspace)
    
    return workspace


@router.delete("/{workspace_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_workspace(
    workspace_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Delete a workspace"""
    workspace = db.query(Workspace).filter(
        Workspace.id == workspace_id,
        Workspace.owner_id == current_user.id
    ).first()
    
    if not workspace:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Workspace not found"
        )
    
    # Stop and remove container if running
    if workspace.container_id:
        await docker_service.remove_workspace(workspace.container_id)
    
    db.delete(workspace)
    db.commit()
    
    return None
