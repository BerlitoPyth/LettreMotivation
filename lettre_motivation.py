import streamlit as st
import time
from theme import toggle_theme
from quiz import display_quiz  
from presentation import display_presentation
from floating_chat import add_floating_chat_to_app
from PIL import Image
import random
from projet_gaming import display_project_concept
from lettre_motivation_content import get_lettre_motivation_content, get_note_importante

# Remplacer la fonction scroll_to_section par :
def scroll_to_section(title_id):
    js = f'''
    <script>
        function scrollToTitle() {{
            const title = document.getElementById("{title_id}");
            if (title) {{
                title.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
            }}
        }}
        // Exécuter après un court délai pour s'assurer que le DOM est chargé
        setTimeout(scrollToTitle, 100);
    </script>
    '''
    st.markdown(js, unsafe_allow_html=True)

def write_text_slowly(text):
    """Fonction pour l'effet machine à écrire"""
    placeholder = st.empty()
    for i in range(len(text) + 1):
        placeholder.markdown(f"### {text[:i]}▌")
        time.sleep(0.03)
    placeholder.markdown(f"### {text}")

def display_data_animation():
    """Animation style Matrix en plein écran"""
    loading_container = st.empty()
    
    # Style CSS Matrix modifié pour le plein écran
    st.markdown("""
        <style>
        @keyframes matrix-rain {
            0% { transform: translateY(-100%); }
            100% { transform: translateY(100%); }
        }
        
        @keyframes glow {
            0% { text-shadow: 0 0 5px #0f0; }
            50% { text-shadow: 0 0 20px #0f0, 0 0 30px #0f0; }
            100% { text-shadow: 0 0 5px #0f0; }
        }
        
        .matrix-animation {
            font-family: 'Courier New', monospace;
            background-color: rgba(0, 0, 0, 0.95);
            color: #0f0;
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            z-index: 9999;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            overflow: hidden;
        }
        
        .binary-stream {
            font-size: 16px;
            letter-spacing: 4px;
            animation: glow 2s infinite;
            opacity: 0.8;
            position: relative;
            z-index: 2;
        }
        
        .message-text {
            font-size: 24px;
            margin: 20px 0;
            color: #fff;
            text-shadow: 0 0 10px #0f0;
            animation: glow 1.5s infinite;
            position: relative;
            z-index: 2;
        }
        
        .matrix-rain {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            display: flex;
            flex-wrap: wrap;
            justify-content: space-around;
            opacity: 0.3;
            pointer-events: none;
            z-index: 1;
        }
        
        .rain-column {
            animation: matrix-rain 2s linear infinite;
            animation-delay: var(--delay);
        }
        </style>
    """, unsafe_allow_html=True)

    # Animation Matrix avec colonnes de pluie
    matrix_chars = "01"
    rain_columns = 50  # Nombre de colonnes de pluie
    
    for i in range(50):
        binary = ''.join(random.choice(matrix_chars) for _ in range(40))
        rain_html = ''.join([
            f'<div class="rain-column" style="--delay: {random.random() * 2}s">{binary}</div>'
            for _ in range(rain_columns)
        ])
        
        loading_container.markdown(f"""
            <div class="matrix-animation">
                <div class="matrix-rain">{rain_html}</div>
                <div class="binary-stream">{binary[:int(i/50*len(binary))]}▌</div>
                <div class="message-text">📊 Initialisation de la Matrice...</div>
            </div>
        """, unsafe_allow_html=True)
        time.sleep(0.02)
    
    time.sleep(0.5)
    
    # Message final avec effet Matrix
    loading_container.markdown(f"""
        <div class="matrix-animation">
            <div class="matrix-rain">{rain_html}</div>
            <div class="binary-stream">{binary}</div>
            <div class="message-text">🚀 Bienvenue dans la Matrice. Merci pour le temps que vous m'accordez.</div>
        </div>
    """, unsafe_allow_html=True)
    time.sleep(1.5)
    loading_container.empty()

