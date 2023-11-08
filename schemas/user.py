from pydantic import BaseModel

# User Model
class User(BaseModel):
    email:str
    password:str
