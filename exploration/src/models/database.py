import sqlite3
import os

DATABASE_PATH = os.path.join('database', 'music_mood.db')

def create_tables():
	"""
	Creates necessary tables in database, if they don't exist yet.
	"""

	os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)
	conn = sqlite3.connect(DATABASE_PATH)
	cursor = conn.cursor()

	cursor.execute('''
	CREATE TABLE IF NOT EXISTS songs (
		id INTEGER PRIMARY KEY,
		title TEXT NOT NULL,
		artist TEXT NOT NULL,
		mood TEXT NOT NULL,
		tempo TEXT NOT NULL,
		genre TEXT NOT NULL
	)
	''')

	conn.commit()
	conn.close()

	print("Tables succesfully created.")

def insert_sample_data():
	"""
	Fulls database with test data, if table 'songs' is empty.
	"""
	conn = sqlite3.connect(DATABASE_PATH)
	cursor = conn.cursor()

	cursor.execute("SELECT COUNT(*) FROM songs")
	count = cursor.fetchone()[0]

	if count == 0:
		sample_songs = [
            ('Happy', 'Pharrell Williams', 'happy', 'middle', 'pop'),
            ('Sad But True', 'Metallica', 'dark', 'slow', 'metal'),
            ('Dancing Queen', 'ABBA', 'happy', 'fast', 'disco'),
            ('Nothing Else Matters', 'Metallica', 'melancholic', 'slow', 'rock'),
            ('Eye of the Tiger', 'Survivor', 'energetic', 'fast', 'rock')
		]
		cursor.executemany(
			"INSERT INTO songs (title, artist, mood, tempo, genre) VALUES (?, ?, ?, ?, ?)",
			sample_songs
		)

		conn.commit()
		print("Test data imported in database.")
	else:
		print("Database is already has data.")
	conn.close()

def initialize_database():
	"""
	Initializies database: creates tables and fulls it with test data.
	"""
	create_tables()
	insert_sample_data()

def get_songs_by_criteria(mood=None, tempo=None):
	"""
	Recieves a list of songs from database.
	"""
	conn = sqlite3.connect(DATABASE_PATH)
	conn.row_factory = sqlite3.Row
	cursor = conn.cursor()

	query = "SELECT * FROM songs WHERE 1=1"
	params = []

	if mood:
		query += " AND mood = ?"
		params.append(mood)
	
	if tempo:
		query += " AND tempo = ?"
		params.append(tempo)
	
	cursor.execute(query, params)
	results = [dict(row) for row in cursor.fetchall()]
	conn.close()

	return results