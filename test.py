from fastapi import FastAPI, Header
import math
import json

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

