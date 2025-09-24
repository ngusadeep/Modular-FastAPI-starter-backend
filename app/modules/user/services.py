from sqlalchemy.orm import Session
from app.modules.user.models import UserModel
from app.modules.auth import services  # for password hashing

def update_user(db: Session, user_id: int, data: dict):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        return None
    if data.get("username"):
        user.username = data["username"]
    if data.get("email"):
        user.email = data["email"]
    if data.get("password"):
        user.hashed_password = services.get_password_hash(data["password"])
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
