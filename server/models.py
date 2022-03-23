from pydantic import BaseModel
from typing import Optional


# ---------- Data models: ---------------------------------------

class Query(BaseModel):
    api: str
    content: dict
    roadmap: Optional[list] = None

class GraphResponse(BaseModel):
    content: dict
    roadmap: Optional[list] = None