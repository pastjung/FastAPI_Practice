from fastapi import APIRouter

from database import SessionLocal

router = APIRouter(
    prefix="/api/user",
)

from database import get_db
from fastapi import Depends
from sqlalchemy.orm import Session

from domain.user import user_schema, user_crud

@router.get("/list", response_model=list[user_schema.User])
def user_list(db: Session = Depends(get_db)):
    _user_list = user_crud.get_user_list(db)
    return _user_list


@router.post("/create")
def user_create(user: user_schema.User, db: Session = Depends(get_db)):
    db_user = user_crud.create_user(user, db)
    #db.refresh(db_user)
    return db_user

@router.put("/update")
def user_update(user: user_schema.User, db: Session = Depends(get_db)):
    db_user = user_crud.update_user(user, db)
    return db_user

@router.delete("/delete/user_id/{user_id}")
def user_delete(user_id: int, db: Session = Depends(get_db)):
    user_crud.delete_user(user_id, db)