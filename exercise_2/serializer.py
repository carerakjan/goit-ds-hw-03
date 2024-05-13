import json
from collections import UserList
from typing import Protocol, Callable

class Serializable(Protocol):
    def serialize(self) -> dict:
        pass


class Serializer(UserList):
    def __init__(self, initlist:list[Serializable]=None, factory:Callable[[dict], Serializable]=None):
        super().__init__(initlist=initlist)
        self.factory = factory or (lambda _: _)

    
    def to_json(self):
        return [it.serialize() for it in self.data]

    
    def save(self, file_name):
        with open(file_name, mode="w", encoding="utf-8") as file:
            json.dump(self.to_json(), file)


    def load(self, file_name):
        try:
            with open(file_name, mode="r", encoding="utf-8") as file:
                self.extend([self.factory(d) for d in json.load(file)])
        except FileNotFoundError:
            pass
        return self