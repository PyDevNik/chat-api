import os, sys
sys.path.append(os.path.join(sys.path[0], '..'))

from fastapi import FastAPI, Body
from fastapi.responses import JSONResponse
from db.db import DB
from db.message import Message
from fast_api.schemas import MsgCreate, MsgEdit

app = FastAPI()
db = DB()

@app.get("/chat")
def all_messages():
    messages = db.get_all_messages()
    messages = [msg.dict() for msg in messages]
    return JSONResponse(messages)

@app.get("/chat/{message_id}")
def get_message(message_id: int):
    message = db.get_message(message_id)
    return JSONResponse(message.dict())

@app.post("/chat")
def add_message(message: MsgCreate = Body()):
    message = Message(id=db.generate_id(), **message.dict())
    db.add_message(message)
    return JSONResponse(message.dict())

@app.put("/chat")
def edit_message(message: MsgEdit = Body()):
    author = db.get_message(message.id).author
    message = Message(author=author, **message.dict())
    db.edit_message(message)
    return JSONResponse(message.dict())

@app.delete("/chat/{message_id}")
def delete_message(message_id: int):
    message = db.get_message(message_id)
    db.delete_message(message_id)
    return JSONResponse(message.dict())
