from sqlmodel import Session, select
from .model import User, UserInDB
from .auth import hash_password

def get_user_by_email(session: Session, email: str):
    statement = select(User).where(User.email == email)
    return session.exec(statement).first()

def create_user(session: Session, user: UserInDB):
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password)
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user
