from pydantic import BaseModel
import datetime

class User(BaseModel):
    id : int
    name : str
    description : str | None = None
    create_date: datetime.datetime | None = None