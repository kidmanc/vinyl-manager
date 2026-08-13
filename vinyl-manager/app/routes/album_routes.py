from fastapi import APIRouter, Depends

from app.controllers.album_controller import (
    create_album,
    delete_album,
    read_album,
    read_albums,
    update_album,
)
from app.core.database import get_db
from app.core.security import get_current_user
from app.models.user_model import User
from app.schemas.album import AlbumCreate, AlbumUpdate

router = APIRouter(prefix="/albums", tags=["albums"])


@router.get("")
def list_albums_route(
    page: int = 1,
    page_size: int = 20,
    genre: str | None = None,
    db=Depends(get_db),
):
    return read_albums(db, page, page_size, genre)


@router.get("/{album_id}")
def get_album_route(album_id: int, db=Depends(get_db)):
    return read_album(db, album_id)


@router.post("", status_code=201)
def create_album_route(
    payload: AlbumCreate,
    db=Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_album(db, payload, current_user.id)


@router.put("/{album_id}")
def update_album_route(
    album_id: int,
    payload: AlbumUpdate,
    db=Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return update_album(db, album_id, payload, current_user.id)


@router.delete("/{album_id}")
def delete_album_route(
    album_id: int,
    db=Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return delete_album(db, album_id, current_user.id)
