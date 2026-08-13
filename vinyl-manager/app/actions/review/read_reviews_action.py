from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.album_model import Album
from app.models.review_model import Review


def read_reviews(db: Session, album_id: int) -> list[Review]:
    album = db.query(Album).filter(Album.id == album_id).first()
    if album is None:
        raise HTTPException(status_code=404, detail="Album not found")
    return db.query(Review).filter(Review.album_id == album_id).all()
