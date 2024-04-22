import pydantic
from pydantic import BaseModel

class Manga(BaseModel):
    id: int
    title: str
    type: str
    author: str

