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
    {
        "name": "Leg Press",
        "muscle": "quads",
        "type": "compound",
        "equipment": "machine"
    },
     {
        "name": "DB Lunge",
        "muscle": "quads",
        "type": "compound",
        "equipment": "dumbbell"
    },
     {
        "name": "",
        "muscle": "quads",
        "type": "compound",
        "equipment": "dumbbell"
    },
    # HAMSTRING
    {
        "name": "Lying hamstring curls",
        "muscle": "hamstring",
        "type": "isolation",
        "equipment": "machine"
    },
     {
        "name": "BB RDL",
        "muscle": "hamstring",
        "type": "compound",
        "equipment": "barbell"
    },
     {
        "name": "DB RDL",
        "muscle": "hamstring",
        "type": "compound",
        "equipment": "dumbbell"
    },
    {
        "name": "Seated hamstring curl machine",
        "muscle": "hamstring",
        "type": "isolation",
        "equipment": "machine"
    },
    # CALVES
     {
        "name": "Standing calf machine",
        "muscle": "calf",
        "type": "isolation",
        "equipment": "machine"
    },
     {
        "name": "Seated calf machine",
        "muscle": "calf",
        "type": "isolation",
        "equipment": "machine"
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
        "name": "DB Fly",
        "muscle": "chest",
        "type": "isolation",
        "equipment": "dumbbell"
    },
    # SHOULDER
     {
        "name": "BB Shoulder Press",
        "muscle": "shoulder",
        "type": "compound",
        "equipment": "barbell"
    },
     {
        "name": "DB Shoulder Press",
        "muscle": "shoulder",
        "type": "isolation",
        "equipment": "dumbbell"
    },
    {
        "name": "Cable lateral raise",
        "muscle": "shoulder",
        "type": "isolation",
        "equipment": "cable"
    },
     {
        "name": "DB Fly back",
        "muscle": "shoulder",
        "type": "isolation",
        "equipment": "dumbbell"
    },
    # TRICEPS
      {
        "name": "BB Skull Crusher",
        "muscle": "triceps",
        "type": "compound",
        "equipment": "barbell"
    },
     {
        "name": "DB Tricep Kickback",
        "muscle": "triceps",
        "type": "isolation",
        "equipment": "dumbbell"
    },
    {
        "name": "Cable Rope Tricep Pushdown",
        "muscle": "triceps",
        "type": "isolation",
        "equipment": "cable"
    },
     {
        "name": "Tricep Dips",
        "muscle": "triceps",
        "type": "compound",
        "equipment": "bodyweight"
    },
    # BACK
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