import json


def save(file_name, data):
    with open(file_name, mode="w", encoding="utf-8") as file:
        json.dump(data, file)


def load(file_name):
    with open(file_name, mode="r", encoding="utf-8") as file:
        return json.load(file)
