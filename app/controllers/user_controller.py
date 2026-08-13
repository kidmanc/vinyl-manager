from sqlalchemy.orm import Session

from app.actions.user.login_user_action import login_user as login_user_action
from app.actions.user.register_user_action import register_user as register_user_action
from app.schemas.user import Token, UserResponse


def register_user(
    db: Session, username: str, email: str, password: str
) -> UserResponse:
    user = register_user_action(db, username, email, password)
    return UserResponse(id=user.id, username=user.username, email=user.email)


def authenticate_user(db: Session, username: str, password: str) -> Token:
    access_token = login_user_action(db, username, password)
    return Token(access_token=access_token, token_type="bearer")