def main():
    st.set_page_config(
        page_title="Candidature BUT Science des Données",
        layout="wide"
    )

    # Ajouter l'animation au début
    if 'animation_shown' not in st.session_state:
        display_data_animation()
        st.session_state.animation_shown = True
    
    # Afficher le toggle theme après l'animation ou directement si déjà montrée
    toggle_theme()

    # Ajouter le chat après l'animation
    add_floating_chat_to_app()

    # Style personnalisé
    st.markdown("""
        <style>
        .main {
            padding: 2rem;
        }
        .highlight {
            background-color: #f0f2f6;
            padding: 1rem;
            border-radius: 0.5rem;
        }
        .stButton > button {
            width: 100%;
        }
        .stImage {
            transition: transform 0.3s ease;
        }
        .stImage:hover {
            transform: scale(1.02);
            cursor: pointer;
        }
        .thumbnail-container {
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 5px;
        }
        .streamlit-title {
            scroll-margin-top: 20px;
        }
        #section-title {
            margin-top: 0;
            padding-top: 2rem;
        }
        .section-title {
            scroll-margin-top: 60px;
            opacity: 0;
            transition: opacity 0.5s;
        }
        .section-title.visible {
            opacity: 1;
        }
        .warning-box {
            background-color: #fee2e2;
            border: 1px solid #ef4444;
            border-radius: 8px;
            padding: 16px;
            margin: 20px 0;
            color: #991b1b;
        }
        .warning-title {
            font-size: 1.2em;
            font-weight: bold;
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .custom-title {
            margin-top: 1rem;
            margin-bottom: 2rem;
            padding-top: 2rem;
            scroll-margin-top: 60px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Sidebar
    with st.sidebar:
        st.title("🎯 Navigation")
        st.markdown("---")

        # Menu de navigation
        selection = st.radio(
            "",
            ["🏠 Accueil",
             "✨ Quiz",
             "🔧 Projet",
             "👤 Présentation",
             "📈 Parcours",
             "✉️ Motivation"]
        )
        st.session_state.selection = selection
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
        st.markdown("### 👤 À propos")
        st.info("""
        🎓 DAEU B en cours
        🤿 Ex-Plongeur Scaphandrier
        💻 Passionné de programmation
        🔢 Amateur de mathématiques
        """)

        st.markdown("---")
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

    # Affichage plein écran de la lettre si demandé
    if st.session_state.get('lettre_agrandie', False):
        # Création d'une overlay pour l'image en plein écran
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

    # Contenu principal basé sur la sélection
    if selection == "🏠 Accueil":
        # Conteneur principal avec titre et photo
        col1, col2 = st.columns([3, 1])
        
        with col1:
            # Titre principal avec style personnalisé
            st.markdown("""
                <h1 style="
                    font-size: 2em;
                    margin-bottom: 0.5rem;
                    color: inherit;
                ">Candidature BUT Science des Données</h1>
                <h2 style="
                    font-size: 1.5em;
                    margin-bottom: 2rem;
                    color: inherit;
                ">Adrien BERLIAT</h2>
            """, unsafe_allow_html=True)
            
            # Citation avec effet machine à écrire
            if 'title_written' not in st.session_state:
                write_text_slowly("De la profondeur des océans à la profondeur des données... 🌊➡️📊")
                st.session_state.title_written = True
            else:
                st.markdown("""
                    <h3 style="
                        font-style: italic;
                        margin-top: 0;
                        color: inherit;
                    ">De la profondeur des océans à la profondeur des données... 🌊➡️📊</h3>
                """, unsafe_allow_html=True)
        
        with col2:
            try:
                # Photo alignée en haut
                image = Image.open(".assets/photo.jpg")
                image_rotated = image.rotate(-90, expand=True)
                st.image(image_rotated, width=200)
            except Exception as e:
                st.info("📸 Photo non disponible")
                print(f"Erreur: {e}")
        
        st.markdown("---")

        # Le reste du code reste inchangé...

    elif selection == "👤 Présentation":
        display_presentation()

        st.markdown("---")
        
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
        scroll_to_section("quiz-title")
        display_quiz()
        
    elif selection == "📈 Parcours":
        st.markdown('<h1 id="parcours-title" class="custom-title">Mon Parcours</h1>', unsafe_allow_html=True)
        scroll_to_section("parcours-title")


    elif selection == "✉️ Motivation":
        st.markdown('<h1 id="motivation-title" class="custom-title">Ma Motivation</h1>', unsafe_allow_html=True)
        scroll_to_section("motivation-title")

    # Footer
    st.markdown("---")
    st.markdown("*Application interactive créé pour accompagner ma candidature au BUT Science des Données*")

if __name__ == "__main__":
    main()
