from typing import Optional

from pydantic import BaseModel


class PropertyTrace(BaseModel):
    data_sale: str
    name: str
    value: float
    tax: float
    id_property: Optional[str]
