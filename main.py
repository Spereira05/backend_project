from fastapi import FastAPI

import mangadex

app=FastAPI()

async def get_mangadex_data():
    data=mangadex.Manga()

    response_string="<h1>Manga Data</h1>"
    for Manga in data:
        response_string += f"<p>{Manga['title']}</p>"
        
    return response_string


    