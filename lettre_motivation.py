import streamlit as st
import time
from theme import toggle_theme
from quiz import display_quiz  
from presentation import display_presentation
from floating_chat import add_floating_chat_to_app
from PIL import Image
import random

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
        st.session_state.animation_shown = False
        display_data_animation()
        st.session_state.animation_shown = True
        
    # Déplacer le toggle_theme après l'animation
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
             "👤 Présentation",
             "📈 Parcours",
             "🔧 Projets",
             "✉️ Motivation"]
        )

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
            # Animation du titre
            write_text_slowly("De la profondeur des océans à la profondeur des données... 🌊➡️📊")
        
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
            - 📊 Goût pour les mathématiques et l'informatique depuis l'enfance
            - 🤝 Expérience du travail d'équipe en conditions exigeantes
            - 💡 Capacité d'adaptation prouvée
            - 🎯 Formation continue en programmation
            - 🚀 Motivation à toute épreuve
            """)
        with col2:
            st.info("""
            ### 🎓 Formation Actuelle
            - 📚 DAEU B à distance
            - 💻 Certifications Python
            - 🔍 Auto-formation continue
            - 🌟 Excellents résultats en mathématiques
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
        J’ai aussi créé un concept innovant (voir section "Projet") de vente de PC gaming basé sur l'analyse détaillée des besoins clients à travers un questionnaire
        sur mesure et des performances réelles des machines sur les différents jeux. Cette expérience a renforcé ma conviction que l'analyse de données
        est un outil puissant et essentiel pour créer des solutions pertinentes.
        
        Lors des journées portes ouvertes de l’IUT, j’ai beaucoup apprécié l’ambiance générale ainsi que les échanges que j’ai pu avoir avec
        les enseignants et les étudiants, notamment avec Monsieur Mellouk, qui a gentiment pris le temps de répondre à mes questions.
        Cette expérience a d’autant plus renforcé mon envie d’intégrer votre établissement, qui correspond pleinement à mes attentes en termes 
        d’exigence et de quête d’excellence.
        
        Pour conclure, ma reconversion professionnelle est le fruit d'une réflexion approfondie et je suis convaincu que mon profil atypique 
        et mon désir d'apprendre seront des atouts précieux pour réussir et contribuer activement à la dynamique de votre formation.
        
        Je vous prie d'agréer, Madame, Monsieur, l'expression de mes sincères salutations.
        
        Adrien BERLIAT

        PS : Je tiens à préciser que je n’ai pas créé cette application pour mettre en avant mes compétences en programmation, j’aurais été
        bien incapable de la réaliser seul. Le véritable objectif était de me démarquer en illustrant l’investissement que je mets dans mes projets
        et mon désir de rejoindre votre établissement. J’ai toujours pensé qu’il est préférable d’agir que de parler. J’espère que vous aurez pris le
        temps de me lire jusqu’ici et que cela vous aura convaincu car j’y ai consacré beaucoup de temps et d’efforts. Merci :)
                    

        """)

    elif selection == "👤 Présentation":
        display_presentation()

        col1, col2 = st.columns(2)
        with col1:
            st.info("""
            ### 🎯 A propos de moi 

            Un professionnel en reconversion, avec un parcours peu commun :
            - Terminale STI2D
            - Première expérience de code à l'École 42
            - Plongeur Scaphandrier Travaux Publics
            - Intérêt pour l'informatique et les mathématiques (LA Mathématique ;) )
            - Entrepreneur en herbe dans le domaine du gaming
            - Formations certifiantes Python
            - DAEU B
            """)
        with col2:
            st.success("""
            ### 🚀 Mon Projet

            Intégrer le BUT Science des Données pour :
            - Me préparer à un Master ou une école d'ingénieur
            - Évoluer professionnellement dans un domaine innovant
            - Apprendre à utiliser la Data pour concrétiser des projets
            - Combiner mathématiques et programmation
            - Relever de nouveaux défis stimulants
            """)

        st.markdown("---")

    elif selection == "✨ Quiz":
        st.title("Découvrez si nous matchons !")
        display_quiz()
        
    elif selection == "📈 Parcours":
        st.title("Mon Parcours")

        st.info("""
        ### 💻 Premier Pas dans l'Informatique

        École 42 - La Piscine :
        - Immersion intensive en programmation
        - Apprentissage des bases de l'algorithmie
        - Travail en peer-learning
        - Développement de la logique de programmation
        """)

        st.success("""
        ### 🤿 Plongeur Scaphandrier

        Un métier exigeant qui m'a formé à :
        - La rigueur technique et la précision
        - La gestion du stress en conditions difficiles
        - La résolution de problèmes
        - La communication efficace en équipe
        - L'adaptabilité permanente face aux imprévus
        """)

        st.warning("""
        ### 🛠️ Projet Entrepreneurial

        Création d'un concept innovant de vente PC Gaming :
        - Analyse détaillée des besoins clients
        - Vulgarisation pour les nouveaux utilisateurs de PC
        - Développement d'un questionnaire structuré pour satisfaire les besoins du client
        - Création de configurations optimisées 
        - Démonstration des performances et transparence totale
        - Approche basée sur les données
        """)

    elif selection == "🔧 Projets":
        display_project_concept()

    elif selection == "✉️ Motivation":
        st.title("Ma Motivation")

        st.info("""
        ### 💫 Mon Parcours vers la Data Science

        Une progression logique à travers :
        - Première expérience de code à l'École 42
        - Création d'un projet basé sur les données
        - Formations Python
        - Passion continue pour l'analyse et les mathématiques
        """)

        st.success("""
        ### 🎯 Pourquoi ce BUT ?

        Cette formation correspond parfaitement à mon projet car elle :
        - Offre une formation complète et pratique
        - Combine théorie et applications
        - Permet une progression structurée
        - Prépare au monde professionnel
        """)

        st.warning("""
        ### 💪 Mes Atouts

        Mon parcours atypique est une force car il démontre :
        - Une capacité d'adaptation éprouvée
        - Une expérience concrète du travail en équipe
        - Un sens aigu de la rigueur et de la précision
        - Une motivation et une détermination solides
        - Une approche data-driven déjà mise en pratique
        """)

    # Footer
    st.markdown("---")
    st.markdown("*Document interactif créé pour accompagner ma candidature au BUT Science des Données*")

if __name__ == "__main__":
    main()
