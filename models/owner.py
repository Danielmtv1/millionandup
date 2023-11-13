from pydantic import BaseModel
from datetime import datetime


class Owner(BaseModel):
    name: str
    address: str
    photo: str
    birthday: datetime
