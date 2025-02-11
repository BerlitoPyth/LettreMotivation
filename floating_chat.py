import streamlit as st
from openai import OpenAI

def init_chat_client():
    """Initialize OpenAI client with API key"""
    if "OPENAI_API_KEY" not in st.secrets:
        st.error("Clé API OpenAI manquante dans les secrets")
        return None
    return OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def create_chat_interface():
    """Create chat interface using Streamlit components"""
    st.markdown("""
        <style>
        .chat-container {
            border-radius: 10px;
            background-color: #1E1F25;
            padding: 20px;
            margin-bottom: 20px;
        }
        .user-message {
            background-color: #3182CE;
            color: white;
            padding: 10px;
            border-radius: 10px;
            margin: 5px 0;
            text-align: right;
        }
        .bot-message {
            background-color: #2D3748;
            color: white;
            padding: 10px;
            border-radius: 10px;
            margin: 5px 0;
        }
        </style>
    """, unsafe_allow_html=True)

def generate_response(client, message, conversation_history):
    """Generate response using OpenAI API"""
    system_prompt = """
    Tu es Adrien BERLIAT, et tu réponds aux questions sur ta candidature pour le BUT Science des Données.
    
    Ton profil :
    - Actuellement en DAEU B avec d'excellents résultats en mathématiques
    - Ex-plongeur scaphandrier professionnel
    - Formation à l'École 42 et certifications Python
    - Passionné de programmation et de mathématiques
    - Grande capacité d'adaptation prouvée par ta reconversion
    
    Ton objectif : Intégrer le BUT Science des Données pour allier ta passion des mathématiques à l'informatique.
    
    Réponds de manière professionnelle mais sympathique, en quelques phrases concises.
    Mets en avant ta motivation et ton parcours unique quand c'est pertinent.
    """
    
    messages = [
        {"role": "system", "content": system_prompt},
        *conversation_history,
        {"role": "user", "content": message}
    ]
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Erreur: {str(e)}")
        return "Désolé, une erreur est survenue."

def add_floating_chat_to_app():
    """Main function to add chat functionality to Streamlit app"""
    # Initialize chat state
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Initialize OpenAI client
    client = init_chat_client()
    if not client:
        return
    
    # Create chat interface
    create_chat_interface()
    
    # Chat container
    with st.container():
        # Display chat history
        for message in st.session_state.messages:
            div_class = "user-message" if message["role"] == "user" else "bot-message"
            st.markdown(f"""
                <div class="{div_class}">
                    {message["content"]}
                </div>
            """, unsafe_allow_html=True)
        
        # Chat input
        if prompt := st.chat_input("Posez votre question..."):
            # Add user message to state
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # Generate response
            response = generate_response(client, prompt, st.session_state.messages)
            
            # Add assistant response to state
            st.session_state.messages.append({"role": "assistant", "content": response})
            
            # Rerun to update chat display
            st.rerun()

        # Suggestion buttons
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Pourquoi le BUT SD ?"):
                st.session_state.messages.append({"role": "user", "content": "Pourquoi le BUT SD ?"})
                response = generate_response(client, "Pourquoi le BUT SD ?", st.session_state.messages)
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.rerun()
        with col2:
            if st.button("Ton parcours ?"):
                st.session_state.messages.append({"role": "user", "content": "Quel est ton parcours ?"})
                response = generate_response(client, "Quel est ton parcours ?", st.session_state.messages)
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.rerun()
        with col3:
            if st.button("Tes motivations ?"):
                st.session_state.messages.append({"role": "user", "content": "Quelles sont tes motivations ?"})
                response = generate_response(client, "Quelles sont tes motivations ?", st.session_state.messages)
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.rerun()
