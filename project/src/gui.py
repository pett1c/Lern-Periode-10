import tkinter as tk
from db import get_emotions, update_rating
from recommender import get_recommendations

class MusicRecommenderGUI:
    def __init__(self, master):
        self.master = master
        self.emotions = get_emotions()
        self.current_emotion = tk.StringVar()
        self.current_emotion.set(self.emotions[0])

        # emotion selector area
        emotion_label = tk.Label(master, text="Select Emotion:")
        emotion_label.pack()
        emotion_menu = tk.OptionMenu(master, self.current_emotion, *self.emotions)
        emotion_menu.pack()
        get_button = tk.Button(master, text="Get Recommendations", command=self.display_recommendations)
        get_button.pack()

        # frame that shows recommendations
        self.recommendations_frame = tk.Frame(master)
        self.recommendations_frame.pack()

    def display_recommendations(self):
        # clearing old recommendations
        for widget in self.recommendations_frame.winfo_children():
            widget.destroy()

        # getting new recommendations
        emotion = self.current_emotion.get()
        recommendations = get_recommendations(emotion)

        # showing tracks with rating buttons
        for track in recommendations:
            track_frame = tk.Frame(self.recommendations_frame)
            track_label = tk.Label(track_frame, text=f"{track['title']} by {track['artist']}")
            yes_button = tk.Button(track_frame, text="Yes", command=lambda t=track: self.rate_track(t['_id'], "yes"))
            no_button = tk.Button(track_frame, text="No", command=lambda t=track: self.rate_track(t['_id'], "no"))
            track_label.pack(side=tk.LEFT)
            yes_button.pack(side=tk.LEFT)
            no_button.pack(side=tk.LEFT)
            track_frame.pack()

    def rate_track(self, track_id, rating):
        # save the rating to the database
        update_rating(track_id, rating)
        print(f"Rated {rating} for track {track_id}")