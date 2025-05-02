
import customtkinter as ctk
from src.controllers.recommendation import get_available_moods, get_available_tempos, get_recommendation
from src.models.database import initialize_database
from src.controllers.feedback import save_feedback

class MusicApp(ctk.CTk):
	def __init__(self):
		super().__init__()

		initialize_database()

		self.title("MMMood")
		self.geometry("500x400")

		self.moods = get_available_moods()
		self.tempos = get_available_tempos()

		self.create_widgets()

		self.current_song = None

	def create_widgets(self):
		# Title
		ctk.CTkLabel(self, text="MMMood - reccommendation system", font=("Arial", 18)).pack(pady=10)

		# Mood selection
		mood_frame = ctk.CTkFrame(self)
		mood_frame.pack(pady=5, padx=10, fill="x")

		ctk.CTkLabel(mood_frame, text="Select mood:").pack(side="left", padx=10)
		self.mood_var = ctk.StringVar(value=self.moods[0] if self.moods else "")
		mood_menu = ctk.CTkComboBox(mood_frame, values=self.moods, variable=self.mood_var, width=150)
		mood_menu.pack(side="right", padx=10)

		# Tempo selection
		tempo_frame = ctk.CTkFrame(self)
		tempo_frame.pack(pady=5, padx=10, fill="x")

		ctk.CTkLabel(tempo_frame, text="Select tempo:").pack(side="left", padx=10)
		self.tempo_var = ctk.StringVar(value=self.tempos[0] if self.tempos else "")
		tempo_menu = ctk.CTkComboBox(tempo_frame, values=self.tempos, variable=self.tempo_var, width=150)
		tempo_menu.pack(side="right", padx=10)

		# Get recommendation button
		ctk.CTkButton(self, text="Get Recommendation", command=self.get_recommendation).pack(pady=10)

		# Result frame
		self.result_frame = ctk.CTkFrame(self)
		self.result_frame.pack(pady=10, padx=10, fill="both", expand=True)

		self.result_label = ctk.CTkLabel(self.result_frame, text="Recommendation will appear here", font=("Arial", 14))
		self.result_label.pack(pady=20)

		# Rating frame
		rating_frame = ctk.CTkFrame(self)
		rating_frame.pack(pady=10, padx=10, fill="x")

		ctk.CTkLabel(rating_frame, text="Rating:").pack(side="left", padx=10)

		# Radio buttons for rating
		self.rating_var = ctk.IntVar(value=0)
		rating_buttons = ctk.CTkFrame(rating_frame)
		rating_buttons.pack(side="right")

		for i in range(1, 6):
			ctk.CTkRadioButton(
				rating_buttons,
				text=str(i),
				variable=self.rating_var,
				value=i,
			).pack(side="left", padx=5)
		
		# Feedback send button
		self.feedback_button = ctk.CTkButton(self, text="Send Feedback", command=self.submit_feedback)
		self.feedback_button.pack(pady=10)
		self.feedback_button.configure(state="disabled")
	
	def get_recommendation(self):
		"""
		Get a song recommendation
		"""

		mood = self.mood_var.get()
		tempo = self.tempo_var.get()

		self.current_song = get_recommendation(mood, tempo)

		if self.current_song:
			text = f"Recommendation: \n{self.current_song['title']} by {self.current_song['artist']}\n"
			text += f"Genre: {self.current_song['genre']}\n"
			text += f"Mood: {self.current_song['mood']}, Tempo: {self.current_song['tempo']}"

			self.result_label.configure(text=text)
			self.feedback_button.configure(state="normal")
		else:
			self.result_label.configure(text="No recommendation found")
			self.feedback_button.configure(state="disabled")
	
	def submit_feedback(self):
		"""
		Sending feedback
		"""
		if self.current_song and self.rating_var.get() > 0:
			rating = self.rating_var.get()
			success = save_feedback(self.current_song['id'], rating)

			if success:
				message_window = ctk.CTkToplevel(self)
				message_window.title("Feedback sent")
				message_window.geometry("300x100")

				ctk.CTkLabel(
					message_window,
					text=f"Thank you for your rating! \nRating: {rating}/5"
				).pack(pady=30)

				self.rating_var.set(0)
	
if __name__ == "__main__":
	app = MusicApp()
	app.mainloop()

