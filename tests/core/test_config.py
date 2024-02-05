import pytest

from app.core.config import Settings


@pytest.mark.asyncio
async def test_config():
    settings = Settings()
    assert settings.VERSION == "1.0"
