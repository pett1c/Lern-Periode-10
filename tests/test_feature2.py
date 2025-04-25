from src.controllers.recommendation import get_recommendation, get_available_moods, get_available_tempos
from src.models.database import initialize_database

initialize_database()

print("\nAvailable moods in database:")
moods = get_available_moods()
print(", ".join(moods))

print("\nAvailable tempos in database:")
tempos = get_available_tempos()
print(", ".join(tempos))

test_cases = [
	("happy", "fast"),
	("melancholic", "slow"),
	("energetic", "fast"),
	("romantic", "fast")
]

print("\nTesting recommendation algorithm:")
for mood, tempo in test_cases:
	print(f"\nFor {mood} mood and {tempo} tempo:")
	recommendation = get_recommendation(mood, tempo)

	if recommendation:
		print(f"We are recommending you {recommendation['title']} - {recommendation['artist']}, because of {recommendation['mood']} mood and {recommendation['tempo']} tempo.")
	else:
		print("Database is empty.")

print("\nRandom recommendation without choosing preferences:")
random_recommendation = get_recommendation(None, None)
if random_recommendation:
		print(f"We are recommending you {recommendation['title']} - {recommendation['artist']}, because of {recommendation['mood']} mood and {recommendation['tempo']} tempo.")
else:
		print("Database is empty.")