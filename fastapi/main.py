from enum import Enum
from fastapi import FastAPI, Query, Path
from pydantic import BaseModel, Field, HttpUrl
from typing import Annotated
import database

app = FastAPI()
database.create_db_engine()

artists_list = {}

class Artist(BaseModel):
    id: Annotated[int, Field(gt=0)]
    name: str
    stage_name: str
    gender: str
    email: str
    phone: str
    social_profiles: dict[str, str] = dict()
    profile_picture: str | None = None

class Song(BaseModel):
    title: str
    artist_id: int
    released_date: str
    featured_artists: list[int] = []

@app.get("/artists")
async def load_artists():
    return artists_list

@app.get("/artist-by-name")
async def get_artist_by_name(artist_name: str | None = None):
    artists = {}
    for artist_id in artists_list:
        print(artists_list[artist_id].name, artist_name)
        if artists_list[artist_id].name == artist_name:
            artists[artist_id] = artists_list[artist_id]
            # artists.update(artist_id=artists_list[artist_id])
    if not artists:
        return {"message": "No artist record found"}
    return artists
    

@app.get("/artist/{artist_id}")
async def get_artist_by_id(artist_id: int):
    if artist_id not in artists_list:
        return {"Error": f"Artist {artist_id} record not found"}
    return artists_list[artist_id]

@app.post("/create-artist")
async def create_artist(artist: Artist):
    if artist.id in artists_list:
        return {"Error": f"Artist with ID {artist.id} already exist."}
    artists_list[artist.id] = artist
    return {"Success": f"Artist profile created successfully"}

@app.put("/update-artist/{artist_id}")
async def update_artist(artist_id: int, artist: Artist):
    if artist_id not in artists_list:
        return {"Error": f"Artist {artist_id} record not found"}
    artists_list[artist_id] = artist

@app.delete("/delete-artist/{artist_id}")
async def delete_artist(artist_id: int):
    del artists_list[artist_id]
    return {"Success": "Record deleted successfully"}

@app.get("/all-songs")
async def get_all_songs():
    return {"data": "all songs"}

@app.get("/artist-song/{artist_id}")
async def get_artist_song(artist_id: str):
    return {"data": f"all songs by artist with ID {artist_id}"}

@app.post("/create-song")
async def create_song(song: Song):
    return song

@app.get("/search")
async def search():
    pass

