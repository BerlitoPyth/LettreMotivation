import streamlit as st
import openai
from streamlit_chat import message

def init_chatbot():
    # Configuration de l'API OpenAI
    openai.api_key = st.secrets["OPENAI_API_KEY"]
    
    # Instructions au chatbot sur votre profil
    system_prompt = """
    Tu es Adrien BERLIAT, candidat pour le BUT Science des Données. Voici ton profil :
    - Actuellement en DAEU B avec d'excellents résultats en mathématiques
    - Ex-plongeur scaphandrier professionnel
    - Passionné de programmation, formé à l'École 42
    - Très motivé et déterminé à réussir dans le domaine de la data science
    - Excellent esprit d'équipe développé lors de ton expérience de plongeur
    - Capacité d'adaptation exceptionnelle prouvée par ta reconversion
    
    Réponds aux questions comme si tu étais moi. Sois professionnel mais sympathique.
    Mets en avant ma motivation et mon parcours unique.
    """
    
    return system_prompt

def get_response(user_input, system_prompt):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ]
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7
    )
    
    return response.choices[0].message["content"]

def display_chatbot():
    st.title("💬 Discutez avec moi !")
    
    # Initialisation
    if 'messages' not in st.session_state:
        st.session_state.messages = []
        
    system_prompt = init_chatbot()
    
    # Zone de saisie
    user_input = st.chat_input("Posez-moi une question sur mon profil, mes motivations...")
    
    if user_input:
        # Ajouter la question de l'utilisateur
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Obtenir la réponse du chatbot
        response = get_response(user_input, system_prompt)
        st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Afficher l'historique des messages
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.chat_message("user").write(msg["content"])
        else:
            st.chat_message("assistant").write(msg["content"])

    # Suggestions de questions
    if not st.session_state.messages:
        st.markdown("""
        ### Suggestions de questions :
        - Pourquoi as-tu choisi le BUT Science des Données ?
        - Que t'a apporté ton expérience de plongeur ?
        - Comment te prépares-tu pour cette formation ?
        - Quels sont tes projets à long terme ?
        """)