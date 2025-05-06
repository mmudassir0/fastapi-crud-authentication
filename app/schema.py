from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserRead(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str|None = None

class HeroCreate(BaseModel):
    name: str
    secret_name: str
    age: int |None = None


class HeroRead(BaseModel):
    id: int
    name: str
    secret_name: str
    age: int |None = None
    team_id:int|None

class TeamCreate(BaseModel):
    name:str
    headquater:str
class TeamRead(BaseModel):
    id:int
    name:str
    headquater:str