from pydantic import BaseModel


class UserAuth(BaseModel):
    username: str
    password: str


class User(BaseModel):
    username: str
    id: int
    token: str
