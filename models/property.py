from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Property(BaseModel):
    name: Optional[str]
    address: Optional[str]
    price: float
    year: Optional[datetime]
    id_owner: Optional[str]


class Property_price(BaseModel):
    price: float
