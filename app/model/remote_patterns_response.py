from typing import Optional, List

from pydantic import BaseModel, Field


class TokenPattern(BaseModel):
    tokenmatchpatterns: Optional[List[str]] = Field(
        description='set of token match patterns',
        default=None
    )


class PhrasePattern(BaseModel):
    tokenmatchpatterns: Optional[List[str]] = Field(
        description='set of token match patterns',
        default=None
    )


class FieldPattern(BaseModel):
    field: str
    phrasePatterns: Optional[List[PhrasePattern]] = Field(
        description='set of phrase patterns for a field',
        default=None
    )


class RemotePatternsResponse(BaseModel):
    fieldpatterns: Optional[List[FieldPattern]] = Field(
        description='set of field patterns',
        default=None
    )
