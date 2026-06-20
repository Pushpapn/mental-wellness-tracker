import random

strategies = [
    "Take 5 deep breaths.",
    "Try a 2-minute gratitude reflection.",
    "Stretch your body for 3 minutes.",
    "Listen to calming music."
]

def get_strategy():
    return random.choice(strategies)

