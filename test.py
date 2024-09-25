from fastapi import FastAPI, Header
import math
import json
import httpx

from schema import User

app = FastAPI()

@app.get("/get_user/{user_prenom}/{user_nom}")
async def recupere_user(user_nom: str, user_prenom: str): # a mettre dans l'URL
    return {
        "nom": user_nom,
        "prenom": user_prenom,
    }

@app.post("/create_user/")
async def create_user(user: User):
    user_nom = user.user_nom
    user_prenom = user.user_prenom
    return {
        "nom": user_nom,
        "prenom": user_prenom,
    }

@app.get("/get_ville/{ville_nom}")
async def recupere_ville(codePostal: str): # a mettre dans l'URL
    url = f'https://geo.api.gouv.fr/communes?codePostal={codePostal}'
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    
    if response.status_code == 200: # succes
        return response.json()  
    else:
        return {"error": "probleme avec API externe"}