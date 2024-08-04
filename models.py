from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(15), nullable=False)
    description = Column(String(50), nullable=True)
    create_date = Column(DateTime, nullable=True)
    
# MariaDB 에서는 VARCHAR와 String 을 사용할 때 크기를 명시해줘야 함