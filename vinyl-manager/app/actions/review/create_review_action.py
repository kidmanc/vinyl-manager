from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.album_model import Album
from app.models.review_model import Review
from app.schemas.review import ReviewCreate


def create_review(
    db: Session, album_id: int, data: ReviewCreate, user_id: int
) -> Review:
    album = db.query(Album).filter(Album.id == album_id).first()
    if album is None:
        raise HTTPException(status_code=404, detail="Album not found")
    review = Review(
        album_id=album_id,
        user_id=user_id,
        text=data.text,
        rating=data.rating,
    )
    db.add(review)
    db.commit()
    db.refresh(review)
    return review
