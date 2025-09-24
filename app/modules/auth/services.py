from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from app.core.config import settings

# JWT / Security settings
SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES
RESET_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


# --- Password hashing ---
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


# --- JWT Tokens ---
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta if expires_delta else timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or Expired Token.",
            headers={"WWW-Authenticate": "Bearer"},
        )

# --- Reset token ---
def create_reset_token(email: str):
    expires = timedelta(minutes=RESET_TOKEN_EXPIRE_MINUTES)
    return create_access_token({"sub": email}, expires_delta=expires)

from typing import Optional

def verify_reset_token(token: str) -> str:
    payload = verify_token(token)
    email: Optional[str] = payload.get("sub")

    if email is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired reset token",
        )

    return email
