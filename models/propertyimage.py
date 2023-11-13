from typing import Optional

from pydantic import BaseModel


class PropertyImage(BaseModel):
    id_property: str
    file: str
    enabled: Optional[bool]
