import streamlit as st

def exercises_ui(strategy):
    st.header("🧘 Mindfulness Exercises")
    st.write(strategy)
    if st.button("Start Exercise"):
        st.success("Exercise started! Follow the instructions above.")
