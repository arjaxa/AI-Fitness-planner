import streamlit as st
import random
import pandas as pd

from splits import custom_splits

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO
from exercise_library import get_exercise
from validation import validate_template

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

# Generate plan   
import random

validate_template(selected_template)
from ai_engine import should_superset


def generate_plan(selected_split, goal, experience_key):

    plan = {}

    for day, exercises in selected_split.items():
        day_plan = []

        for muscle, ex_type, equipment in exercises:
            exercise = get_exercise(muscle, ex_type, equipment)

            # sets
            if experience_key == "beginner":
                sets = random.choice([2, 3])
            elif experience_key == "intermediate":
                sets = random.choice([3, 4])
            else:
                sets = random.choice([4, 5])        

            # reps
            if goal == "strength":
                reps = "4-6 reps"
            elif goal == "fat_loss":
                reps = "12-16 reps"
            else:
                reps = "8-12 reps"

            final_exercise = {
                "name": exercise["name"],
                "primary": exercise["primary"],
                "secondary": exercise["secondary"],
                "type": exercise["type"],
                "equipment": exercise["equipment"],
                "sets": sets,
                "reps": reps
            }

            day_plan.append(final_exercise)

        # grouping
        grouped_plan = []
        i = 0

        while i < len(day_plan):

            # last exercise must be single
            if i == len(day_plan) - 1:
                grouped_plan.append({
                    "mode": "single",
                    "exercises": [day_plan[i]]
                })
                break

            ex1 = day_plan[i]
            ex2 = day_plan[i + 1]

            if should_superset(ex1, ex2):

                grouped_plan.append({
                    "mode": "superset",
                    "exercises": [ex1, ex2]
                })

                i += 2  # skip next because it was paired

            else:

                grouped_plan.append({
                    "mode": "single",
                    "exercises": [ex1]
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
                   <span style='float:right'>{ex['sets']} x {ex['reps']}</span>

                   **+ {ex2['name']}**
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
        
               
    