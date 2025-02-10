import streamlit as st

def toggle_theme():
    """Bascule entre le mode jour et nuit"""
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = False
    
    if st.button("🌙 / ☀️ Changer de mode"):
        st.session_state.dark_mode = not st.session_state.dark_mode

    dark_css = """
        <style>
        body { background-color: #0e1117; color: white; }
        .stApp { background-color: #0e1117; }
        </style>
    """

    light_css = """
        <style>
        body { background-color: white; color: black; }
        .stApp { background-color: white; }
        </style>
    """

    st.markdown(dark_css if st.session_state.dark_mode else light_css, unsafe_allow_html=True)
