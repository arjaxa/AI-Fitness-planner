EXERCISE_LIBRARY = [
    # QUADS
    {
        "name": "Leg Extension",
        "muscle": "quads",
        "type": "isolation",
        "equipment": "machine"
    },
     {
        "name": "Back Squat",
        "muscle": "quads",
        "type": "compound",
        "equipment": "barbell"
    },
     {
        "name": "Goblet Squat",
        "muscle": "quads",
        "type": "compound",
        "equipment": "dumbbell"
    },
    # CHEST
     {
        "name": "BB Bench Press",
        "muscle": "chest",
        "type": "compound",
        "equipment": "barbell"
    },
     {
        "name": "DB Bench Press",
        "muscle": "chest",
        "type": "compound",
        "equipment": "dumbbell"
    },
    {
        "name": "Cable fly",
        "muscle": "chest",
        "type": "isolation",
        "equipment": "cable"
    },
    {
        "name": "Lat Pulldown",
        "muscle": "back",
        "type": "compound",
        "equipment": "machine"
    },
    {
        "name": "Seated Cable Row",
        "muscle": "back",
        "type": "compound",
        "equipment": "cable"
    },
    {
        "name": "Pull-up",
        "muscle": "back",
        "type": "compound",
        "equipment": "bodyweight"
    }
]






import random

def get_exercise(muscle, ex_type=None, equipment=None):
    candidates = [
        ex for ex in EXERCISE_LIBRARY if ex["muscle"] == muscle
    ]

    if ex_type:
        candidates = [ex for ex in candidates if ex["type"] == ex_type]
        if equipment:
            candidates = [ex for ex in candidates if ex["equipment"] == equipment]
            if not candidates:
                raise ValueError(
                    f"No exercise found for {muscle}, {ex_type}, {equipment}"
                )  
            return random.choice(candidates)