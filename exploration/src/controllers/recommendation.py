from src.models.database import get_songs_by_criteria
import random

def get_recommendation(mood, tempo):
	"""
	Returns song recommendation on user preferences.
	"""
	matching_songs = get_songs_by_criteria(mood=mood, tempo=tempo)

	if not matching_songs:
		matching_songs = get_songs_by_criteria(mood=mood)
		if not matching_songs:
			matching_songs = get_songs_by_criteria(tempo=tempo)
			if not matching_songs:
				matching_songs = get_songs_by_criteria()
	
	if matching_songs:
		return random.choice(matching_songs)
	else:
		return None

def get_available_moods():
	"""
	Returns list of available moods in database.
	"""
	all_songs = get_songs_by_criteria()
	moods = set(song['mood'] for song in all_songs)

	return list(moods)

def get_available_tempos():
	"""
	Returns list of available tempos in database.
	"""
	all_songs = get_songs_by_criteria()
	tempos = set(song['tempo'] for song in all_songs)

	return list(tempos)