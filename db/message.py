from pydantic import BaseModel

class Message(BaseModel):
    id: int
    author: str
    content: str