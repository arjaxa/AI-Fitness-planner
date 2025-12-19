import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="AI Fitness Planner", page_icon="aris.png")

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
        "Day 1 - Upper (Back, Triceps)": [
            ["lat pulldown | 12x4"],
            ["BB Rows | 12 + 10 + 10 + 8"],
            ["H Machine | 12x4", "Single arm cable rows | 12x4"],
            ["DB Rows | 12x4"],
            ["Straight arms | 12x3"],
            ["hyperextensions | 20x4"],
            ["Cable triceps pulldown | 12x3"],
            ["DB tricep kickbacks | 8x4"]
        ],
        "Day 2 - Lower (Quad, abductor, calve)": [
            ["Leg extensions 4x12"],
            ["Smith squats | 12 + 10 + 10 + 8"],
            ["Smith lunge | 12x4", "Sumo squats | 12x4"],
            ["Single leg leg press (12 + 20(both))x4", "Goblet squats | 16x4"],
            ["Leg abduction machine | 16x4"],
            ["Cable(Knee bent) kick backs | 12x4"],
            ["Standing calves machine | 20x3"],
            ["Seated calves | 30x3"]
        ],
        "Day 3 - Upper (Shoulder, Chest, Bicep)": [
            ["Smith shoulder press | 12x4", "Seated db shoulder press | 12x4"],
            ["Cable lateral raises | 12x4"],
            ["DB Lateral raises | 10x4"],
            ["DB Front raise | 12x4"],
            ["Reversed fly machine | 10x3"],
            ["Cable rear delt | 12x4"],
            ["DB Chest press | 10x3"],
            ["DB chest fly | 8x3"],
            ["BB Bicep curls | 8x3"],
            ["DB hammer curls 12x3"]
        ],
        "Day 4 - Lower (hamstring, glute)": [
            ["Hamstring curls | 12x4", "Cable kick backs(straight) | 12x4"],
            ["BB RDL | 12x4"],
            ["BB hip thrusts | 12x4", "Cable side kick | 15x3"],
            ["Bulgarian split squats | 8x3"],
            ["abduction machine | 15x4"],
            ["DB lifts | 12x3"],
            ["DB Step ups | 12x4"],
            ["Standing calves | 30x3"]
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


# SPLIT STRUCTURES

splits = {
    "Full Body": [["chest", "back", "legs", "shoulders", "arms", "core"]],
    "Upper / Lower": [["chest", "back", "shoulders", "arms"], ["legs", "core"]],
    "Push / Pull / Legs": [["chest", "shoulders", "triceps"], ["back", "biceps"], ["legs", "core"]],
}


# USER INPUT

st.header("🦾 Plan Your Routine")

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