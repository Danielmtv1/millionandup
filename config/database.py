import os
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorGridFSBucket

mongo_user = os.environ.get("MONGO_USER")
mongo_password = os.environ.get("MONGO_PASSWORD")
mongo_host = os.environ.get("MONGO_HOST")

uri = f"mongodb+srv://{mongo_user}:{mongo_password}@{mongo_host}/?retryWrites=true&w=majority"

client = AsyncIOMotorClient(uri)


db = client.challenge_million_up_db

fs = AsyncIOMotorGridFSBucket(db, bucket_name="atachments")
attachments = db.get_collection("attachments.files")

collection_owner = db["owner_collection"]
collection_property = db["property_collection"]
collection_property_image = db["property_image_collection"]
collection_property_trace = db["property_trace_collection"]
