from pydantic import BaseModel

class Anime(BaseModel):
    id: int
    title: str
    synopsis: str