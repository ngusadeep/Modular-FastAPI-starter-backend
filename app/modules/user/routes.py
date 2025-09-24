from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.modules.user import models, schemas, services
from app.db.database import get_db
from app.modules.auth.services import oauth2_scheme, verify_token

router = APIRouter()

# ---------------- Get current logged-in user ----------------
@router.get("/me", response_model=schemas.UserOut)
def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    email = payload.get("sub")
    user = db.query(models.UserModel).filter(models.UserModel.email == email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


# ---------------- List all users ----------------
@router.get("/", response_model=list[schemas.UserOut])
def list_users(db: Session = Depends(get_db)):
    users = db.query(models.UserModel).all()
    return users


# ---------------- Update logged-in user ----------------
@router.put("/me", response_model=schemas.UserOut)
def update_current_user(data: schemas.UserUpdate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    email = payload.get("sub")
    user = db.query(models.UserModel).filter(models.UserModel.email == email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    updated_user = services.update_user(db, user.id, data.dict(exclude_unset=True))
    return updated_user
