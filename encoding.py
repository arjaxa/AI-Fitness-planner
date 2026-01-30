MUSCLE_MAP = {
    "chest": 0,
    "back": 1,
    "quads": 2,
    "hamstrings": 3,
    "shoulders": 4,
    "arms": 5,
}

def encode_exercise(ex):
    return [
        MUSCLE_MAP.get(ex["muscle"], -1),
        1 if ex["type"] == "compound" else 0
    ]
