from pymongo import MongoClient

# connecting to the mongodb
client = MongoClient('localhost', 27017)
db = client['music_db']
collection = db['songs']

def get_emotions():
    return collection.distinct("emotion")

def get_tracks(emotion, user_rating=None):
    query = {"emotion": emotion}
    if user_rating is not None:
        query["user_rating"] = user_rating
    else:
        query["user_rating"] = {"$exists": False}
    return list(collection.find(query))

def update_rating(track_id, rating):
    collection.update_one({"_id": track_id}, {"$set": {"user_rating": rating}})