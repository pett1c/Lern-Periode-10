from src.models.database import initialize_database
from src.views.gui import MusicApp

def main():
	"""
	Main function for starting the app.
	"""

	print("Database initialization...")
	initialize_database()
	app = MusicApp()
	app.mainloop()

if __name__ == "__main__":
	main()