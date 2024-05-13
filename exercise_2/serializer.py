import json
from collections import UserList
from typing import Protocol

class Serializable(Protocol):
    def serialize(self) -> dict:
        pass


class Serializer(UserList):
    def __init__(self, initlist=list[Serializable]):
        super().__init__(initlist=initlist)

    def save(self, file_name):
        with open(file_name, mode="w", encoding="utf-8") as file:
            json.dump([it.serialize() for it in self.data], file)


    def load(file_name):
        with open(file_name, mode="r", encoding="utf-8") as file:
            return json.load(file)