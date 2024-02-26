import pytest

from app.services import remote_job_detection_service


@pytest.mark.asyncio
async def test_load_field_remote_patterns():
    response = await remote_job_detection_service.load_field_remote_patterns()
    assert len(response) == 7
