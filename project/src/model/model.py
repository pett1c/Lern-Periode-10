import random
from pymongo import MongoClient

# connect to the mongodb
client = MongoClient('localhost', 27017)
db = client['music_db']
collection = db['songs']

def get_emotions():
    """return a list of all available emotions from the database"""
    return collection.distinct("emotion")

def get_tracks(emotion, user_rating=None):
    """return tracks for a given emotion and optional user_rating ('yes', 'no', or None)"""
    query = {"emotion": emotion}
    if user_rating is not None:
        query["user_rating"] = user_rating
    else:
        query["user_rating"] = {"$exists": False}
    return list(collection.find(query))

def update_track_rating(track_id, rating):
    """update the user_rating for a track by its _id"""
    collection.update_one({"_id": track_id}, {"$set": {"user_rating": rating}})

def get_recommendations(emotion, num_recommendations=4):
    """get up to num_recommendations tracks for a given emotion, prioritizing highly rated tracks"""
    yes_tracks = get_tracks(emotion, "yes")
    neutral_tracks = get_tracks(emotion, None)
    no_tracks = get_tracks(emotion, "no")

    recommendations = []
    remaining = num_recommendations

    if yes_tracks:
        num_yes = min(len(yes_tracks), remaining)
        recommendations.extend(random.sample(yes_tracks, num_yes))
        remaining -= num_yes

    # if we need more, add neutral tracks
    if remaining > 0 and neutral_tracks:
        num_neutral = min(len(neutral_tracks), remaining)
        recommendations.extend(random.sample(neutral_tracks, num_neutral))
        remaining -= num_neutral

    # if we need more, add tracks with 'no' (1 of 10 chance)
    if remaining > 0 and no_tracks and random.random() < 0.1:
        num_no = min(len(no_tracks), remaining)
        recommendations.extend(random.sample(no_tracks, num_no))

    if remaining > 0 and neutral_tracks:
        recommendations.extend(random.sample(neutral_tracks, remaining))

    return recommendations[:num_recommendations] 