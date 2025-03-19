from fastapi import APIRouter, Depends, HTTPException, Path
from pydantic import BaseModel, Field
from models import Users
from database import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status
from .auth import get_current_user


router = APIRouter(prefix="/user", tags=["users"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


@router.get("/", status_code=status.HTTP_200_OK)
async def get_user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authenication Failed")

    return db.query(Users).all()
