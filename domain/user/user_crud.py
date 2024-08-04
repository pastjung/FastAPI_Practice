from models import User
from sqlalchemy.orm import Session
from fastapi import HTTPException


def get_user_list(db: Session):
    # 데이터베이스에서 모든 사용자 찾기
    _user_list = db.query(User)\
        .order_by(User.id.desc())\
        .all()
    return _user_list

def create_user(user:User, db: Session):
    db_user = User(id=user.id, 
                   name=user.name, 
                   description=user.description, 
                   create_date=user.create_date
    )
    # 데이터베이스에 사용자 등록
    db.add(db_user)
    db.commit()
    
    return db_user

def update_user(user:User, db: Session):
    # 데이터베이스에서 사용자 찾기
    db_user = db.query(User)\
        .filter(User.id == user.id)\
        .first()
    
    # 사용자가 존재하지 않을 경우 404 에러 반환
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    # 사용자 정보 업데이트
    db_user.name = user.name
    db_user.description = user.description
    
    # 변경 사항 커밋
    db.commit()
    
    # 변경된 객체 반환
    db.refresh(db_user)
    return db_user

def delete_user(user_id:int, db: Session):
    # 데이터베이스에서 사용자 찾기
    db_user = db.query(User)\
        .filter(User.id == user_id)\
        .first()
    
    # 사용자가 존재하지 않을 경우 404 에러 반환
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # 사용자 삭제
    db.delete(db_user)
    
    # 변경 사항 커밋
    db.commit()