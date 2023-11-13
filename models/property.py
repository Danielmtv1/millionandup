from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Property(BaseModel):
    name: Optional[str]
    address: Optional[str]
    price: float
    year: Optional[datetime]
    id_owner: Optional[str]


class Property_price(BaseModel):
    price: float
