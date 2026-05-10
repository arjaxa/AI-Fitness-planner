# AI Fitness Planner

A smart workout generator that builds structured, goal-oriented training plans in seconds.

ArisPlan creates personalized gym routines based on user goals and experience level and then exports the plan as a PDF.

---

## What It Does

* Generates complete multi-day workout splits based on experience level
* Selects exercises from a structured library using muscle group, equipment, and movement patterns
* Automatically builds supersets using a compatibility checking system
* Prevents duplicate exercises within the same training day
* Chooses sets and reps according to the user’s goal
* Exports workout plans as downloadable PDFs
* Runs entirely in a Streamlit interface

---

## Live App

https://arisplan.streamlit.app/

---


## Screenshots

<img width="1847" height="807" alt="Screenshot 2026-05-10 183808" src="https://github.com/user-attachments/assets/1f4f88d2-6dc5-4e48-93a3-26d49571aa10" />

<img width="1848" height="839" alt="Screenshot 2026-05-10 183912" src="https://github.com/user-attachments/assets/89afcbb3-238f-43c0-a1c0-2747d3c461de" />

<img width="1848" height="829" alt="Screenshot 2026-05-10 183939" src="https://github.com/user-attachments/assets/0311f74b-2df0-481b-826e-60622ed44aa6" />




## Tech Stack

* **Python** — core logic
* **Scikit-Learn** — exercise pairing
* **Streamlit** — user interface and deployment
* **ReportLab** — PDF generation

---


## Running Locally

```bash
git clone <https://github.com/arjaxa/AI-Fitness-planner-ArisPlan >
cd ai-fitness-planner
pip install -r requirements.txt
streamlit run app.py
```

---

## Future Improvements

* Machine learning–based exercise pairing
* Trisets
* Smarter fatigue tracking across the week
* User profiles and saved plans
* Expanded exercise library






