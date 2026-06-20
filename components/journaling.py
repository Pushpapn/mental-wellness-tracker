import streamlit as st

def journaling_ui():
    st.header("📓 Daily Journal")
    entry = st.text_area("Write your thoughts here:")
    if st.button("Save Journal"):
        return entry
    return None
