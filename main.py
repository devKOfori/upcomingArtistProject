from enum import Enum
from fastapi import FastAPI, Query, Path, HTTPException, Depends
from pydantic import BaseModel, Field, HttpUrl
from typing import Annotated, List
from sqlalchemy.orm import Session

from data import models, database, schemas, api

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally: 
        db.close()


@app.get("/social-media")
def get_all_social_media(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    all_social_media = api.get_all_social_media(db, skip=skip, limit=limit)
    return all_social_media

@app.get("/social-media/{social_medial_id}")
def get_social_media(social_media_id: int, db: Session = Depends(get_db)):
    social_media = api.get_social_media(db, social_media_id)
    return social_media
