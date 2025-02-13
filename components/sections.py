import streamlit as st
from PIL import Image
from floating_chat import add_floating_chat_to_app
from lettre_motivation_content import get_lettre_motivation_content, get_note_importante
from projet_gaming import display_project_concept
from presentation import display_presentation
from quiz import display_quiz

def display_home():
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("""
            <div style="margin-bottom: 1rem;">
                <h1 style="
                    font-size: 2em;
                    margin-bottom: 0.5rem;
                    color: inherit;
                ">Candidature BUT Science des Données</h1>
                <h2 style="
                    font-size: 1.5em;
                    margin-bottom: 1rem;
                    color: inherit;
                ">Adrien BERLIAT</h2>
            </div>
        """, unsafe_allow_html=True)
        
        if 'title_written' not in st.session_state:
            write_text_slowly("De la profondeur des océans à la profondeur des données... 🌊➡️📊")
            st.session_state.title_written = True
        else:
            st.markdown("""
                <h3 style="
                    font-style: italic;
                    color: inherit;
                    font-size: 1.2em;
                    margin: 0 0 2rem 0;
                ">De la profondeur des océans à la profondeur des données... 🌊➡️📊</h3>
            """, unsafe_allow_html=True)
    
    with col2:
        try:
            image = Image.open(".assets/photo.jpg")
            image_rotated = image.rotate(-90, expand=True)
            st.image(image_rotated, width=200)
        except Exception as e:
            st.info("📸 Photo non disponible")
            print(f"Erreur: {e}")
    
    st.markdown("---")
    add_floating_chat_to_app()
    
    col1, col2 = st.columns(2)
    with col1:
        st.success("""
        ### ✨ Points Clés
        - 📊 Goût pour les mathématiques et l'informatique
        - 🤝 Expérience du travail d'équipe
        - 💡 Autodidacte
        - 🚀 Motivation à toute épreuve
        """)
    with col2:
        st.info("""
        ### 🎓 Formation Actuelle
        - 📚 DAEU B en cours
        - 💻 Certifications Python
        - 🔍 École 42 - La Piscine
        - 🌟 Excellents résultats en sciences
        """)
    
    st.markdown("---")
    display_lettre_motivation()

def display_lettre_motivation():
    st.markdown("""
        <h2 style="
            display: flex;
            align-items: center;
            gap: 0.5rem;
            margin: 1rem 0;
            line-height: 1.2;
        ">
            📜 Ma Lettre de Motivation
        </h2>
    """, unsafe_allow_html=True)
    
    st.markdown(get_lettre_motivation_content())
    st.markdown(get_note_importante(), unsafe_allow_html=True)

def write_text_slowly(text):
    placeholder = st.empty()
    for i in range(len(text) + 1):
        placeholder.markdown(f"### {text[:i]}▌")
        st.session_state.placeholder = placeholder
        time.sleep(0.03)
    placeholder.markdown(f"### {text}")

def display_sections(selection):
    if selection == "🏠 Accueil":
        display_home()
    elif selection == "👤 Présentation":
        display_presentation()
    elif selection == "🔧 Projet":
        display_project_concept()
    elif selection == "✨ Quiz":
        title_html = """
            <div style="
                margin-top: 20px;
                margin-bottom: 30px;
                scroll-margin-top: 60px;
            ">
                <h1 id="quiz-title">Découvrez si nous matchons ! ❤️</h1>
            </div>
        """
        st.markdown(title_html, unsafe_allow_html=True)
        display_quiz()
    elif selection == "📈 Parcours":
        st.markdown('<h1 id="parcours-title" class="custom-title">Mon Parcours</h1>', unsafe_allow_html=True)
    elif selection == "✉️ Motivation":
        st.markdown('<h1 id="motivation-title" class="custom-title">Ma Motivation</h1>', unsafe_allow_html=True)
