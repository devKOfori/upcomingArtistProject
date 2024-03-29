from fastapi import FastAPI, Depends, HTTPException
from database import SessionLocal, engine
import models, crud, schemas
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/artists/add", response_model=schemas.Artist)
async def create_artist(artist: schemas.Artist, db: Session = Depends(get_db)):
    db_artist = crud.get_artist_by_email(db, email=artist.email)
    if db_artist:
        raise HTTPException(status_code=404, detail="Artist already exist")
    return crud.create_artist(db=db, artist=artist)

@app.get("/artists/{artist_id}", response_model=schemas.Artist)
async def get_artist_by_id(artist_id: int, db: Session = Depends(get_db)):
    db_artist = crud.get_artist(db, artist_id=artist_id)
    if db_artist is None:
        raise HTTPException(status_code=404, detail="Artist not found")
    return db_artist

@app.get("/artists/", response_model=list[schemas.Artist])
async def get_all_artists(db: Session = Depends(get_db)):
    artists = crud.get_all_artists(db=db)
    return artists

@app.put("/artists/{artist_id}/update", response_model=schemas.Artist)
async def update_artist_record(artist_id: int, artist: schemas.Artist, db: Session = Depends(get_db)):
    artist = crud.update_artist_record(db=db, artist_id=artist_id, artist=artist)
    return artist

@app.delete("/artists/{artist_id}/delete")
async def delete_artist_record(artist_id: int, db: Session = Depends(get_db)):
    artist = crud.get_artist(db, artist_id)
    if artist:
        db.delete(artist)
        db.commit()
        return {"message": "Record deleted successfully"}
    return {"message": "No Artist found"}

@app.post("/artists/{artist_id}/add-song", response_model=schemas.Song)
async def add_new_song(artist_id: int, song: schemas.SongCreate, db: Session = Depends(get_db)):
    new_song = crud.add_new_song(db, artist_id, song)
    return new_song

@app.get("/artists/{artist_id}/songs", response_model=list[schemas.Song])
async def get_songs_by_artist(artist_id: int, db: Session = Depends(get_db)):
    artist_songs = crud.get_songs_by_artist(db, artist_id)
    return artist_songs

@app.get("/songs/all", response_model=list[schemas.Song])
async def get_all_songs(db: Session = Depends(get_db)):
    songs = crud.get_all_songs(db)
    return songs