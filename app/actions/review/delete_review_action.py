from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.review_model import Review


def delete_review(db: Session, review_id: int, user_id: int) -> None:
    review = db.query(Review).filter(Review.id == review_id).first()
    if review is None:
        raise HTTPException(status_code=404, detail="Review not found")
    if review.user_id != user_id:
        raise HTTPException(
            status_code=403, detail="Not authorized to delete this review"
        )
    db.delete(review)
    db.commit()
