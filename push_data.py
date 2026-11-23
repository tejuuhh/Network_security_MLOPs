import pymongo
from pymongo import MongoClient
uri = "mongodb+srv://tejswinikorade:Teju1708@cluster0.ij6lg8y.mongodb.net/"
client = MongoClient(uri)
try:
    client.admin.command("ping")
    print("Connected successfully")
    client.close()
except Exception as e:
    raise Exception(
        "The following error occurred: ", e)