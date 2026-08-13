from sqlalchemy.orm import Session

from app.models.album_model import Album
from app.schemas.album import AlbumCreate


def create_album(db: Session, data: AlbumCreate, owner_id: int) -> Album:
    album = Album(**data.model_dump(), owner_id=owner_id)
    db.add(album)
    db.commit()
    db.refresh(album)
    return album
