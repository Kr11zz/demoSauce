import uvicorn
from fastapi import FastAPI
import api_data
from models.User_Model import UserModel as model

app= FastAPI()

@app.get("/")
def index():
    return{
        "message":"Hello world!"
    }



@app.get("/api/users/{loginID}", response_model=model)
async def userGetter(loginID:str):
    user = await api_data.get_userByLogin(loginID)
    return user.dict()


if __name__== "__main__":
    uvicorn.run(app)