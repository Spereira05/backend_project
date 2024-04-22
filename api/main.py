import logging
from fastapi import FastAPI, HTTPException
import requests

from api.models import Manga

app=FastAPI()

@app.get("/all_manga", response_model= list[Manga])
async def read_pall_manga():
    try:    
        response = requests.get("https://api.myanimelist.net/v2/manga/all")
        requests.raise_for_status()
    except requests.exceptions.HTTPError as e:
        logging.error(f"Error while fetching mangas: {e}")
        raise HTTPException(status_code=response.status_code, detail=str(e))
    return [Manga(**manga) for manga  in response.json()]

    