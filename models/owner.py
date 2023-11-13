from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Owner(BaseModel):
    name: Optional[str]
    address: Optional[str]
    photo: Optional[str]
    birthday: Optional[datetime]
