from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.actions.album.read_album_action import read_album
from app.models.album_model import Album
from app.schemas.album import AlbumUpdate


def update_album(db: Session, album_id: int, data: AlbumUpdate, user_id: int) -> Album:
    album = read_album(db, album_id)
    if album.owner_id != user_id:
        raise HTTPException(status_code=403, detail="Not authorized to edit this album")
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(album, field, value)
    db.commit()
    db.refresh(album)
    return album
