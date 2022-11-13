from typing import Optional
import httpx
from models.User_Model import UserModel as model

async def get_userByLogin(loginID:str) -> Optional[model]:
    url= f"https://api.github.com/users/{loginID}"
    async with httpx.AsyncClient() as client:
        response: httpx.Response = await client.get(url)
        response.raise_for_status()
        data= response.json()
        user = model(**data)
        return user
    