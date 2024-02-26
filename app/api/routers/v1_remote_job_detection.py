from fastapi import APIRouter
from typing import Any
from loguru import logger

from ...model.job_posting import JobPosting
from ...model.remote_job_detection_response import RemoteJobDetectionResponse
from app.services.remote_job_detection_service import (
    extract_remote_patterns, load_field_remote_patterns
)

router = APIRouter()


@router.post(
    path="/remotejobdetect",
    response_model=RemoteJobDetectionResponse,
    response_model_exclude_none=True,
    summary="Given a JobPosting object as input, return remote job pattern matches'",
)
async def extract_remote_patterns_job_posting(
        jobposting: JobPosting,
        researchpatterns: bool = False
) -> Any:
    data = await extract_remote_patterns(jobposting, researchpatterns)

    remotejobdetectionresponse = RemoteJobDetectionResponse(**data)

    logger.info("remotejobdetectionresponse '{response}'",
                response=remotejobdetectionresponse)

    return remotejobdetectionresponse


@router.get(
    path="/remotepatterns",
    summary="return all remote patterns",
)
async def get_remote_patterns(
) -> Any:
    data = await load_field_remote_patterns()

    return data
