
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorGridFSBucket

uri = "mongodb+srv://admin:admin123@challenge-million-up.khx0rsj.mongodb.net/?retryWrites=true&w=majority" # noqa

client = AsyncIOMotorClient(uri)


db = client.challenge_million_up_db

fs = AsyncIOMotorGridFSBucket(db, bucket_name="atachments")
attachments = db.get_collection("attachments.files")

collection_owner = db["owner_collection"]
collection_property = db["property_collection"]
collection_property_image = db["property_image_collection"]
collection_property_trace = db["property_trace_collection"]
