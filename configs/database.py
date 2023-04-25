from pymongo import MongoClient
import os

client = MongoClient("mongodb+srv://moisestabar013:R7qH4a7Vs1jZDzoL@cluster0.bujakpc.mongodb.net/?retryWrites=true&w=majority")

db = client['urls']