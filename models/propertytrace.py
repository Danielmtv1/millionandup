from pydantic import BaseModel
from typing import Optional


class PropertyTrace(BaseModel):
    data_sale: str
    name: str
    value: float
    tax: float
    id_property: Optional[str]
