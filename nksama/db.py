import pymongo
from nksama import log
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

MONGO_URL = "mongodb+srv://Music:Music@cluster0.f9x4i.mongodb.net/Cluster0?retryWrites=true&w=majority"

log.info("Initializing MongoDB client")
database = pymongo.MongoClient(MONGO_URL)["notes"]["notes"]
mongo_client = MongoClient(MONGO_URL)
db = mongo_client.nanamori
