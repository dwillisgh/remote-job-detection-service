import pytest

from app.api.errors import GenericException


@pytest.mark.asyncio
async def test_errors():
    errors = GenericException(400, "test error")

    assert errors.http_status_code == 400
