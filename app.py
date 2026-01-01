import streamlit as st
import random
import pandas as pd

from splits import custom_splits

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO

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


# EXERCISE DATABASE

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

def generate_plan(selected_split, goal, experience_key):
    plan = {}

    for day, exercises in selected_split.items():
        day_plan = []

        for ex in exercises:
            chosen = random.choice(ex)
            if isinstance(ex, list):
                if experience_key == "beginner":
                    chosen += " | 2-3 sets"
                elif experience_key == "intermediate":
                    chosen += " | 3-4 sets"
                else:
                    chosen += " | 4-5 sets"
            
            if goal == "strenght":
                chosen += " | 4-6 reps"
            elif goal == "Fat Loss":
                chosen += " | 12-16 reps"
            else:
                chosen += " | 8-12 reps"                
            day_plan.append(chosen)                

        plan[day] = day_plan

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
        for i, ex in enumerate(exercises, 1):
            c.drawString(x + 10, y, f"{i}. {ex}")
            y -= 15

            if y < 40:
                c.showPage()
                c.setFont("Helvetica", 10)
                y = height - 40

        y -= 10

    c.save()
    buffer.seek(0)
    return buffer
 



# Generate plan
if st.button("Generate plan"):
    templates = custom_splits[days_per_week][goal][experience_key]
    selected_template = random.choice(templates)
    st.session_state.generated_plan = generate_plan(selected_template, goal, experience_key)
    st.session_state.show_download = False
    


# Display plan
if st.session_state.generated_plan:
    for day, exercises in st.session_state.generated_plan.items():
        st.subheader(day)
        for i, ex in enumerate(exercises, 1):
            if "|" in ex:
                name, details = ex.split("|", 1)
                st.markdown(f"**{i}. {name.strip()}**\n_{details.strip()}_")
            else:
                st.markdown(f"**{i}. {ex}**")
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
        
               
    