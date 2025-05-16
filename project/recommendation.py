import pandas as pd
import pymongo
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# connect to mongodb
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
    # convert emotions & genres to numbers
    emotion_encoder = LabelEncoder()
    genre_encoder = LabelEncoder()
    df['emotion_num'] = emotion_encoder.fit_transform(df['emotion'])
    df['genre_num'] = genre_encoder.fit_transform(df['Genre'])
    
    # features and target
    X = df[['Tempo', 'Energy', 'Popularity', 'genre_num']]
    y = df['emotion_num']
    
    return X, y, emotion_encoder, df

# train the model
def train_model(X, y):
    # split data into train and test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    # create and train model
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)
    
    # check accuracy
    accuracy = model.score(X_test, y_test)
    print(f"Model accuracy: {accuracy:.2f}")
    
    return model

# recommend songs
def recommend_songs(mood, model, emotion_encoder, df):
    try:
        # convert mood to number
        mood_num = emotion_encoder.transform([mood])[0]
        
        # get features
        X = df[['Tempo', 'Energy', 'Popularity', 'genre_num']]
        
        # predict probabilities
        probs = model.predict_proba(X)
        mood_probs = probs[:, mood_num]
        
        # add probabilities to dataframe
        df['mood_prob'] = mood_probs
        
        # sort by probability and popularity
        recommendations = df.sort_values(by=['mood_prob', 'Popularity'], ascending=False)
        
        # get top 10 songs
        top_songs = recommendations[['title', 'artist', 'Genre', 'emotion', 'Popularity', 'Tempo', 'Energy']].head(10)
        
        return top_songs
    except:
        print(f"Sorry, mood '{mood}' not found!")
        return None

# main
if __name__ == "__main__":
    # load data
    df = load_data()
    
    # prepare data
    X, y, emotion_encoder, df = prepare_data(df)
    
    # train model
    model = train_model(X, y)
    
    # recommend songs for 'joy'
    mood = "joy"
    recommendations = recommend_songs(mood, model, emotion_encoder, df)
    
    if recommendations is not None:
        print(f"\nTop 10 Songs for Mood: {mood}")
        print(recommendations)