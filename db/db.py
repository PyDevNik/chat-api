from pymongo import MongoClient
from .config import URL, DB_NAME, MESSAGES, ID_LENGTH
from .message import Message
import random
from typing import List

class DB:
    def __init__(self) -> None:
        self.__client = MongoClient(URL)
        self._database = self.__client.get_database(DB_NAME)
        self._messages = self._database.get_collection(MESSAGES)
        self._id_length = ID_LENGTH
        
    def generate_id(self) -> str:
        def generate():
            return random.randint(int(f"1{'0'*(self._id_length-1)}"), int('9'*self._id_length))
        id = generate()
        messages = self.get_all_messages()
        while id in messages:
            id = generate()
        return id
    
    def get_all_messages(self) -> List[Message]:
        return [Message(**message) for message in list(self._messages.find({}))]
    
    def get_message(self, message_id: int) -> Message:
        message = self._messages.find_one({"id": message_id})
        return Message(**message) if message else None

    def add_message(self, msg: Message) -> None:
        self._messages.insert_one(msg.dict())

    def edit_message(self, msg: Message) -> None:
        filter = {"id": msg.id}
        self._messages.update_one(filter, {"$set": msg.dict()})

    def delete_message(self, msg_id: int) -> None:
        filter = {"id": msg_id}
        self._messages.delete_one(filter)