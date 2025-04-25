from src.models.database import initialize_database
from src.views.console_ui import run_interface

def main():
	"""
	Main function for starting the app.
	"""

	print("Database initialization...")
	initialize_database()

	run_interface()

if __name__ == "__main__":
	main()