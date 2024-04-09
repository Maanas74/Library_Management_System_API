from pymongo import MongoClient

uri = MongoClient("mongodb+srv://Maanas:%40123@librarymanagementsystem.38wcnwv.mongodb.net/")
db = uri.Library_Management
collection = db["Students"]