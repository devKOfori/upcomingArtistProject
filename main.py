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

@app.post("/artists/", response_model=schemas.Artist)
def create_artist(artist: schemas.Artist, db: Session = Depends(get_db)):
    db_artist = crud.get_artist_by_email(db, email=artist.email)
    if db_artist:
        raise HTTPException(status_code=404, detail="Artist already exist")
    return crud.create_artist(db=db, artist=artist)

@app.get("/artists/{artist_id}", response_model=schemas.Artist)
def read_user(artist_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_artist(db, artist_id=artist_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Artist not found")
    return db_user