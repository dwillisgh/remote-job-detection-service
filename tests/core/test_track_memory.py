import pytest

from app.core.track_memory import track


async def sample_func():
    print("hello world")


@pytest.mark.asyncio
async def test_track():
    track(sample_func)
