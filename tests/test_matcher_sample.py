import pytest

from matcher_sample import run_match


@pytest.mark.asyncio
async def test_matcher_sample():
    run_match()