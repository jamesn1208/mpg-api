from pydantic import BaseModel


class NotYetImplemented(BaseModel):
    detail: str


class ActionResponse(BaseModel):
    message: str
    success: bool
