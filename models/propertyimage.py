from pydantic import BaseModel
from typing import Optional


class PropertyImage(BaseModel):
    id_property: str
    file: str
    enabled: Optional[bool]
