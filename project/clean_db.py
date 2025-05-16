import pymongo
import re

# connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["music_db"]
collection = db["songs"]

# function to check if a genre is normally written
def is_valid_genre(genre):
    if not genre or genre.lower() == "unknown":
        return False
    # allow only lowercase letters, spaces, and simple phrases (no commas or special chars)
    return bool(re.match(r'^[a-z\s]+$', genre.lower()))

# function to check if artist or song is valid (no "Unknown" or malformed data)
def is_valid_text(text):
    if not text or "unknown" in text.lower():
        return False
    # disallow commas, excessive special chars, or malformed patterns
    return bool(re.match(r'^[a-zA-Z\s\-\']+$', text))

# function to clean the database
def clean_database():
    # fetch all documents
    documents = list(collection.find())
    cleaned_data = []

    for doc in documents:
        genre = str(doc.get("Genre", "")).strip()
        if not is_valid_genre(genre):
            continue

        artist = str(doc.get("artist", "")).strip()
        if not is_valid_text(artist):
            continue

        song = str(doc.get("song", "")).strip()
        if not is_valid_text(song):
            continue

        emotion = str(doc.get("emotion", "")).strip().lower()
        if emotion in ["true", "angry", "thirst", "pink"] or not emotion:
            continue

        try:
            popularity = float(doc.get("Popularity", 0))
            if not (0 <= popularity <= 100):
                continue
        except (ValueError, TypeError):
            continue

        try:
            tempo = float(doc.get("Tempo", 0))
            if not (33 <= tempo <= 200):
                continue
        except (ValueError, TypeError):
            continue

        try:
            energy = float(doc.get("Energy", 0))
            if not (0 <= energy <= 100):
                continue
        except (ValueError, TypeError):
            continue

        # create cleaned document
        cleaned_doc = {
            "title": song,
            "artist": artist,
            "Genre": genre,
            "emotion": emotion,
            "Popularity": popularity,
            "Tempo": tempo,
            "Energy": energy
        }
        cleaned_data.append(cleaned_doc)

    # drop existing collection and insert cleaned data
    collection.drop()
    if cleaned_data:
        collection.insert_many(cleaned_data)
        print(f"Cleaned and inserted {len(cleaned_data)} valid documents.")
    else:
        print("No valid data to insert after cleaning.")

# main
if __name__ == "__main__":
    clean_database()