"""
Docker service for managing workspace containers
"""
import docker
from docker.errors import DockerException
import logging
from core.config import settings

logger = logging.getLogger(__name__)


class DockerService:
    """Service for managing Docker containers"""
    
    def __init__(self):
        try:
            self.client = docker.from_env()
            logger.info("Docker client initialized successfully")
        except DockerException as e:
            logger.error(f"Failed to initialize Docker client: {e}")
            self.client = None
    
    async def start_workspace(self, workspace_id: int, user_id: int) -> str:
        """Start a new workspace container"""
        if not self.client:
            raise Exception("Docker client not available")
        
        container_name = f"workspace_{user_id}_{workspace_id}"
        
        try:
            # Check if container already exists
            try:
                existing = self.client.containers.get(container_name)
                existing.start()
                logger.info(f"Started existing container: {container_name}")
                return existing.id
            except docker.errors.NotFound:
                pass
            
            # Create new container
            container = self.client.containers.run(
                settings.WORKSPACE_IMAGE,
                name=container_name,
                detach=True,
                tty=True,
                stdin_open=True,
                network_mode="bridge",
                labels={
                    "workspace_id": str(workspace_id),
                    "user_id": str(user_id),
                    "managed_by": "ghost-labs"
                }
            )
            
            logger.info(f"Created new container: {container_name}")
            return container.id
        
        except DockerException as e:
            logger.error(f"Failed to start workspace: {e}")
            raise Exception(f"Failed to start workspace: {str(e)}")
    
    async def stop_workspace(self, container_id: str):
        """Stop a workspace container"""
        if not self.client:
            raise Exception("Docker client not available")
        
        try:
            container = self.client.containers.get(container_id)
            container.stop(timeout=10)
            logger.info(f"Stopped container: {container_id}")
        except docker.errors.NotFound:
            logger.warning(f"Container not found: {container_id}")
        except DockerException as e:
            logger.error(f"Failed to stop workspace: {e}")
            raise Exception(f"Failed to stop workspace: {str(e)}")
    
    async def create_snapshot(self, container_id: str, snapshot_name: str) -> str:
        """Create a snapshot of a container"""
        if not self.client:
            raise Exception("Docker client not available")
        
        try:
            container = self.client.containers.get(container_id)
            
            # Commit container to image
            image = container.commit(
                repository="ghost-labs-snapshots",
                tag=snapshot_name
            )
            
            snapshot_path = f"{settings.WORKSPACE_SNAPSHOT_PATH}/{snapshot_name}.tar"
            logger.info(f"Created snapshot: {snapshot_name}")
            return snapshot_path
        
        except DockerException as e:
            logger.error(f"Failed to create snapshot: {e}")
            raise Exception(f"Failed to create snapshot: {str(e)}")
    
    async def restore_snapshot(self, container_id: str, snapshot_path: str):
        """Restore a container from snapshot"""
        # TODO: Implement snapshot restoration logic
        logger.info(f"Restoring snapshot: {snapshot_path}")
        pass
    
    async def remove_workspace(self, container_id: str):
        """Remove a workspace container"""
        if not self.client:
            raise Exception("Docker client not available")
        
        try:
            container = self.client.containers.get(container_id)
            container.stop(timeout=5)
            container.remove()
            logger.info(f"Removed container: {container_id}")
        except docker.errors.NotFound:
            logger.warning(f"Container not found: {container_id}")
        except DockerException as e:
            logger.error(f"Failed to remove workspace: {e}")
            raise Exception(f"Failed to remove workspace: {str(e)}")


# Global Docker service instance
docker_service = DockerService()
