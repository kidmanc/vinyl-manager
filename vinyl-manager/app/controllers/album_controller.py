from sqlalchemy.orm import Session

from app.actions.album.create_album_action import create_album as create_album_action
from app.actions.album.delete_album_action import delete_album as delete_album_action
from app.actions.album.read_album_action import read_album as read_album_action
from app.actions.album.read_albums_action import read_albums as read_albums_action
from app.actions.album.update_album_action import update_album as update_album_action
from app.schemas.album import AlbumCreate, AlbumListResponse, AlbumResponse, AlbumUpdate


def read_albums(
    db: Session, page: int, page_size: int, genre: str | None
) -> AlbumListResponse:
    items, total = read_albums_action(db, page, page_size, genre)
    return AlbumListResponse(items=items, total=total, page=page, page_size=page_size)


def read_album(db: Session, album_id: int) -> AlbumResponse:
    return read_album_action(db, album_id)


def create_album(db: Session, data: AlbumCreate, owner_id: int) -> AlbumResponse:
    return create_album_action(db, data, owner_id)


def update_album(
    db: Session, album_id: int, data: AlbumUpdate, user_id: int
) -> AlbumResponse:
    return update_album_action(db, album_id, data, user_id)


def delete_album(db: Session, album_id: int, user_id: int) -> dict:
    delete_album_action(db, album_id, user_id)
    return {"message": "Album deleted successfully"}
