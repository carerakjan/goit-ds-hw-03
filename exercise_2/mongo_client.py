import certifi
from pymongo import MongoClient
from pymongo.server_api import ServerApi

connection_string = ""

client = MongoClient(connection_string, server_api=ServerApi("1"), tlsCAFile=certifi.where())
