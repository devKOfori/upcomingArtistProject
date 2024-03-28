from sqlalchemy.orm import Session
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
