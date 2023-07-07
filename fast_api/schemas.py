from pydantic import BaseModel

class MsgCreate(BaseModel):
    author: str
    content: str


class MsgEdit(BaseModel):
    id: int
    content: str