from pydantic import BaseModel
from typing import Optional


class UserAuth(BaseModel):
    username: str
    password: str


class UserUpdate(BaseModel):
    username: Optional[str]
    password: Optional[str]


class User(BaseModel):
    username: str
    id: int
    token: str
