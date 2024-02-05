import pytest

from app.model.remote_job_detection_response import RemoteJobDetectionResponse


@pytest.mark.asyncio
async def test_remote_job_detection_response():
    remote_job_detection_response = RemoteJobDetectionResponse()

    remote_job_detection_response.titlematches = ["remote"]

    assert remote_job_detection_response.titlematches == ["remote"]
    