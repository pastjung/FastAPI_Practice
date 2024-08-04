from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# MariaDB Docker 컨테이너에서 도커 호스트의 IP를 사용하여 연결
# DB_URI = 'mysql+pymysql://root:12345678@localhost:3306/fastapi_sample'
DB_URI = 'mysql+pymysql://root:12345678@172.17.0.2:3306/fastapi_sample'

# DB 커넥션 풀 생성
'''
engine = create_engine(
    DB_URI, connect_args={"check_same_thread": False}
)
'''
engine = create_engine(DB_URI)
# DB 접속을 위한 클래스
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base 클래스는 DB 모델 구성할 때 사용
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()