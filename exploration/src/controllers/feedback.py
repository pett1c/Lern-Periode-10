import sqlite3
import os

DATABASE_PATH = os.path.join('database', 'music_mood.db')

def save_feedback(song_id, rating):
	"""
	Saves user rating for song
	"""
	conn = sqlite3.connect(DATABASE_PATH)
	cursor = conn.cursor()

	try:
		cursor.execute(
			"INSERT INTO feedback (song_id, rating) VALUES (?, ?)",
			(song_id, rating)
		)
		conn.commit()
		print(f"Saved rating: {song_id} song with {rating} rating.")
		return True
	except Exception as e:
		print(f"Error by rating saving: {e}")
		return False
	finally:
		conn.close()

def get_avg_rating(song_id):
	"""
	Returns average rating for any song
	"""
	conn = sqlite3.connect(DATABASE_PATH)
	cursor = conn.cursor()

	cursor.execute(
		"SELECT AVG(rating) FROM feedback WHERE song_id = ?",
		(song_id,)
	)

	avg_rating = cursor.fetchone()[0]
	conn.close()

	return avg_rating if avg_rating else 0