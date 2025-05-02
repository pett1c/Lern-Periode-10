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
		genre TEXT NOT NULL,
		release_year INTEGER,
		vocal_type TEXT,
		language TEXT,
		popularity INTEGER
	)
	''')

	cursor.execute('''
	CREATE TABLE IF NOT EXISTS feedback (
		id INTEGER PRIMARY KEY,
		song_id INTEGER NOT NULL,
		rating INTEGER NOT NULL,
		FOREIGN KEY (song_id) REFERENCES songs (id)
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
            ('Happy', 'Pharrell Williams', 'happy', 'middle', 'pop', 2013, 'vocal', 'english', 9),
            ('Sad But True', 'Metallica', 'dark', 'slow', 'metal', 1991, 'vocal', 'english', 8),
            ('Dancing Queen', 'ABBA', 'happy', 'fast', 'disco', 1976, 'vocal', 'english', 9),
            ('Nothing Else Matters', 'Metallica', 'melancholic', 'slow', 'rock', 1991, 'vocal', 'english', 9),
            ('Eye of the Tiger', 'Survivor', 'energetic', 'fast', 'rock', 1982, 'vocal', 'english', 8),
            ('The Sounds of Silence', 'Simon & Garfunkel', 'melancholic', 'slow', 'folk', 1964, 'vocal', 'english', 8),
            ('Bohemian Rhapsody', 'Queen', 'complex', 'varied', 'rock', 1975, 'vocal', 'english', 10),
            ('Get Lucky', 'Daft Punk ft. Pharrell Williams', 'groovy', 'middle', 'dance', 2013, 'vocal', 'english', 9),
            ('Californication', 'Red Hot Chili Peppers', 'reflective', 'middle', 'alternative', 1999, 'vocal', 'english', 8),
            ('Nocturne Op. 9 No. 2', 'Frédéric Chopin', 'peaceful', 'slow', 'classical', 1830, 'instrumental', 'none', 7),
            ('Für Elise', 'Ludwig van Beethoven', 'gentle', 'middle', 'classical', 1810, 'instrumental', 'none', 8),
            ('Don\'t Stop Me Now', 'Queen', 'euphoric', 'fast', 'rock', 1978, 'vocal', 'english', 9),
            ('Smells Like Teen Spirit', 'Nirvana', 'angry', 'fast', 'grunge', 1991, 'vocal', 'english', 9),
            ('Yesterday', 'The Beatles', 'sad', 'slow', 'pop', 1965, 'vocal', 'english', 9),
            ('Summer', 'Antonio Vivaldi', 'bright', 'fast', 'classical', 1723, 'instrumental', 'none', 8),
            ('Shape of You', 'Ed Sheeran', 'romantic', 'middle', 'pop', 2017, 'vocal', 'english', 9),
            ('Hallelujah', 'Leonard Cohen', 'spiritual', 'slow', 'folk', 1984, 'vocal', 'english', 8),
            ('Moonlight Sonata', 'Ludwig van Beethoven', 'mysterious', 'slow', 'classical', 1801, 'instrumental', 'none', 8),
            ('Africa', 'Toto', 'nostalgic', 'middle', 'pop rock', 1982, 'vocal', 'english', 8),
            ('Toxic', 'Britney Spears', 'seductive', 'fast', 'pop', 2003, 'vocal', 'english', 8)

		]
		cursor.executemany(
			"INSERT INTO songs (title, artist, mood, tempo, genre, release_year, vocal_type, language, popularity) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
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