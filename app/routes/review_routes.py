from fastapi import APIRouter, Depends

from app.controllers.review_controller import (
    create_review,
    delete_review,
    read_reviews,
)
from app.core.database import get_db
from app.core.security import get_current_user
from app.models.user_model import User
from app.schemas.review import ReviewCreate

router = APIRouter(tags=["reviews"])


@router.get("/albums/{album_id}/reviews")
def list_reviews_route(album_id: int, db=Depends(get_db)):
    return read_reviews(db, album_id)


@router.post("/albums/{album_id}/reviews", status_code=201)
def create_review_route(
    album_id: int,
    payload: ReviewCreate,
    db=Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_review(db, album_id, payload, current_user.id)


@router.delete("/reviews/{review_id}")
def delete_review_route(
    review_id: int,
    db=Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return delete_review(db, review_id, current_user.id)
