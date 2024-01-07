from pydantic import BaseModel
from typing import Annotated, List
from pydantic import Field
from fastapi import Query, Path

class SocialMediaBase(BaseModel):
    name: str
    url: str | None

class SocialMediaCreate(SocialMediaBase):
    url: str | None
    icon_path: str | None
    owner: List[str] | None
    social_handles: List["SocialHandle"] | None

class SocialMedia(SocialMediaBase):
    id: Annotated[int, Field(gt=0)]
    icon_path: str | None
    owner: List[str] | None
    social_handles: List["SocialHandle"] | None

class SocialHandle(BaseModel):
    pass