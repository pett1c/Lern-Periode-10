from src.models.database import initialize_database, get_songs_by_criteria

initialize_database()

print("\nSongs with happy mood:")
happy_songs = get_songs_by_criteria(mood="happy")
for song in happy_songs:
	print(f"{song['title']} - {song['artist']}")

print("\nSongs with slow tempo:")
slow_songs = get_songs_by_criteria(tempo="slow")
for song in slow_songs:
	print(f"{song['title']} - {song['artist']}")

print("\nSongs with fast tempo and energetic mood:")
fast_energetic_songs = get_songs_by_criteria(tempo="fast", mood="energetic")
for song in fast_energetic_songs:
	print(f"{song['title']} - {song['artist']}")

print("\nAll songs in database:")
all_songs = get_songs_by_criteria()
for song in all_songs:
	print(f"{song['title']} - {song['artist']} ({song['mood']}, {song['tempo']})")