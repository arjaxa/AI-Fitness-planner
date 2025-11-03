import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="AI Fitness Planner", page_icon="💪")

st.title("AI Fitness Planner")
st.write("Plan personalized workouts based on your goals and preferences.")

# --------------------------
# 1️⃣ EXERCISE DATABASE
# --------------------------
exercises = {
    "chest": ["Bench Press", "Incline Dumbbell Press", "Push-ups", "Cable Fly", "Chest Dips"],
    "back": ["Pull-ups", "Deadlift", "Barbell Row", "Lat Pulldown", "Seated Cable Row"],
    "legs": ["Squats", "Lunges", "Leg Press", "Romanian Deadlift", "Leg Extension"],
    "shoulders": ["Overhead Press", "Lateral Raises", "Front Raises", "Reverse Fly", "Arnold Press"],
    "arms": ["Bicep Curls", "Tricep Pushdown", "Hammer Curls", "Skull Crushers", "Concentration Curl"],
    "core": ["Plank", "Crunches", "Leg Raises", "Bicycle Crunch", "Russian Twists"],
     "biceps": ["Barbell Curl", "Dumbbell Curl", "Preacher Curl"],
    "triceps": ["Tricep Dips", "Overhead Tricep Extension", "Close Grip Bench Press"]
}

# --------------------------
# CUSTOM SPLIT BLUEPRINT
# --------------------------

custom_splits = {
    "4 Day Upper Lower (2Upper/2Lower Custom)": {
        "Day 1 - Upper (Push)": [
            {"muscle": "chest", "type": "compound", "exercise": ["Barbell Bench Press", "Incline Dumbbell Press"]},
            {"muscle": "shoulders", "type": "compound", "exercise": ["Overhead Press"]},
            {"muscle": "chest", "type": "isolation", "exercise": ["Cable Fly"]},
            {"muscle": "triceps", "type": "isolation", "exercise": ["Tricep Pushdown"]},
            {"muscle": "core", "type": "stability", "exercise": ["Plank", "Hanging Leg Raises"]}
        ],
        "Day 2 - Lower (Quad, glute, abductor, calve)": [
            {"muscle": "Quads", "type": "isolation", "exercise": ["Leg extension", "Leg extension"]},
            {"muscle": "Quads", "type": "compound", "exercise": ["Smith squats", "BB Squats"]},
            {"muscle": "Quads", "type": "compound", "exercise": ["Hack squats"]},
            {"muscle": "Glute/abductor", "type": "i/c", "exercise": ["Cable leg abductions"]},
            {"muscle": "Quads", "type": "isolation/L", "exercise": ["DB Goblet squats"]},
            {"muscle": "Quads", "type": "compound/L", "exercise": ["DB Lunge"]},
            {"muscle": "Calves", "type": "i/c", "exercise": ["Seated DB Calves"]},
            {"muscle": "Calves", "type": "i/c", "exercise": ["Standing calves machine"]}
        ],
        "Day 3 - Upper (Pull)": [
            {"muscle": "back", "type": "compound", "exercise": ["Deadlift", "Barbell Row"]},
            {"muscle": "biceps", "type": "isolation", "exercise": ["Barbell Curl", "Hammer Curl"]},
            {"muscle": "shoulders", "type": "isolation", "exercise": ["Rear Delt Fly"]}
        ],
        "Day 4 - Lower": [
            {"muscle": "legs", "type": "compound", "exercise": ["Front Squat", "Lunges"]},
            {"muscle": "legs", "type": "isolation", "exercise": ["Calf Raises", "Glute Kickbacks"]},
            {"muscle": "core", "type": "core", "exercise": ["Ab Wheel Rollout"]}
        ]
    }
      # more variations...
}

# --------------------------
# 2️⃣ SPLIT STRUCTURES
# --------------------------
splits = {
    "Full Body": [["chest", "back", "legs", "shoulders", "arms", "core"]],
    "Upper / Lower": [["chest", "back", "shoulders", "arms"], ["legs", "core"]],
    "Push / Pull / Legs": [["chest", "shoulders", "triceps"], ["back", "biceps"], ["legs", "core"]],
}

# --------------------------
# 3️⃣ USER INPUT
# --------------------------
st.header("🏋️ Plan Your Routine")

days = st.selectbox("How many days per week do you want to work out?", [3, 4, 5, 6])
split_choice = st.selectbox("Choose your workout split:", list(splits.keys()))

if st.button("Generate Plan"):
    chosen_split = splits[split_choice]
    plan = {}

    # Cycle through the split for the number of workout days
    for i in range(days):
        muscles = chosen_split[i % len(chosen_split)]
        day_plan = []
        for m in muscles:
            day_plan.append(f"{m.capitalize()}: {random.choice(exercises.get(m, []))}")
        plan[f"Day {i+1}"] = day_plan

    st.success(f"✅ Generated {days}-Day {split_choice} Plan")
    for day, workouts in plan.items():
        st.subheader(day)
        for w in workouts:
            st.write(f"- {w}")