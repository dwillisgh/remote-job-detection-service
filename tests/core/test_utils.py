import pytest

from app.core.utils import app_startup, app_shutdown


@pytest.mark.asyncio
async def test_utils():
    await app_startup()
    await app_shutdown()