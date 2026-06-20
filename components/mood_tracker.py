import streamlit as st

def mood_ui():
    st.header("😊 Mood Tracker")
    mood = st.selectbox("How are you feeling today?", ["Happy", "Stressed", "Anxious", "Motivated", "Neutral"])
    if st.button("Log Mood"):
        return mood
    return None
