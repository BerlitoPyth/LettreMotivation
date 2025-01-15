import streamlit as st
import time


def write_text_slowly(text):
    """Fonction pour l'effet machine à écrire"""
    placeholder = st.empty()
    for i in range(len(text) + 1):
        placeholder.markdown(f"### {text[:i]}▌")
        time.sleep(0.03)
    placeholder.markdown(f"### {text}")


def main():
    st.set_page_config(
        page_title="Candidature BUT Science des Données",
        layout="wide"
    )

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
             "👤 Présentation",
             "📈 Parcours",
             "🔧 Projets",
             "✉️ Motivation"]
        )

        # Informations dans la sidebar
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
        - Using Python to Acces Web Data
        - École 42 - La Piscine
        - École Nationale des Scaphandriers
        - Expérience professionnelle
        """)

    # Contenu principal basé sur la sélection
    if selection == "🏠 Accueil":
        col1, col2 = st.columns([3, 1])
        with col1:
            # Animation du titre
            write_text_slowly("De la profondeur des océans à la profondeur des données... 🌊➡️📊")
        with col2:
            try:
                # Photo en haut à droite
                import PIL
                from PIL import Image
                image = Image.open("photo.jpg")
                image_rotated = image.rotate(-90, expand=True)
                st.image(image_rotated, width=200)
            except Exception as e:
                st.info("📸 Photo non disponible")

        st.title("Candidature BUT Science des Données, BERLIAT Adrien")
        st.markdown("---")

        # Points clés
        col1, col2 = st.columns(2)
        with col1:
            st.success("""
            ### ✨ Points Clés
            - 📊 Goût pour les mathématiques depuis l'enfance
            - 🤝 Expérience du travail d'équipe en conditions exigeantes
            - 💡 Capacité d'adaptation prouvée
            - 🎯 Formation continue en programmation
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

        C'est avec enthousiasme que je vous présente ma candidature pour le BUT Science des Données, une formation qui représente 
        pour moi l'opportunité idéale d'allier ma passion pour les mathématiques et l'informatique à mon désir d'évolution professionnelle.

        Mon parcours, bien qu'atypique, témoigne de mon intérêt précoce pour le monde numérique et de ma capacité d'adaptation. 
        À 17 ans, après le lycée, j'ai participé à la "piscine" de l'École 42, une expérience intense d'un mois en programmation 
        qui a confirmé mon attrait pour le développement informatique. Cette première immersion dans le code m'a appris l'importance 
        de la persévérance et de la logique algorithmique.

        Par la suite, en tant que plongeur scaphandrier, j'ai évolué dans un environnement exigeant où la précision, le travail 
        d'équipe et la gestion du stress étaient essentiels. Cette expérience m'a appris l'importance de la rigueur et de la 
        communication claire, des compétences précieuses dans le domaine de la data science.

        Cette capacité à relever des défis remonte à ma jeunesse. À l'âge de 11 ans, j'ai remporté le titre de champion de France de
        pentathlon lors de ma première participation à ce championnat national. Cet accomplissement m'a appris très tôt que la
        persévérance, la rigueur et l'engagement sont indispensables pour atteindre ses objectifs, des qualités que je mets en pratique
        dans tous les aspects de ma vie.

        Mon intérêt pour la technologie et l'analyse de données s'est récemment concrétisé à travers un projet entrepreneurial 
        innovant. J'ai créé un concept de vente de PC gaming basé sur l'analyse détaillée des besoins clients et des performances 
        réelles. Ce projet m'a permis de développer une approche data-driven : création d'un questionnaire client structuré, 
        analyse des besoins, création de tableaux de performances, et visualisation des données pour aider à la décision. 
        Cette expérience a renforcé ma conviction que l'analyse de données est un outil puissant pour créer des solutions 
        pertinentes et accessibles.

        En parallèle, j'ai commencé à explorer des projets d'initiation sur Kaggle afin de me familiariser avec l'analyse de données.
        Ces exercices m'ont permis de découvrir des techniques pratiques pour la manipulation et l'interprétation des données, tout 
        en renforçant mon appétence pour ce domaine.

        Les mathématiques ont toujours été une passion pour moi. Cette affinité naturelle, présente depuis mon plus jeune âge, 
        s'est pleinement confirmée lors de ma reprise d'études en DAEU B. J'ai choisi de suivre cette formation à distance, 
        ce qui démontre ma capacité à m'organiser de manière autonome et à maintenir un haut niveau d'exigence dans mes études. 
        Les excellents résultats obtenus en mathématiques confirment cette facilité et ce goût pour les raisonnements logiques.

        Pour préparer ma reconversion et maximiser mes chances de réussite, j'ai pris l'initiative de suivre des formations certifiantes
        en Python sur Coursera, ce qui a consolidé mon intérêt pour la programmation et le secteur de la data.

        Le BUT Science des Données représente pour moi l'alliance parfaite entre :
        - Ma passion historique pour les mathématiques
        - Mon expérience précoce en programmation avec l'École 42
        - Mes projets personnels orientés data
        - Mon goût pour les défis techniques
        - Mon désir d'apprentissage continu

        Ma reconversion professionnelle est le fruit d'une réflexion approfondie. Je suis pleinement conscient des efforts 
        qu'implique ce changement de carrière, mais ma détermination et mes capacités d'adaptation, prouvées par mon parcours, 
        sont des atouts solides pour réussir dans cette voie. Mon expérience en tant que plongeur scaphandrier m'a appris 
        qu'aucun défi n'est insurmontable avec de la persévérance et de la rigueur.

        Je suis convaincu que mon profil atypique, alliant expérience professionnelle, passion pour les mathématiques et 
        motivation à apprendre, serait un atout pour votre formation. Ma maturité professionnelle et mon engagement dans 
        l'auto-formation démontrent mon sérieux et ma capacité à mener à bien ce projet de reconversion.

        Je reste à votre disposition pour un entretien où je pourrai vous exposer plus en détail ma motivation et mon projet 
        professionnel.

        Je vous prie d'agréer, Madame, Monsieur, l'expression de mes sincères salutations.
        """)

    elif selection == "👤 Présentation":
        st.title("Présentation")

        col1, col2 = st.columns(2)
        with col1:
            st.info("""
            ### 🎯 Qui suis-je ?

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
            - Apprendre à utiliser la Data pour concrétiser des projets personnels
            - Combiner mathématiques et programmation
            - Relever de nouveaux défis stimulants
            - Évoluer dans un domaine innovant
            """)

        st.markdown("---")

        st.warning("""
        ### 💫 Ma Démarche

        Une progression logique vers la data science :
        - Premier contact avec le code à l'École 42
        - Développement d'un projet basé sur les données
        - Retour aux études via le DAEU B
        - Formation complémentaire en programmation (Python)
        - Veille technologique régulière
        """)

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
        - Développement d'un questionnaire structuré pour satisfaire le besoin du client
        - Création de configurations optimisées
        - Documentation des performances
        - Approche basée sur les données
        """)


    elif selection == "🔧 Projets":
        st.title("Mes Projets")

        st.info("""
        ### 🖥️ Projet PC Gamer

        Création d'un concept innovant de vente de PC gaming :
        - **Analyse des Besoins :**
            - Développement d'un questionnaire client détaillé
            - Analyse des usages (gaming, streaming, montage)
            - Étude des exigences techniques par jeu

        - **Solution Innovante :**
            - Création de 5 gammes (configurations) optimisées et adaptées aux besoins du client
            - Tableaux de performances détaillés
            - Tests réels sur différents jeux
            - Documentation vidéo des performances

        - **Objectif :**
            - Démocratiser le PC gaming
            - Conseils personnalisés basés sur les données
            - Transparence sur les performances réelles
        """)

        st.success("""
        ### 💻 École 42 - La Piscine

        Une expérience formatrice :
        - Un mois d'immersion totale en programmation
        - Apprentissage de la méthode peer-learning
        - Développement de la persévérance
        """)

        st.warning("""
        ### 📊 Formations Python

        Un parcours complet comprenant :
        - Apprentissage des fondamentaux Python
        - Structures de données
        - Utilisation de Python pour accéser aux données Web
        - Utilisation des bases de données avec Python
        """)

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
