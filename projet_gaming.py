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
        - Questions adaptatives
        - Recommandations personnalisées
        - Interface intuitive
        """)
    with col2:
        try:
            image = Image.open(".assets/questionnaire.jpg")
            st.image(image, caption="Interface du questionnaire")
        except:
            st.info("Capture d'écran non disponible")

    # Solution 2: Configurations optimisées
    st.subheader("⚡ Configurations Optimisées")
    col1, col2 = st.columns([2,1])
    with col1:
        st.markdown("""
        - 5 gammes adaptées aux différents profils
        - Rapport qualité/prix optimisé
        - Performances garanties
        - Tests réels sur les jeux populaires
        """)
    with col2:
        try:
            image = Image.open(".assets/configs.jpg")
            st.image(image, caption="Exemples de configurations")
        except:
            st.info("Image non disponible")

    # Solution 3: Transparence totale
    st.subheader("📊 Transparence Totale")
    st.markdown("""
    - Documentation détaillée des performances
    - Benchmarks personnalisés
    - Comparatifs visuels
    - Tests en conditions réelles
    """)
    
    # Démo du site
    st.header("🌐 Découvrir le Site")
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown("""
        <div style='text-align: center;'>
            <a href='https://votre-site.com' target='_blank'>
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
        st.metric(label="Satisfaction Client", value="95%", delta="+15%")
    with col2:
        st.metric(label="Économie Moyenne", value="200€", delta="par configuration")

if __name__ == "__main__":
    st.set_page_config(page_title="Projet PC Gaming", layout="wide")
    display_project_concept()