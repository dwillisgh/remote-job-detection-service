import pytest

from app.model.remote_patterns_response import RemotePatternsResponse, PhrasePattern, FieldPattern


@pytest.mark.asyncio
async def test_remote_patterns_response():
    remote_patterns_response = RemotePatternsResponse()

    phrase_patterns = []
    phrase_pattern = PhrasePattern()
    phrase_patterns.append(phrase_pattern)

    field_patterns = []
    field_pattern = FieldPattern
    field_pattern.phrasePatterns = phrase_patterns
    field_patterns.append(field_pattern)

    remote_patterns_response.fieldpatterns = field_patterns

    assert len(remote_patterns_response.fieldpatterns) == 1
