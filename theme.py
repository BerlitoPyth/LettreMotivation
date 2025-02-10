import streamlit as st

def toggle_theme():
    """
    Bascule entre le mode jour et nuit dans une application Streamlit.
    Gère les styles CSS pour une expérience utilisateur cohérente.
    Mode sombre activé par défaut.
    """
    # Initialisation de l'état du thème - mode sombre par défaut
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
    
    # Bouton de bascule avec icône et texte
    if st.button("🌙 / ☀️ Changer de thème"):
        st.session_state.dark_mode = not st.session_state.dark_mode
        # Force le rechargement de la page pour appliquer les changements
        st.rerun()
    
    # Sélection du thème actif
    current_theme = THEMES["dark"] if st.session_state.dark_mode else THEMES["light"]
    
    # Création du CSS dynamique
    css = f"""
    <style>
    /* Styles globaux */
    body, .stApp {{
        background-color: {current_theme["bg_color"]};
        color: {current_theme["text_color"]};
    }}
    
    /* Styles de la barre latérale */
    .stSidebar, .stSidebarContent {{
        background-color: {current_theme["sidebar_bg"]} !important;
        color: {current_theme["text_color"]} !important;
    }}
    
    /* Styles des conteneurs principaux */
    .st-emotion-cache-h4xjwg,
    .st-emotion-cache-15ecox0 {{
        background-color: {current_theme["bg_color"]} !important;
        color: {current_theme["text_color"]} !important;
    }}
    
    /* Styles de texte */
    h1, h2, h3, h4, h5, h6, p, span, div {{
        color: {current_theme["text_color"]} !important;
    }}
    
    /* Styles des éléments d'interface */
    .stTextInput,
    .stButton>button,
    .stSelectbox,
    .stRadio {{
        background-color: {current_theme["input_bg"]} !important;
        color: {current_theme["text_color"]} !important;
        border-color: {current_theme["border_color"]} !important;
    }}
    
    /* Styles des widgets DataFrames et tables */
    .dataframe {{
        color: {current_theme["text_color"]} !important;
    }}
    
    /* Styles des liens */
    a {{
        color: {current_theme["text_color"]} !important;
        text-decoration: underline;
    }}
    </style>
    """
    
    # Application du CSS
    st.markdown(css, unsafe_allow_html=True)
