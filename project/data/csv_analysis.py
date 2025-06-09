import pymongo
import pandas as pd

# connect to mongodb
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["music_db"]
collection = db["songs"]

# load csv into mongodb
def load_data(csv_file_path):
	# read csv file
	df = pd.read_csv(csv_file_path)
	# convert dataframe to dictionary
	data = df.to_dict('records')
	# clear old data & insert new data
	collection.drop()
	collection.insert_many(data)
	print(f"Loaded {len(data)} songs into MongoDB.")

# data analysis
def analyze_data():
	# load data into panndas
	df = pd.DataFrame(list(collection.find()))

	# count songs by genre
	genre_pipeline = [
		{
			"$group": {
				"_id": "$Genre",
				"count": {"$sum": 1}
			}
		},
		{
			"$sort": {
				"count": -1
			}
		}
	]
	genre_counts = list(collection.aggregate(genre_pipeline))

	# count songs by emotion
	emotion_pipeline = [
		{
			"$group": {
				"_id": "$emotion",
				"count": {"$sum": 1}
			}
		},
		{
			"$sort": {
				"count": -1
			}
		}
	]
	emotion_counts = list(collection.aggregate(emotion_pipeline))

	# average attributes by genre (tempo, energy, popularity)
	attribute_pipeline = [
		{
			"$group": {
				"_id": "$Genre",
				"avg_tempo": {"$avg": "$Tempo"},
				"avg_energy": {"$avg": "$Energy"},
				"avg_popularity": {"$avg": "$Popularity"}
			}
		},
		{
			"$sort": {
				"_id": 1
			}
		}
	]
	
	attribute_stats = list(collection.aggregate(attribute_pipeline))

	# correlation between Tempo and Energy
	tempo_energy_corr = df[["Tempo", "Energy"]].corr().iloc[0,1]

	# print results
	print("\n--= data analysis results =--")

	print("\nsongs by genre:")
	for genre in genre_counts:
		print(f"Genre: {genre['_id']}, Count: {genre['count']}")
	print("\nsongs by emotion:")
	for emotion in emotion_counts:
		print(f"Emotion: {emotion['_id']}, Count: {emotion['count']}")
	print("\naverage attributes by genre:")
	for stat in attribute_stats:
		print(f"Genre: {stat['_id']}, Avg Tempo: {stat['avg_tempo']:.2f}, Avg Energy: {stat['avg_energy']:.2f}, Avg Popularity: {stat['avg_popularity']:.2f}")
	print("\ncorrelation between Tempo and Energy:")
	print(f"correlation coefficient: {tempo_energy_corr:.2f}")

	# patterns
	print("\n--= patterns =--")
	print("- emotions helps match songs to user mood")
	print(f"- Tempo and Energy correlation ({tempo_energy_corr:.2f} suggests faster songs tend to be more energetic")

# main
if __name__ == "__main__":
	csv_file_path = "dirty_db.csv"
	load_data(csv_file_path)
	analyze_data()