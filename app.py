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

# moved to splits.py


# SPLIT STRUCTURES

splits = {
    "Full Body": [["chest", "back", "legs", "shoulders", "arms", "core"]],
    "Upper / Lower": [["chest", "back", "shoulders", "arms"], ["legs", "core"]],
    "Push / Pull / Legs": [["chest", "shoulders", "triceps"], ["back", "biceps"], ["legs", "core"]],
}


# USER INPUT

st.header("🦾 Plan Your Routine")

# Choose number of days
days_per_week = st.selectbox("How many days a week do you want to work out?", ["3", "4", "5", "6"])

# Show split variations only for that day count
available_variations = list(custom_splits[days_per_week].keys())
selected_split = st.selectbox("Choose your split variation:", available_variations)

selected_split_data = custom_splits[days_per_week][selected_split]

currunt_selection = (days_per_week, selected_split)
if st.session_state.last_selection != currunt_selection:
    st.session_state.generated_plan = None
    st.session_state.last_selection = currunt_selection

# Generate plan
import random

def generate_plan(selected_split):
    plan = {}

    for day, exercises in selected_split.items():
        day_plan = []

        for ex in exercises:
            if isinstance(ex, list):
                day_plan.append(random.choice(ex))
            else:
                day_plan.append(ex)

        plan[day] = day_plan

    return plan

# convert plan to text
#def plan_to_text(plan):
#    text = ""
#    for day, exercises in plan.items():
#        for i, ex in enumerate(exercises, 1):
#            text += f"{i}. {ex}\n"
#        text += "\n"
#    return text

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

#col1, col2 = st.columns(2)
#with col1:
#    regenerate = st.button("Regenerate", key="regenerate")
#with col2:
#    clear = st.button("Clear", key="clear")

#if regenerate:
#    st.session_state.generated_plan = generate_plan(custom_splits[days_per_week][selected_split])
#if clear:
#    st.session_state.generated_plan = None    
    
if st.button("Generate plan"):
    plan = generate_plan(selected_split_data)
    st.session_state.generated_plan = generate_plan(custom_splits[days_per_week][selected_split])
    st.session_state.pdf_ready = False
    st.session_state.pdf_file = None
    # display
    if st.session_state.generated_plan:
     if st.button("Generate PDF"):
        st.session_state.pdf_file = plan_to_pdf(
            st.session_state.generated_plan
        )
        st.session_state.pdf_ready = True

    if st.session_state.pdf_ready:
        st.download_button(
            "⬇Download PDF",
            st.session_state.pdf_file,
            file_name="workout_plan.pdf",
            mime="application/pdf"
        )
    for day, exercises in st.session_state.generated_plan.items():
        st.subheader(day)
        st.divider()
        for i, ex in enumerate(exercises, start=1):
            if "|" in ex:
                name, details = ex.split("|", 1)
                st.markdown(f"**{i}. {name.strip()}**\n_{details.strip()}_")
            else:
                st.markdown(f"**{i}. {ex}**")


# download converted text
#if st.session_state.generated_plan:
#    plan_text = plan_to_text(st.session_state.generated_plan)
#    st.download_button(label="Download Plan", data=plan_text, file_name="Workout_plan.txt", mime="text/plan")    

# download pdf
if st.session_state.generated_plan:
    if st.button("Download PDF"):
        st.session_state.pdf_file = plan_to_pdf(st.session_state.generated_plan)
    if st.session_state.pdf_file:
        st.download_button(label="Download PDF", data=st.session_state.pdf_file, file_name="Workout_plan.pdf", mime="application/pdf")    
               
        
   # for day, exercises in selected_split_data.items():
   #     st.subheader(day)
   #     st.divider()
   #     for i, ex in enumerate(exercises, start=1):
   #         if "|" in ex:
   #             name, details = ex.split("|", 1)
   #             st.markdown(f"**{i}. {name.strip()}**\n_{details.strip()}_")
   #         else:
   #             st.markdown(f"**{i}. {ex}**")
        
        #for i, ex in enumerate(exercises, start=1):
        #    st.write(f"{i}. {ex}")


#if st.button("Generate Plan"):
 #   selected_plan = custom_splits[days_per_week][selected_split]
  #  for day, exercises_list in selected_plan.items():
   #     st.subheader(day)
    #    for i, exercise_group in enumerate(exercises_list, start=1):
            # Pick one random workout from each exercise group
     #       if isinstance(exercise_group, list):
      #          chosen_ex = random.choice(exercise_group)
       #     else:
        #        chosen_ex = exercise_group
         #   st.write(f"{i}. {chosen_ex}")


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