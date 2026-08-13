from fastapi import APIRouter, Depends

from app.controllers.user_controller import authenticate_user, register_user
from app.core.database import get_db
from app.schemas.user import LoginRequest, UserCreate

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/register", status_code=201)
def register_route(payload: UserCreate, db=Depends(get_db)):
    return register_user(db, payload.username, payload.email, payload.password)


@router.post("/login")
def login_route(payload: LoginRequest, db=Depends(get_db)):
    return authenticate_user(db, payload.username, payload.password)
