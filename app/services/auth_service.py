
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)


def register_user(db: Session, user: UserCreate):
    # Check whether email or username already exists
    existing_user = db.query(User).filter(
        (User.email == user.email) |
        (User.username == user.username)
    ).first()

    if existing_user:
        return None

    # Hash the user's password
    hashed_password = hash_password(user.password)

    # Create new user
    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )

    db.add(new_user)

    try:
        db.commit()
        db.refresh(new_user)
        return new_user

    except Exception:
        db.rollback()
        raise


def login_user(db: Session, email: str, password: str):
    # Find user by email
    user = db.query(User).filter(
        User.email == email
    ).first()

    if not user:
        return None

    # Verify password
    if not verify_password(password, user.hashed_password):
        return None

    # Generate JWT access token
    access_token = create_access_token(
        data={"sub": str(user.id)}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
