from pydantic import BaseModel
from datetime import date

class ArtistBase(BaseModel):
    stage_name: str

class ArtistCreate(ArtistBase):
    id: int
    first_name: str
    last_name: str
    email: str
    date_of_birth: date

class Artist(ArtistCreate):
    class Config:
        orm_mode = True
        
class SongBase(BaseModel):
    title: str
    artist: Artist

class SongCreate(SongBase):
    producer: str
    release_date: date

class Song(SongCreate):
    
    class Config:
        orm_mode = True