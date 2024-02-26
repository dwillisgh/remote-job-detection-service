from pydantic import BaseModel
from typing import Any, Union, List, Optional


class PostalAddress(BaseModel):
    addressLocality: Optional[str] = None


class Place(BaseModel):
    address: Optional[PostalAddress] = None


class Identifier(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None


class JobPosting(BaseModel):
    description: Optional[str] = None
    title: Optional[str] = None
    jobLocation: Union[Optional[List[Place]], Optional[Place]] = None
    jobLocationType: Optional[str] = None
    identifier: Optional[Identifier] = None
