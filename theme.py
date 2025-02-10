import streamlit as st

def toggle_theme():
    """Bascule entre le mode jour et nuit"""
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = False
    
    if st.button("🌙 / ☀️ Changer de mode"):
        st.session_state.dark_mode = not st.session_state.dark_mode

    dark_css = """
    <style>
    body, .stApp { background-color: #0e1117; color: white; }
    h1, h2, h3, h4, h5, h6, p, span, div { color: white !important; }
    </style>
"""

light_css = """
    <style>
    body, .stApp { background-color: white; color: black; }
    h1, h2, h3, h4, h5, h6, p, span, div { color: black !important; }
    </style>
"""


    st.markdown(dark_css if st.session_state.dark_mode else light_css, unsafe_allow_html=True)
