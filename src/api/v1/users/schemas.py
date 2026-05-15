from pydantic import BaseModel
from typing import Optional


class UserAuth(BaseModel):
    username: str
    password: str


class UserUpdate(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None


class User(BaseModel):
    id: int
    username: str
    token: str
