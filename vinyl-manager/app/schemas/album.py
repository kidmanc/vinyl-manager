from pydantic import BaseModel


class AlbumCreate(BaseModel):
    title: str
    artist: str
    genre: str
    release_year: int
    cover_url: str = ""


class AlbumUpdate(BaseModel):
    title: str | None = None
    artist: str | None = None
    genre: str | None = None
    release_year: int | None = None
    cover_url: str | None = None


class AlbumResponse(BaseModel):
    id: int
    title: str
    artist: str
    genre: str
    release_year: int
    cover_url: str
    owner_id: int

    model_config = {"from_attributes": True}


class AlbumListResponse(BaseModel):
    items: list[AlbumResponse]
    total: int
    page: int
    page_size: int
