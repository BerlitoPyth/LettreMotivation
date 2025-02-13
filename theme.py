import streamlit as st
def toggle_theme():
    """
    Bascule entre le mode jour et nuit dans une application Streamlit.
    Gère les styles CSS pour une expérience utilisateur cohérente.
    Mode sombre activé par défaut.
    """
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = True
    
    # Configuration des thèmes
    THEMES = {
        "dark": {
            "bg_color": "#0e1117",
            "text_color": "white",
            "sidebar_bg": "#1a1d23",
            "input_bg": "#25282e",
            "border_color": "white"
        },
        "light": {
            "bg_color": "white",
            "text_color": "black",
            "sidebar_bg": "#f0f0f0",
            "input_bg": "white",
            "border_color": "black"
        }
    }
    
    # Bouton de thème avec clé unique
    if st.button("☀️" if st.session_state.dark_mode else "🌙", 
                key=f"theme_toggle_btn_{id(st.session_state)}"):
        st.session_state.dark_mode = not st.session_state.dark_mode
        st.rerun()
    
    current_theme = THEMES["dark"] if st.session_state.dark_mode else THEMES["light"]
    
    # CSS dynamique optimisé
    css = f"""
    <style>
    /* Styles globaux */
    body, .stApp {{
        background-color: {current_theme["bg_color"]};
        color: {current_theme["text_color"]};
    }}
    
    /* Sidebar et navigation */
    .stSidebar, .stSidebarContent {{
        background-color: {current_theme["sidebar_bg"]} !important;
        color: {current_theme["text_color"]} !important;
        padding-top: 0 !important;
    }}
    
    /* Menu radio */
    .stRadio {{
        background: none !important;
        margin-top: -1rem !important;
    }}
    
    .stRadio > div[role="radiogroup"] {{
        display: flex !important;
        flex-direction: column !important;
        gap: 4px !important;
        padding: 0 !important;
        margin-bottom: 1rem !important;
    }}
    
    /* Style des boutons radio */
    .stRadio > div[role="radiogroup"] > label {{
        background-color: {current_theme["sidebar_bg"]} !important;
        color: {current_theme["text_color"]} !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 4px !important;
        margin: 0 !important;
        padding: 12px !important;
        height: 45px !important;
        display: flex !important;
        align-items: center !important;
        width: 100% !important;
        cursor: pointer !important;
        transition: all 0.2s ease !important;
    }}
    
    .stRadio > div[role="radiogroup"] > label:hover {{
        border-color: rgba(96, 165, 250, 0.4) !important;
        transform: translateX(4px);
    }}

    .stRadio > div[role="radiogroup"] > label[data-checked="true"] {{
        border-color: #60a5fa !important;
        background-color: rgba(96, 165, 250, 0.1) !important;
    }}
    
    /* Suppression des labels superflus */
    .st-emotion-cache-1qg05tj,
    .st-emotion-cache-1dx5vew0 {{
        display: none !important;
    }}

    /* Bouton de thème */
    .stButton > button {{
        background-color: {current_theme["sidebar_bg"]} !important;
        color: {current_theme["text_color"]} !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        width: 100% !important;
        padding: 0.5rem !important;
        margin: 0 0 1rem 0 !important;
        border-radius: 4px !important;
        cursor: pointer !important;
        transition: all 0.2s ease !important;
    }}

    .stButton > button:hover {{
        border-color: rgba(96, 165, 250, 0.4) !important;
        transform: translateX(4px);
    }}
    </style>
    """
    
    st.markdown(css, unsafe_allow_html=True)
