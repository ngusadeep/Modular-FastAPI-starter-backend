from sqlalchemy.orm import Session
from sqlalchemy.orm import Mapped, mapped_column
from app.modules.user.schemas import  UserInDB
from app.db.database import Base
from passlib.context import CryptContext
from sqlalchemy import  String

# Password hashing configuration
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    username: Mapped[str | None] = mapped_column(String, nullable=True)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(db: Session, email: str, password: str) -> UserInDB | None:
    user = get_by_email(db, email)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

def get_by_email(db: Session, email: str) -> UserInDB | None:
    return db.query(UserModel).filter(UserModel.email == email).first()
