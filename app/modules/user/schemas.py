from pydantic import BaseModel

class User(BaseModel):
    email: str
    username: str | None = None
    hashed_password: str  # only used internally for DB creation

class UserInDB(User):
    pass  # optional, could be used for internal DB operations

class UserOut(BaseModel):
    email: str
    username: str | None = None  # safe to expose to clients

from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    username: str | None = None

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    username: str | None = None
    email: str | None = None
    password: str | None = None
