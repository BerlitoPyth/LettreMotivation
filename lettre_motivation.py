import streamlit as st
import time
from theme import toggle_theme
from quiz import display_quiz  
from presentation import display_presentation
from floating_chat import add_floating_chat_to_app
from PIL import Image
import random
from projet_gaming import display_project_concept

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

        nav_container = st.container()
        with nav_container:
            st.markdown("""
                <div style="
                    background-color: rgba(255, 255, 255, 0.05);
                    border: 1px solid rgba(255, 255, 255, 0.1);
                    border-radius: 8px;
                    padding: 16px;
                    margin: 10px 0;
                ">
            """, unsafe_allow_html=True)
            
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
            
            st.markdown("</div>", unsafe_allow_html=True)

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
        # Première rangée avec le titre et la photo
        col1, col2 = st.columns([3, 1])
        with col1:
            # Vérifier si le titre a déjà été écrit
            if 'title_written' not in st.session_state:
                write_text_slowly("De la profondeur des océans à la profondeur des données... 🌊➡️📊")
                st.session_state.title_written = True
            else:
                st.markdown("### De la profondeur des océans à la profondeur des données... 🌊➡️📊")
        
        with col2:
            try:
                # Photo en haut à droite
                image = Image.open(".assets/photo.jpg")
                image_rotated = image.rotate(-90, expand=True)
                st.image(image_rotated, width=200)
            except Exception as e:
                st.info("📸 Photo non disponible")
                print(f"Erreur: {e}")
        
        st.title("Candidature BUT Science des Données, BERLIAT Adrien")
        st.markdown("---")

        # Points clés
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
            - 📚 STI-2D
            - 💻 Certifications Python
            - 🔍 DAEU B à distance
            - 🌟 Excellents résultats en sciences
            """)

        st.markdown("---")

        # Lettre de motivation
        st.header("📝 Ma Lettre de Motivation")
        st.markdown("""
        Madame, Monsieur,
        
        C'est avec enthousiasme que je vous présente ma candidature pour le BUT Science des Données.
        Une formation qui représente pour moi l'opportunité idéale d'allier ma passion pour les mathématiques
        et l'informatique à mon désir d’acquérir les compétences nécessaires pour apprendre à faire parler les données,
        par là j'entends en extraire du sens et des informations utiles pour la prise de décision.
        
        Dès mon plus jeune âge, j’ai développé une affinité naturelle pour les mathématiques et la logique, et j’ai toujours
        trouvé la résolution de problèmes stimulante.
        
        Mon parcours, bien que singulier, reflète mon esprit d’initiative, ma détermination et ma capacité d’adaptation.
        Après avoir interrompu ma terminale STI2D, j’ai intégré la piscine de l’École 42, où j’ai découvert mon goût pour la
        programmation et renforcé ma logique algorithmique. 
        
        Le sport de haut niveau a également façonné ma persévérance : j’ai été, plus jeune, champion de France de pentathlon
        . Une expérience qui m’a appris le dépassement de soi et la rigueur. 
        
        Plus tard, mon expérience en tant que plongeur scaphandrier m’a permis d’évoluer dans un environnement exigeant où la précision,
        l’esprit d’équipe et la gestion du stress et la communication étaient primordiaux.
        
        Grâce à des échanges avec des data analysts, j’ai découvert ce domaine qui m’est rapidement apparu comme une évidence
        tant il correspond à mes affinités. Depuis, je m’y intéresse de près, suivant avec assiduité l’actualité du secteur ainsi 
        que des podcasts et conférences de professionnels.
        
        Suite à cette découverte, et après mûres réflexions, j’ai décidé de me réorienter vers la science des données et ai repris
        mes études avec un DAEU B en distanciel. Mon sérieux et mon engagement dans cette formation se reflètent à travers mes résultats 
        ainsi que la lettre de recommandation de mon professeur de physique. Cette reprise d’étude à distance m'a appris à m'organiser
        de manière autonome et à maintenir un haut niveau d'exigence dans mes études.
        
        Par ailleurs, en parallèle de mes révisions, je me suis formé à Python en passant des formations certifiantes sur Coursera. 
        J’ai aussi créé un concept innovant (voir section "Projet") dans le domaine du gaming. Cette expérience a renforcé ma conviction que l'analyse de données
        est un outil puissant et essentiel pour créer des solutions pertinentes.
        
        Lors des journées portes ouvertes de l’IUT, j’ai beaucoup apprécié l’ambiance générale ainsi que les échanges que j’ai pu avoir avec
        les enseignants et les étudiants, notamment avec Monsieur Mellouk, qui a gentiment pris le temps de répondre à mes questions.
        Cette expérience a d’autant plus renforcé mon envie d’intégrer votre établissement, qui correspond pleinement à mes attentes en termes 
        d’exigence et de quête d’excellence.
        
        Pour conclure, ma reconversion professionnelle est le fruit d'une réflexion approfondie et je suis convaincu que mon profil atypique 
        et mon désir d'apprendre seront des atouts précieux pour réussir et contribuer activement à la dynamique de votre formation.
        
        Je vous prie d'agréer, Madame, Monsieur, l'expression de mes sincères salutations.
        
        Adrien BERLIAT
        """)

        # Ajouter une boîte d'avertissement séparée
        st.markdown("""
            <div style="
                background-color: #7f1d1d;
                border: 2px solid #ef4444;
                border-radius: 12px;
                padding: 25px;
                margin: 30px 0;
                color: #fecaca;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.4);
            ">
                <div style="
                    font-size: 1.3em;
                    font-weight: bold;
                    margin-bottom: 16px;
                    padding-bottom: 12px;
                    border-bottom: 1px solid #ef4444;
                    display: flex;
                    align-items: center;
                    gap: 10px;
                    color: #fee2e2;
                ">
                    ⚠️ Note importante
                </div>
                <div style="
                    background-color: rgba(0, 0, 0, 0.2);
                    padding: 20px;
                    border-radius: 8px;
                    border: 1px solid rgba(239, 68, 68, 0.3);
                ">
                    <p style="line-height: 1.7; margin-bottom: 16px;">
                    Je tiens à préciser que je n'ai pas créé cette application pour mettre en avant mes compétences en programmation, j'aurais été
                    bien incapable de la réaliser sans l'aide d'ia génératives. Pour autant je considère ces dernières comme un outil dont il serait dommage de ne pas se servir
                    plutôt que comme une façon de "tricher".
                    </p>
                    <p style="line-height: 1.7; margin: 0;">
                    Le véritable objectif était de me démarquer en illustrant l'investissement que je mets dans mes projets
                    et mon désir de rejoindre votre établissement. J'ai toujours pensé qu'il est préférable d'agir que de parler. J'espère que vous aurez pris le
                    temps de me lire jusqu'ici et que cela vous aura convaincu car j'y ai consacré beaucoup de temps et d'efforts. Merci 😊
                    </p>
                </div>
            </div>
        """, unsafe_allow_html=True)

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
