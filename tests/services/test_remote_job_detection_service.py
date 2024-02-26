import pytest

from app.model.job_posting import JobPosting
from app.services import remote_job_detection_service


@pytest.mark.asyncio
async def test_extract_remote_patterns_description():
    jobposting = JobPosting(description="This is a remote position")

    response = await remote_job_detection_service.extract_remote_patterns_description(jobposting)
    assert len(response) == 2
    assert all([a == b for a, b in zip(response, ["remote position", "This is a remote position"])])

