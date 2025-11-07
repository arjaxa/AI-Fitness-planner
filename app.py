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
    "3": {
        "3 Day Push/Pull/Leg split": {
            "Day1": [...],
            "Day2": [...],
            "Day3": [...]
        }
    },

    "4": {"4 Day Upper Lower (pull/leg(q)/push/leg(h) Custom1)": {
        "Day 1 - Upper (Push)": [
            ["bench press", "db press"],
            ["bb rows", "db rows"]
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
        ]},
    },

    "5": {
        "5 Day Split (custom1)": {
            "Day1": [...],
            "Day2": [...],
            "Day3": [...],
            "Day4": [...],
            "Day5": [...]
        }
    },

    "6": {
        "6 Days Split (custom1)": {
            "Day1": [...],
            "Day2": [...],
            "Day3": [...],
            "Day4": [...],
            "Day5": [...],
            "Day6": [...]
        }
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

# Step 1: Choose number of days
days_per_week = st.selectbox("How many days a week do you want to work out?", ["3", "4", "5", "6"])

# Step 2: Show split variations only for that day count
available_variations = list(custom_splits[days_per_week].keys())
selected_split = st.selectbox("Choose your split variation:", available_variations)


# Step 3: Generate plan
import random

if st.button("Generate Plan"):
    selected_plan = custom_splits[days_per_week][selected_split]
    for day, exercises_list in selected_plan.items():
        st.subheader(day)
        for i, exercise_group in enumerate(exercises_list, start=1):
            # Pick one random workout from each exercise group
            if isinstance(exercise_group, list):
                chosen_ex = random.choice(exercise_group)
            else:
                chosen_ex = exercise_group
            st.write(f"{i}. {chosen_ex}")
#    selected_plan = custom_splits[days_per_week][selected_split]
#   for day, exercises_list in selected_plan.items():
#        st.subheader(day)
#        for i, ex in enumerate(exercises_list, start=1):
#            st.write(f"{i}. {ex}")

#split_names = list(custom_splits.keys())
#selected_split = st.selectbox("Select a split variation:", split_names)

#if st.button("Generate Custom Plan"):
#    selected_plan = custom_splits[selected_split]
#    for day, exercises_list in selected_plan.items():
#        st.subheader(day)
#        for i, ex in enumerate(exercises_list, start=1):
#            st.write(f"{i}. {ex}")


#days = st.selectbox("How many days per week do you want to work out?", [3, 4, 5, 6])
#split_choice = st.selectbox("Choose your workout split:", list(splits.keys()))

#if st.button("Generate Plan"):
#    chosen_split = splits[split_choice]
#    plan = {}

    # Cycle through the split for the number of workout days
#    for i in range(days):
#        muscles = chosen_split[i % len(chosen_split)]
#        day_plan = []
#        for m in muscles:
#            day_plan.append(f"{m.capitalize()}: {random.choice(exercises.get(m, []))}")
#        plan[f"Day {i+1}"] = day_plan

#    st.success(f"✅ Generated {days}-Day {split_choice} Plan")
#    for day, workouts in plan.items():
#        st.subheader(day)
#        for w in workouts:
#            st.write(f"- {w}")