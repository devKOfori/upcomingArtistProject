from sqlalchemy.orm import Session
from . import models, schemas

def get_social_media(db: Session, social_media_id: int):
    print(social_media_id)
    results =  db.query(models.SocialMedia).filter(models.SocialMedia.id_social_media == social_media_id).first()
    print(results)
    return results

def get_all_social_media(db: Session, skip: int = 0, limit: int = 100):
    print(db)
    results =  db.query(models.SocialMedia).offset(skip).limit(limit).all()
    print(results)
    return results


