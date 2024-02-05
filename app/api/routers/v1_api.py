from fastapi import APIRouter

from app.api.routers import v1_remote_job_detection

router = APIRouter()
router.include_router(
    v1_remote_job_detection.router, tags=["remote job detection"], prefix="/v1"
)