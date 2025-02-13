import streamlit as st
from PIL import Image
from theme import toggle_theme

def display_navigation():
    return st.radio(
        "",
        ["🏠 Accueil",
         "✨ Quiz",
         "🔧 Projet",
         "👤 Présentation",
         "📈 Parcours",
         "✉️ Motivation"]
    )

def display_sidebar():
    col1, col2 = st.columns([4, 1])
    with col2:
        toggle_theme()
    
    st.title("🎯 Navigation")
    st.markdown("---")
    selection = display_navigation()
    display_sidebar_content()
    return selection

def display_sidebar_content():
    # Lettre de recommandation
    st.markdown("### 📄 Lettre de recommandation")
    try:
        if "lettre_agrandie" not in st.session_state:
            st.session_state.lettre_agrandie = False
        
        lettre = Image.open(".assets/lettre_recommandation.jpg")
        st.image(lettre, width=200, caption="Lettre de recommandation")
        if st.button("📄 Voir en plein écran"):
            st.session_state.lettre_agrandie = True
    except Exception as e:
        print(f"Erreur lors du chargement de la lettre: {str(e)}")
        st.error("Lettre de recommandation non disponible")

    st.markdown("---")
    
    # Section À propos
    st.markdown("### 👤 À propos")
    st.info("""
    🎓 DAEU B en cours
    🤿 Ex-Plongeur Scaphandrier
    💻 Passionné de programmation
    🔢 Amateur de mathématiques
    """)

    st.markdown("---")
    
    # Section Formations
    st.success("""
    ### 📚 Formations
    - DAEU B (en cours)
    - Python for Everybody
    - Python Data Structures
    - Using Python to Access Web Data
    - École 42 - La Piscine
    - École Nationale des Scaphandriers
    - Expérience professionnelle
    """)

def display_fullscreen_letter():
    overlay_container = st.container()
    with overlay_container:
        col1, col2, col3 = st.columns([1, 6, 1])
        with col2:
            try:
                lettre = Image.open(".assets/lettre_recommandation.jpg")
                st.image(lettre, use_container_width=True)
                if st.button("❌ Fermer", key="close_fullscreen"):
                    st.session_state.lettre_agrandie = False
                    st.rerun()
            except Exception as e:
                st.error("Impossible d'afficher la lettre en plein écran")
                print(f"Erreur: {e}")
