from pydantic import BaseModel

class User(BaseModel):
    user_nom: str
    user_prenom: str
