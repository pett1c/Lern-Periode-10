import pandas as pd
import pymongo
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import customtkinter as ctk
from tkinter import messagebox
import pyperclip

# connect
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["music_db"]
collection = db["songs"]

# load data from mongodb
def load_data():
    data = collection.find()
    df = pd.DataFrame(list(data))
    return df

# prepare data for model
def prepare_data(df):
    emotion_encoder = LabelEncoder()
    genre_encoder = LabelEncoder()
    df['emotion_num'] = emotion_encoder.fit_transform(df['emotion'])
    df['genre_num'] = genre_encoder.fit_transform(df['Genre'])
    X = df[['Tempo', 'Energy', 'Popularity', 'genre_num']]
    y = df['emotion_num']
    return X, y, emotion_encoder, df

# train the model
def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)
    print(f"Model accuracy: {accuracy:.2f}")
    return model

# recommend songs
def recommend_songs(mood, model, emotion_encoder, df):
    try:
        print(f"Available emotions: {emotion_encoder.classes_}")
        print(f"Selected mood: {mood}")
        if mood not in emotion_encoder.classes_:
            raise ValueError(f"Mood '{mood}' not found in database emotions: {emotion_encoder.classes_}")
        mood_num = emotion_encoder.transform([mood])[0]
        X = df[['Tempo', 'Energy', 'Popularity', 'genre_num']]
        probs = model.predict_proba(X)
        mood_probs = probs[:, mood_num]
        df['mood_prob'] = mood_probs
        recommendations = df.sort_values(by=['mood_prob', 'Popularity'], ascending=False)
        top_songs = recommendations[['_id', 'title', 'artist', 'Genre', 'emotion', 'Popularity', 'Tempo', 'Energy']].head(4)  # Only 4 songs
        return top_songs
    except ValueError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# save feedback to mongodb
def save_feedback(song_id, rating):
    popularity_change = rating - 3
    collection.update_one({"_id": song_id}, {"$inc": {"Popularity": popularity_change}})
    print(f"Updated Popularity for song {song_id} by {popularity_change}")

# show mood selection screen
def show_mood_selection():
    for widget in app.winfo_children():
        widget.destroy()
    
    # title
    ctk.CTkLabel(app, text="MMMood", font=("Arial", 24, "bold")).pack(pady=20)
    
    # subtitle
    ctk.CTkLabel(app, text="choose your mood today:", font=("Arial", 12)).pack(pady=5)
    
    # mood grid
    mood_frame = ctk.CTkFrame(app)
    mood_frame.pack(pady=10)
    
    moods = [
        ("😃 joy", "joy"),
        ("😭 sadness", "sadness"),
        ("🎉 surprise", "surprise"),
        ("🤬 anger", "anger"),
        ("😱 fear", "fear")
    ]
    
    # split into rows (max 3 per row)
    for row in range((len(moods) + 2) // 3):
        row_frame = ctk.CTkFrame(mood_frame)
        row_frame.pack(pady=10)
        
        start_idx = row * 3
        end_idx = min(start_idx + 3, len(moods))
        for i in range(start_idx, end_idx):
            mood_text, mood_value = moods[i]
            mood_button = ctk.CTkFrame(row_frame, width=100, height=100)
            mood_button.pack(side="left", padx=10)
            
            parts = mood_text.split()
            emoji = parts[0] if parts else mood_text
            text = parts[1] if len(parts) > 1 else mood_text
            
            emoji_label = ctk.CTkLabel(mood_button, text=emoji, font=("Arial", 24))
            emoji_label.pack(pady=5)
            emoji_label.bind("<Button-1>", lambda e, m=mood_value: show_results(m))
            
            text_label = ctk.CTkLabel(mood_button, text=text, font=("Arial", 12))
            text_label.pack(pady=5)
            text_label.bind("<Button-1>", lambda e, m=mood_value: show_results(m))

# show results screen
def show_results(selected_mood):
    for widget in app.winfo_children():
        widget.destroy()
    
    # title and subtitle
    ctk.CTkLabel(app, text="MMMood", font=("Arial", 24, "bold")).pack(pady=10)
    ctk.CTkLabel(app, text="recommended you:", font=("Arial", 12)).pack()
    
    # song grid (2 rows, 2 columns)
    song_frame = ctk.CTkFrame(app)
    song_frame.pack(pady=10)
    
    recommendations = recommend_songs(selected_mood, model, emotion_encoder, df)
    if recommendations is not None:
        for i in range(min(4, len(recommendations))):
            row = recommendations.iloc[i]
            row_idx = i // 2
            col_idx = i % 2
            
            # song frame
            track_frame = ctk.CTkFrame(song_frame, width=150, height=150)
            track_frame.grid(row=row_idx, column=col_idx, padx=10, pady=10)
            
            # track name (click to copy)
            def copy_track(track=row['title'], artist=row['artist']):
                pyperclip.copy(f"{artist} - {track}")
                messagebox.showinfo("Copied", f"Copied: {artist} - {track}")
            
            track_label = ctk.CTkLabel(track_frame, text=row['title'].upper(), font=("Arial", 12, "bold"))
            track_label.pack(pady=2)
            track_label.bind("<Button-1>", lambda e, t=row['title'], a=row['artist']: copy_track(t, a))
            
            # artist
            artist_label = ctk.CTkLabel(track_frame, text=row['artist'], font=("Arial", 10))
            artist_label.pack(pady=2)
            
            # stars for rating with hover effect
            stars_frame = ctk.CTkFrame(track_frame)
            stars_frame.pack(pady=2)
            
            rating_var = ctk.StringVar(value="0")  # 0 means no rating selected
            star_labels = []
            for star in range(5):
                star_label = ctk.CTkLabel(stars_frame, text="☆", font=("Arial", 12), width=20)
                star_label.pack(side="left")
                star_labels.append(star_label)
            
            def update_stars(hovered_star=None, clicked=False):
                selected_rating = int(rating_var.get())
                for j in range(5):
                    if clicked and j < selected_rating:
                        star_labels[j].configure(text="★")
                    elif hovered_star is not None and j <= hovered_star:
                        star_labels[j].configure(text="★")
                    else:
                        star_labels[j].configure(text="☆")
            
            for star in range(5):
                star_labels[star].bind("<Enter>", lambda e, s=star: update_stars(hovered_star=s))
                star_labels[star].bind("<Leave>", lambda e: update_stars(hovered_star=None))
                star_labels[star].bind("<Button-1>", lambda e, s=star+1: [rating_var.set(str(s)), update_stars(clicked=True), save_feedback(row['_id'], s)])
            
            # update stars when rating changes
            rating_var.trace("w", lambda *args: update_stars(clicked=True))
            
            # popularity
            popularity_label = ctk.CTkLabel(track_frame, text=f"{row['Popularity']}", font=("Arial", 8))
            popularity_label.pack(pady=2)
    
    # refresh button
    refresh_button = ctk.CTkButton(app, text="Refresh", command=lambda: show_results(selected_mood))
    refresh_button.pack(pady=5)
    
    # choose new mood link
    mood_link = ctk.CTkLabel(app, text="...or choose new mood", font=("Arial", 10), text_color="blue")
    mood_link.pack(pady=5)
    mood_link.bind("<Button-1>", lambda e: show_mood_selection())

# initialize GUI
app = ctk.CTk()
app.title("MMMood")
app.geometry("400x520")

# load and prepare data
df = load_data()
X, y, emotion_encoder, df = prepare_data(df)
model = train_model(X, y)

# show mood selection screen
show_mood_selection()

# start the app
app.mainloop()
