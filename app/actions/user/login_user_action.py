from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.security import create_access_token, verify_password
from app.models.user_model import User


def login_user(db: Session, username: str, password: str) -> str:
    user = db.query(User).filter(User.username == username).first()
    if user is None or not verify_password(password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return create_access_token(data={"sub": str(user.id)})
