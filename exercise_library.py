EXERCISE_LIBRARY = [
    # QUADS
    {
        "name": "Leg Extension",
        "primary": "quads",
        "secondary": [], 
        "type": "isolation",
        "equipment": "machine",
        "fatigue": 1,
        "pattern": "extension" # add for all
    },
     {
        "name": "Back Squat",
        "primary": "quads",
        "secondary": ["glute", "hamstring"],
        "type": "compound",
        "equipment": "barbell",
        "fatigue": 3,
        "pattern": "squat"

    },
     {
        "name": "Goblet Squat",
        "primary": "quads",
        "secondary": ["glute"],
        "type": "compound",
        "equipment": "dumbbell",
        "fatigue": 2,
        "pattern": "squat"
    },
    {
        "name": "Leg Press",
        "primary": "quads",
        "secondary": ["hamstring"],
        "type": "compound",
        "equipment": "machine",
        "fatigue": 3,
        "pattern": "press"
    },
     {
        "name": "DB Lunge",
        "primary": "quads",
        "secondary": ["glute", "hamstring"],
        "type": "compound",
        "equipment": "dumbbell",
        "fatigue": 2,
        "pattern": "lunge"
    },
     {
        "name": "Cable Goblet Squat",
        "primary": "quads",
        "secondary": ["glute"],
        "type": "compound",
        "equipment": "cable",
        "fatigue": 2,
        "pattern": "squat"
    },
    # HAMSTRING
    {
        "name": "Lying hamstring curls",
        "primary": "hamstring",
        "secondary": [],
        "type": "isolation",
        "equipment": "machine",
        "fatigue": 1,
        "pattern": "curl"
    },
     {
        "name": "BB RDL",
        "primary": "hamstring",
        "secondary": ["glute", "lowerback"],
        "type": "compound",
        "equipment": "barbell",
        "fatigue": 3,
        "pattern": "hinge"
    },
     {
        "name": "DB RDL",
        "primary": "hamstring",
        "secondary": ["glute"],
        "type": "compound",
        "equipment": "dumbbell",
        "fatigue": 2,
        "pattern": "hinge"
    },
    {
        "name": "Seated hamstring curl machine",
        "primary": "hamstring",
        "secondary": [],
        "type": "isolation",
        "equipment": "machine",
        "fatigue": 1,
        "pattern": "curl"
    },
    # CALVES
     {
        "name": "Standing calf machine",
        "primary": "calf",
        "secondary": [],
        "type": "isolation",
        "equipment": "machine",
        "fatigue": 1,
        "pattern": "calf"
    },
     {
        "name": "Seated calf machine",
        "primary": "calf",
        "secondary": [],
        "type": "isolation",
        "equipment": "machine",
        "fatigue": 1,
        "pattern": "calf"
    },
    # CHEST
     {
        "name": "BB Bench Press",
        "primary": "chest",
        "secondary": ["shoulder", "triceps"],
        "type": "compound",
        "equipment": "barbell",
        "fatigue": 3,
        "pattern": "press"
    },
     {
        "name": "DB Bench Press",
        "primary": "chest",
        "secondary": ["shoulder", "triceps"],
        "type": "compound",
        "equipment": "dumbbell",
        "fatigue": 3,
        "pattern": "press"
    },
    {
        "name": "Cable fly",
        "primary": "chest",
        "secondary": ["shoulder"],
        "type": "isolation",
        "equipment": "cable",
        "fatigue": 2,
        "pattern": "fly"
    },
     {
        "name": "DB Fly",
        "primary": "chest",
        "secondary": ["shoulder"],
        "type": "isolation",
        "equipment": "dumbbell",
        "fatigue": 1,
        "pattern": "fly"
    },
    # SHOULDER
     {
        "name": "BB Shoulder Press",
        "secondary": ["triceps"],
        "primary": "shoulder",
        "type": "compound",
        "equipment": "barbell",
        "fatigue": 2,
        "pattern": "press"
    },
     {
        "name": "DB Shoulder Press",
        "primary": "shoulder",
        "secondary": [],
        "type": "isolation",
        "equipment": "dumbbell",
        "fatigue": 2,
        "pattern": "press"
    },
    {
        "name": "Cable lateral raise",
        "secondary": [],
        "primary": "shoulder",
        "type": "isolation",
        "equipment": "cable",
        "fatigue": 2,
        "pattern": "lateral_raise"
    },
     {
        "name": "DB Fly back",
        "primary": "shoulder",
        "secondary": [],
        "type": "isolation",
        "equipment": "dumbbell",
        "fatigue": 1,
        "pattern": "fly_back"
    },
    # TRICEPS
      {
        "name": "BB Skull Crusher",
        "primary": "triceps",
        "secondary": ["chest"],
        "type": "compound",
        "equipment": "barbell",
        "fatigue": 2,
        "pattern": "press"
    },
     {
        "name": "DB Tricep Kickback",
        "primary": "triceps",
        "secondary": [],
        "type": "isolation",
        "equipment": "dumbbell",
        "fatigue": 1,
        "pattern": "kickback"
    },
    {
        "name": "Cable Rope Tricep Pushdown",
        "primary": "triceps",
        "secondary": [],
        "type": "isolation",
        "equipment": "cable",
        "fatigue": 1,
        "pattern": "pushdown"
    },
     {
        "name": "Tricep Dips",
        "primary": "triceps",
        "secondary": ["chest", "shoulder"],
        "type": "compound",
        "equipment": "bodyweight",
        "fatigue": 3,
        "pattern": "dip"
    },
    # BACK
    {
        "name": "Lat Pulldown",
        "primary": "back",
        "secondary": ["biceps"],
        "type": "compound",
        "equipment": "machine",
        "fatigue": 2,
        "pattern": "pulldown"
    },
    {
        "name": "Seated Cable Row",
        "primary": "back",
        "secondary": ["biceps"],
        "type": "compound",
        "equipment": "cable",
        "fatigue": 2,
        "pattern": "row"
    },
    {
        "name": "Pull-up",
        "primary": "back",
        "secondary": ["biceps"],
        "type": "compound",
        "equipment": "bodyweight",
        "fatigue": 3,
        "pattern": "pullup"
    }
]






import random


def get_exercise(muscle, ex_type=None, equipment=None):
    candidates = [
        ex for ex in EXERCISE_LIBRARY if ex["primary"] == muscle # changed "muscle" to "primary"
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