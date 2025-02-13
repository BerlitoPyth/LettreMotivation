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
from styles.main import get_main_styles
from animations.matrix import get_matrix_styles

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

    # Apply styles
    st.markdown(get_main_styles(), unsafe_allow_html=True)
    
    if 'animation_shown' not in st.session_state:
        st.markdown(get_matrix_styles(), unsafe_allow_html=True)
        display_data_animation()
        st.session_state.animation_shown = True

    # Sidebar
    with st.sidebar:
        col1, col2 = st.columns([4, 1])
        with col2:
            toggle_theme()
        
        st.title("🎯 Navigation")
        display_navigation()  # Move navigation logic to separate function
    
    # Content
    if st.session_state.get('lettre_agrandie', False):
        display_fullscreen_letter()
    
    # Main content based on selection
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
