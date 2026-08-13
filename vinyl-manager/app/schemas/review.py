from datetime import datetime

from pydantic import BaseModel, Field


class ReviewCreate(BaseModel):
    text: str
    rating: int = Field(ge=1, le=5)


class ReviewResponse(BaseModel):
    id: int
    album_id: int
    user_id: int
    text: str
    rating: int
    created_at: datetime

    model_config = {"from_attributes": True}
