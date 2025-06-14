from pymongo import MongoClient
from dotenv import load_dotenv
import os

# load environment
load_dotenv()

# env variable for mongo
MONGO_URI = os.getenv('MONGO_URI')

# stablish client, databases and collections

client = MongoClient(MONGO_URI)

# database
db = client['backend_labs']

# collections

users_collection = db['users_collection']