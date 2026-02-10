import streamlit as st
import random
import pandas as pd

from splits import custom_splits

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO
from exercise_library import get_exercise
from validation import validate_template

from ml_engine import ml_should_superset as should_superset


if "generated_plan" not in st.session_state:
    st.session_state.generated_plan = None
if "last_selection" not in st.session_state:
    st.session_state.last_selection = None
if "pdf_file" not in st.session_state:
    st.session_state.pdf_file = None 
if "show_download" not in st.session_state:
    st.session_state.show_download = False       

st.set_page_config(page_title="AI Fitness Planner", page_icon="aris.png")

st.title("AI Fitness Planner")
st.write("Plan personalized workouts based on your goals and preferences.")



# moved to splits.py


# SPLIT STRUCTURES

splits = {
    "Full Body": [["chest", "back", "legs", "shoulders", "arms", "core"]],
    "Upper / Lower": [["chest", "back", "shoulders", "arms"], ["legs", "core"]],
    "Push / Pull / Legs": [["chest", "shoulders", "triceps"], ["back", "biceps"], ["legs", "core"]],
}


# USER INPUT

st.header("🦾 Plan Your Routine")

# user goal
goal = st.selectbox(
    "What's your main goal?", ["Hyperthrophy (Muscle Gain)", "Strength", "Fat Loss"]
)

goal_map = {
    "Hyperthrophy (Muscle Gain)": "hypertrophy",
    "Fat Loss": "fat_loss",
    "Strength": "strength"
}


goal = goal_map[goal]

# experience level
experience = st.selectbox(
    "Select experience level:", ["Beginner", "Intermediate", "Advanced"]
)

experience_map = {
    "Beginner": "beginner",
    "Intermediate": "intermediate",
    "Advanced": "advanced"
}

experience_key = experience_map[experience]

# Choose number of days
days_per_week = st.selectbox("How many days a week do you want to work out?", ["3", "4", "5", "6"]) # add 4,5,6 later

templates = custom_splits[days_per_week][goal][experience_key]
selected_template = random.choice(templates)



currunt_selection = (days_per_week, selected_template)
if st.session_state.last_selection != currunt_selection:
    st.session_state.generated_plan = None
    st.session_state.last_selection = currunt_selection

# sets function
def get_random_sets(experience_key):
    if experience_key == "beginner":
        return random.choice([2, 3])
    elif experience_key == "intermediate":
        return random.choice([3, 4])
    else: # advanced
        return random.choice([4, 5])

# reps function
def get_random_reps(goal):
    if goal == "strength":
        return random.choice([4, 5, 6])
    elif goal == "fat_loss":
        return random.choice([12, 15, 16])
    else: # hyperthrophy
        return random.choice([8, 10, 12])


# Generate plan   
import random

validate_template(selected_template)
from ai_engine import should_superset


def generate_plan(selected_split, goal, experience_key):

    plan = {}

    for day, exercises in selected_split.items():
        day_plan = []
        used_patterns = set()

        for muscle, ex_type, equipment in exercises:
            for _ in range(10):
                exercise = get_exercise(muscle, ex_type, equipment)
                if exercise["pattern"] not in used_patterns:
                    used_patterns.add(exercise["pattern"])
                    break


            final_exercise = {
                "name": exercise["name"],
                "primary": exercise["primary"],
                "secondary": exercise["secondary"],
                "type": exercise["type"],
                "equipment": exercise["equipment"]
            }

            day_plan.append(final_exercise)

        # grouping
        grouped_plan = []
        i = 0

        while i < len(day_plan):

            # last exercise must be single
            if i == len(day_plan) - 1:

                ex = day_plan[i]

                ex["sets"] = get_random_sets(experience_key)
                ex["reps"] = get_random_reps(goal)

                grouped_plan.append({
                    "mode": "single",
                    "exercises": [ex]
                })
                break

            ex1 = day_plan[i]
            ex2 = day_plan[i + 1]

            if should_superset(ex1, ex2):

                shared_sets = get_random_sets(experience_key)

                ex1["sets"] = shared_sets
                ex2["sets"] = shared_sets

                ex1["reps"] = get_random_reps(goal)
                ex2["reps"] = get_random_reps(goal)

                grouped_plan.append({
                    "mode": "superset",
                    "exercises": [ex1, ex2]
                })

                i += 2  # skip next because it was paired

            else:

                ex = day_plan[i]

                ex["sets"] = get_random_sets(experience_key)
                ex["reps"] = get_random_reps(goal)

                grouped_plan.append({
                    "mode": "single",
                    "exercises": [ex]
                })

                i += 1

        plan[day] = grouped_plan

    return plan




# plan to pdf
def plan_to_pdf(plan):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    x = 40
    y = height - 40

    for day, exercises in plan.items():
        c.setFont("Helvetica-Bold", 12)
        c.drawString(x, y, day)
        y -= 20

        c.setFont("Helvetica", 10)
    for group in exercises:

     if group["mode"] == "superset":
        c.drawString(x + 10, y, "Superset:")
        y -= 15

        for ex in group["exercises"]:
            c.drawString(
                x + 20,
                y,
                f"- {ex['name']} ({ex['sets']} | {ex['reps']})"
            )
            y -= 15

    else:
        ex = group["exercises"][0]

        c.drawString(
            x + 10,
            y,
            f"- {ex['name']} ({ex['sets']} | {ex['reps']})"
        )
        y -= 15


        if y < 40:
                c.showPage()
                c.setFont("Helvetica", 10)
                y = height - 40

        y -= 10

    c.save()
    buffer.seek(0)
    return buffer
 



# Generate plan BTN
if st.button("Generate plan"):
    templates = custom_splits[days_per_week][goal][experience_key]
    selected_template = random.choice(templates)
    st.session_state.generated_plan = generate_plan(selected_template, goal, experience_key)
    st.session_state.show_download = False
    


# Display plan
if st.session_state.generated_plan:
    for day, exercises in st.session_state.generated_plan.items():
        st.subheader(day)
        workout_number = 1

        for group in exercises:

            if group["mode"] == "single":
                ex = group["exercises"][0]
                # single workout
                st.markdown(
                    f"""
                    <strong>{workout_number}. {ex['name']}</strong>
                    <span style='float:right'>{ex['sets']} x {ex['reps']}</span>
                    """,
                    unsafe_allow_html=True
                )

            elif group["mode"] == "superset":

                ex1, ex2 = group["exercises"]

                # superset workout

                st.markdown(
                    f"""
                   <strong>{workout_number}. {ex['name']}</strong>
                   <span style='float:right'>{ex1['sets']} x {ex1['reps']}</span><br>

                   <strong>+ {ex2['name']}</strong>
                   <span style='float:right'>{ex2['sets']} x {ex2['reps']}</span>
                   """,
                    unsafe_allow_html=True
                )

            workout_number += 1

        st.divider()

    
        
        


            




# export pdf

    if st.session_state.generated_plan:
        if st.button("Prepare PDF"):
            st.session_state.pdf_ready = True
    if st.session_state.get("pdf_ready", False):
        if st.download_button(label="Download PDF",
            data=plan_to_pdf(st.session_state.generated_plan),
            file_name="WorkoutPlan.pdf",
            mime="application/pdf"):
            st.session_state.pdf_ready = False
        
               
    