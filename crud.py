from sqlalchemy.orm import Session
from fastapi import HTTPException
import models, schemas

def create_artist(db: Session, artist: schemas.ArtistCreate):
    artist = models.Artist(**artist.dict())
    db.add(artist)
    db.commit()
    db.refresh(artist)
    return artist

def get_artist(db: Session, artist_id: int):
    return db.query(models.Artist).filter(models.Artist.id==artist_id).first()

def get_artist_by_email(db: Session, email: str):
    return db.query(models.Artist).filter(models.Artist.email==email).first()

def get_all_artists(db: Session):
    return db.query(models.Artist)

def update_artist_record(db: Session, artist_id: int, artist: schemas.Artist):
    db_artist = db.query(models.Artist).filter(models.Artist.id==artist_id).first()
    if db_artist is None:
        raise HTTPException(status_code=404, detail="Artist does not exist")
    for key, value in artist.dict().items():
        setattr(db_artist, key, value)
    db.commit()
    db.refresh(db_artist)
    return db_artist

def add_new_song(db: Session, artist_id: int, song: schemas.SongCreate):
    artist = db.query(models.Artist).filter(models.Artist.id==artist_id).first()
    if artist is None:
        raise HTTPException(status_code=404, detail="No artist found")
    new_song = models.Song(**song.dict(), artist_id=artist_id)
    db.add(new_song)
    db.commit()
    db.refresh(new_song)
    return new_song