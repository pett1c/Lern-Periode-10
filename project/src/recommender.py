import random
from db import get_tracks

def get_recommendations(emotion, num_recommendations=4):
    yes_tracks = get_tracks(emotion, "yes")
    neutral_tracks = get_tracks(emotion, None)
    no_tracks = get_tracks(emotion, "no")

    recommendations = []
    remaining = num_recommendations

    if yes_tracks:
        num_yes = min(len(yes_tracks), remaining)
        recommendations.extend(random.sample(yes_tracks, num_yes))
        remaining -= num_yes

    # if we need more, adding neutral tracks too
    if remaining > 0 and neutral_tracks:
        num_neutral = min(len(neutral_tracks), remaining)
        recommendations.extend(random.sample(neutral_tracks, num_neutral))
        remaining -= num_neutral

    # if we need more, adding tracks with "no" (1 of 10 chance)
    if remaining > 0 and no_tracks and random.random() < 0.1:
        num_no = min(len(no_tracks), remaining)
        recommendations.extend(random.sample(no_tracks, num_no))

    if remaining > 0 and neutral_tracks:
        recommendations.extend(random.sample(neutral_tracks, remaining))

    return recommendations[:num_recommendations]