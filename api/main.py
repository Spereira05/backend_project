import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging
import requests

from api.models import Anime

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.get("/anime/{id}/full")
async def get_anime_by_id(id):
    logger.info(f"Requisição para obter anime com ID {id}")
    response = requests.get(f"https://api.jikan.moe/v4/anime/{id}/full")
    if response.status_code == 200:
        anime_data = response.json()
        return anime_data
    else:
        raise HTTPException(status_code=404, detail="Anime não encontrado")

@app.get("/anime/{id}/news")
async def get_full_anime(id):
    logger.info(f"Requisição para obter notícias de anime com ID {id}")
    response = requests.get(f"https://api.jikan.moe/v4/anime/{id}/news")
    if response.status_code == 200:
        anime_data = response.json()
        return anime_data
    else:
        raise HTTPException(status_code=404, detail="Notícias não encontradas")

@app.get("/random/anime")
async def get_anime_episode_by_id():
    logger.info(f"Requisição para obter um anime alietório")
    response = requests.get(f"https://api.jikan.moe/v4/random/anime")
    if response.status_code == 200:
        episode_data = response.json()
        return episode_data
    else:
        raise HTTPException(status_code=404, detail="Episódio não encontrado")
    