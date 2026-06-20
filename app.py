import streamlit as st
from components.journaling import journaling_ui
from components.mood_tracker import mood_ui
from components.exercises import exercises_ui
from services.ai_analysis import analyze_entry
from services.coping_strategies import get_strategy
from services.storage import save_entry, load_entries

st.set_page_config(page_title="Mental Wellness Tracker", layout="centered")

st.title("🧠 Mental Wellness Tracker")
st.sidebar.success("Navigate through sections")

menu = st.sidebar.radio("Choose a section:", ["Journal", "Mood Tracker", "Exercises"])

if menu == "Journal":
    entry = journaling_ui()
    if entry:
        save_entry(entry)
        analysis = analyze_entry(entry)
        st.write("### AI Insights")
        st.write(analysis)
        st.success("Entry saved successfully!")

elif menu == "Mood Tracker":
    mood = mood_ui()
    if mood:
        save_entry({"mood": mood})
        st.success(f"Mood '{mood}' logged successfully!")

elif menu == "Exercises":
    strategy = get_strategy()
    exercises_ui(strategy)
