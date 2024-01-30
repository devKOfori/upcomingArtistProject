from pydantic import BaseModel
from typing import Annotated, List
from pydantic import Field
from fastapi import Query, Path
from typing import Optional

class SocialHandle(BaseModel):
    id: Annotated[int, Field(gt=0)]

class SocialMediaBase(BaseModel):
    name: str
    url: Optional[str]

class SocialMediaCreate(SocialMediaBase):
    url: Optional[str]
    icon_path: Optional[str]
    owner: Optional[List[str]]
    social_handles: List["SocialHandle"]

class SocialMedia(SocialMediaBase):
    id: int
    icon_path: Optional[str]
    owner: Optional[str]
    social_handles: List["SocialHandle"]

    # class Config:
    #     orm_mode = True

