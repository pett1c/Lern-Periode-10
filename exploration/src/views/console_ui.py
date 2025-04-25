from src.controllers.recommendation import get_recommendation, get_available_moods, get_available_tempos

def display_welcome():
	"""
	Shows an welcome message by starting the app.
	"""
	print("\n" + "=" * 60)
	print("    Musical Recommendation Service - MMMood")
	print("=" * 60)
	print("This service helps pick up music for your mood and preferences.")
	print("=" * 60 + "\n")

def display_available_options():
	"""
	Shows available options of moods and tempos from database.
	"""
	moods = get_available_moods()
	tempos = get_available_tempos()

	print("\nAvailable moods:")
	for i, mood in enumerate(moods, 1):
		print(f"{i}. {mood}")

	print("\nAvailable tempos:")
	for i, tempo in enumerate(tempos, 1):
		print(f"{i}. {tempo}")
	
	return moods, tempos

def get_user_preferences():
	"""
	Asking user for his preferences by mood and tempo.
	"""

	moods, tempos = display_available_options()

	mood_choice = None
	while mood_choice is None:
		try:
			choice = int(input("\nChoose number of preferred mood: "))
			if 1 <= choice <= len(moods):
				mood_choice = moods[choice - 1]
			else:
				print("Error: choose number from the list.")
		except ValueError:
			print("Error: enter number.")

	tempo_choice = None
	while tempo_choice is None:
		try:
			choice = int(input("\nChoose number of preferred tempo: "))
			if 1 <= choice <= len(tempos):
				tempo_choice = tempos[choice - 1]
			else:
				print("Error: choose number from the list.")
		except ValueError:
			print("Error: enter number.")
	
	return mood_choice, tempo_choice

def display_recommendation(song):
	"""
	Shows an information about recommendated song.
	"""

	if song:
		print("\n" + "-" * 50)
		print(f"RECOMMENDATION FOR YOU:")
		print("-" * 50)
		print(f"Title: {song['title']}")
		print(f"Artist: {song['artist']}")
		print(f"Genre: {song['genre']}")
		print(f"Mood: {song['mood']}")
		print(f"Tempo: {song['tempo']}")
		print("-" * 50)
	else:
		print("\nUnfortunately, we're cannot provide you any song =()")

def run_interface():
	"""
	Main function for setup the UI.
	"""
	display_welcome()

	while True:
		mood, tempo = get_user_preferences()
		print(f"\nYou choosed: {mood} mood and {tempo} tempo.")

		recommendation = get_recommendation(mood, tempo)
		display_recommendation(recommendation)

		choice = input("\nDo you wan another one recommendation? (yes / no):" ).lower()
		if choice != 'yes' and choice != 'y':
			print("\nThank you for using MMMood! Goodbye!")
			break