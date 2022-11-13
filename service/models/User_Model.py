from pydantic import BaseModel

class UserModel(BaseModel):
    login: str
    id: str
    node_id: str
    avatar_url: str