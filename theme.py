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
    .stSidebar, .stSidebarContent { background-color: #1a1d23 !important; color: white !important; }
    .st-emotion-cache-h4xjwg, .st-emotion-cache-15ecox0 { background-color: #0e1117 !important; color: white !important; }
    h1, h2, h3, h4, h5, h6, p, span, div { color: white !important; }
    .stTextInput, .stButton>button, .stSelectbox, .stRadio { background-color: #25282e !important; color: white !important; border-color: white !important; }
    </style>
    """

    light_css = """
    <style>
    body, .stApp { background-color: white; color: black; }
    .stSidebar, .stSidebarContent { background-color: #f0f0f0 !important; color: black !important; }
    .st-emotion-cache-h4xjwg, .st-emotion-cache-15ecox0 { background-color: white !important; color: black !important; }
    h1, h2, h3, h4, h5, h6, p, span, div { color: black !important; }
    .stTextInput, .stButton>button, .stSelectbox, .stRadio { background-color: white !important; color: black !important; border-color: black !important; }
    </style>
    """

    st.markdown(dark_css if st.session_state.dark_mode else light_css, unsafe_allow_html=True)
