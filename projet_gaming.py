import streamlit as st
from PIL import Image

def display_project_concept():
    st.title("🎮 Concept PC Gaming adapté aux réels besoin du client")
    
    # Genèse du projet
    st.header("💡 Genèse du Projet")
    with st.expander("Découvrir l'origine du projet", expanded=True):
        col1, col2 = st.columns([2,1])
        with col1:
            st.markdown("""
            En discutant avec des amis me demandant conseils pour acheter un PC pour jouer, j'ai identifié plusieurs problématiques majeures
            dans le marché du PC Gaming. En effet, certains ont acheté des machines bien trop puissantes pour leurs besoins et déboursé bien plus d'argent que nécessaire,
            tandis que d'autres ont été déçus par les performances de leur ordinateur. Il y a aussi ceux qui ne sont jamais passés à l'acte se disant que les prix étaient inabordables.
                        
            C'est pourquoi j'ai décidé de créer un site web proposant des configurations de PC Gaming adaptées aux besoins réels des clients, avec des recommandations personnalisées
            et des tests de performances transparents pour répondre à ces problématiques.
                        
            - 🤔 **Complexité** : Difficulté pour les non-initiés de choisir un PC adapté à leurs besoins
            - 💰 **Budget** : Surcoût fréquent lié à des composants surdimensionnés
            - 📊 **Performances** : Manque de transparence sur les performances réelles
            - 🔍 **Conseil** : Absence d'accompagnement personnalisé
            """)
        with col2:
            try:
                image = Image.open(".assets/gaming_concept.jpg")
                st.image(image, caption="Concept PC Gaming")
            except:
                st.info("Image non disponible")

    # Solutions innovantes
    st.header("🚀 Solutions Innovantes")
    
    # Solution 1: Questionnaire intelligent
    st.subheader("📋 Questionnaire Intelligent")
    col1, col2 = st.columns([1,2])
    with col1:
        st.markdown("""
        - Analyse détaillée des besoins
        - Récuparation de la data
        - Recommandation parfaitement adaptée
        - Interface intuitive
        """)
    with col2:
        try:
            # Remplacer l'image par une vidéo
            video_file = open(".assets/demo_questionnaire.mp4", "rb")
            video_bytes = video_file.read()
            st.video(video_bytes, start_time=0)
        except Exception as e:
            st.info("Démo vidéo non disponible")
            print(f"Erreur: {e}")

    # Solution 2: Configurations Optimisées
    st.subheader("⚡ Configurations Optimisées")
    col1, col2 = st.columns([2,1])
    with col1:
        st.markdown("""
        - 5 gammes adaptées aux différents besoins
        - Rapport qualité/prix optimisé
        - Performances garanties
        - Compatibilité des composants
        - Évolutivité des configurations
        - Comparaison intuitive des gammes
        """)
    with col2:
        try:
            video_file = open(".assets/demo_configs.mp4", "rb")
            video_bytes = video_file.read()
            st.video(video_bytes, start_time=0)
        except Exception as e:
            st.info("Démo vidéo non disponible")
            print(f"Erreur: {e}")

    # Solution 3: Transparence Totale
    st.subheader("📊 Transparence Totale")
    col1, col2 = st.columns([1,2])
    with col1:
        st.markdown("""
        - Documentation détaillée des performances
        - Graphiques de performances
        - Vidéos des performances en jeu
        - Tests en conditions réelles
        """)
    with col2:
        try:
            video_file = open(".assets/demo_performances.mp4", "rb")
            video_bytes = video_file.read()
            st.video(video_bytes, start_time=0)
        except Exception as e:
            st.info("Démo vidéo non disponible")
            print(f"Erreur: {e}")
    
    # Démo du site
    st.header("🌐 Découvrir le Site")
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown("""
        <div style='text-align: center;'>
            <a href='https://gamingforall.odoo.com/' target='_blank'>
                <button style='
                    background-color: #FF4B4B;
                    color: white;
                    padding: 12px 20px;
                    border: none;
                    border-radius: 8px;
                    cursor: pointer;
                    font-size: 16px;
                '>
                    🔗 Visiter le Site
                </button>
            </a>
        </div>
        """, unsafe_allow_html=True)

    # Statistiques et résultats
    st.header("📈 Impact et Résultats")
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Performances comparées aux PC de grandes enseignes en moyenne", value="+20%", delta="20 FPS")
    with col2:
        st.metric(label="Économie Moyenne", value="210€", delta="par configuration")

if __name__ == "__main__":
    st.set_page_config(page_title="Projet PC Gaming", layout="wide")
    display_project_concept()
