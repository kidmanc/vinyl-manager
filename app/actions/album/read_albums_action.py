from sqlalchemy.orm import Session

from app.models.album_model import Album


def read_albums(
    db: Session, page: int = 1, page_size: int = 20, genre: str | None = None
) -> tuple[list[Album], int]:
    query = db.query(Album)
    if genre:
        query = query.filter(Album.genre == genre)
    total = query.count()
    items = query.offset((page - 1) * page_size).limit(page_size).all()
    return items, total
