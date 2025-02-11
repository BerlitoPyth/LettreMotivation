import streamlit as st
import openai

def init_floating_chat():
    # Configuration de l'API OpenAI
    if "OPENAI_API_KEY" not in st.secrets:
        st.error("Clé API OpenAI manquante dans les secrets")
        return
    
    openai.api_key = st.secrets["OPENAI_API_KEY"]
    
    # Initialisation de l'état du chat
    if 'chat_messages' not in st.session_state:
        st.session_state.chat_messages = []

    st.markdown("""
    <style>
    #floating-chat-container {
        position: fixed;
        bottom: 20px;
        right: 20px;
        z-index: 999999;
        font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    }

    #chat-button {
        display: none; /* Masquer le bouton de chat */
    }

    #chat-window {
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 380px;
        height: 500px;
        background: #1E1F25;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        display: flex;
        flex-direction: column;
        overflow: hidden;
        z-index: 999999;
        opacity: 1;
        visibility: visible;
    }

    .chat-header {
        padding: 16px;
        background: #2D3748;
        color: white;
        font-weight: 600;
        display: flex;
        align-items: center;
        justify-content: space-between;
        border-bottom: 1px solid rgba(255,255,255,0.1);
    }

    .chat-header-title {
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .chat-close {
        cursor: pointer;
        opacity: 0.8;
        transition: opacity 0.2s ease;
        padding: 4px 8px;
    }

    .chat-close:hover {
        opacity: 1;
    }

    .chat-body {
        flex-grow: 1;
        padding: 16px;
        overflow-y: auto;
        background: #1E1F25;
    }

    .message {
        max-width: 80%;
        padding: 10px 14px;
        margin-bottom: 10px;
        border-radius: 12px;
        font-size: 14px;
        line-height: 1.4;
    }

    .user-message {
        background: #3182CE;
        color: white;
        margin-left: auto;
        border-bottom-right-radius: 4px;
    }

    .bot-message {
        background: #2D3748;
        color: white;
        margin-right: auto;
        border-bottom-left-radius: 4px;
    }

    .chat-input-container {
        padding: 16px;
        background: #2D3748;
        border-top: 1px solid rgba(255,255,255,0.1);
    }

    .chat-input {
        width: 100%;
        padding: 10px;
        border-radius: 8px;
        border: 1px solid rgba(255,255,255,0.2);
        background: #1E1F25;
        color: white;
        font-size: 14px;
    }

    .chat-input:focus {
        outline: none;
        border-color: #3182CE;
    }

    .suggestions {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-top: 12px;
    }

    .suggestion-chip {
        padding: 6px 12px;
        background: rgba(49, 130, 206, 0.1);
        color: #60A5FA;
        border-radius: 16px;
        font-size: 12px;
        cursor: pointer;
        transition: all 0.2s ease;
    }

    .suggestion-chip:hover {
        background: rgba(49, 130, 206, 0.2);
    }

    @keyframes slideUp {
        from { transform: translateY(10px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }

    .animate-in {
        animation: slideUp 0.3s ease forwards;
    }
    </style>

    <div id="floating-chat-container">
        <div id="chat-window">
            <div class="chat-header">
                <div class="chat-header-title">
                    <span>💬</span>
                    <span>Chat avec Adrien</span>
                </div>
                <span class="chat-close">✕</span>
            </div>
            <div class="chat-body" id="chatBody">
                <div class="message bot-message">
                    Bonjour ! Je suis Adrien. N'hésitez pas à me poser des questions sur mon profil ou mes motivations !
                </div>
                <div class="suggestions">
                    <div class="suggestion-chip">Pourquoi le BUT SD ?</div>
                    <div class="suggestion-chip">Ton parcours ?</div>
                    <div class="suggestion-chip">Tes motivations ?</div>
                </div>
            </div>
            <div class="chat-input-container">
                <input type="text" class="chat-input" placeholder="Posez votre question...">
            </div>
        </div>
    </div>

    <script>
    document.addEventListener('DOMContentLoaded', function() {
        const chatWindow = document.getElementById('chat-window');
        const chatClose = document.querySelector('.chat-close');
        const chatInput = document.querySelector('.chat-input');
        const chatBody = document.getElementById('chatBody');
        const suggestionChips = document.querySelectorAll('.suggestion-chip');

        function closeChat() {
            chatWindow.style.display = 'none';
        }

        function appendMessage(message, isUser = false) {
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${isUser ? 'user-message' : 'bot-message'} animate-in`;
            messageDiv.textContent = message;
            chatBody.appendChild(messageDiv);
            chatBody.scrollTop = chatBody.scrollHeight;
        }

        async function sendMessage(message) {
            appendMessage(message, true);
            try {
                const queryString = new URLSearchParams({ message: message }).toString();
                const response = await fetch(`?${queryString}`, {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                    }
                });
                
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                
                const data = await response.json();
                if (data && data.response) {
                    appendMessage(data.response);
                } else {
                    throw new Error('Invalid response format');
                }
            } catch (error) {
                console.error('Error:', error);
                appendMessage('Désolé, une erreur est survenue. Veuillez réessayer.');
            }
        }

        chatClose.addEventListener('click', closeChat);

        chatInput.addEventListener('keypress', function(event) {
            if (event.key === 'Enter') {
                const message = this.value.trim();
                if (message) {
                    sendMessage(message);
                    this.value = '';
                }
            }
        });

        suggestionChips.forEach(chip => {
            chip.addEventListener('click', function() {
                sendMessage(this.textContent);
            });
        });
    });
    </script>
    """, unsafe_allow_html=True)

def handle_chat_input():
    system_prompt = """
    Tu es Adrien BERLIAT, et tu réponds aux questions sur ta candidature pour le BUT Science des Données. 
    
    Ton profil :
    - Actuellement en DAEU B avec d'excellents résultats en mathématiques
    - Ex-plongeur scaphandrier professionnel
    - Formation à l'École 42 et certifications Python
    - Passionné de programmation et de mathématiques
    - Grande capacité d'adaptation prouvée par ta reconversion
    
    Ton objectif : Intégrer le BUT Science des Données pour allier ta passion des mathématiques à l'informatique
    
    Réponds de manière professionnelle mais sympathique, en quelques phrases concises.
    Mets en avant ta motivation et ton parcours unique quand c'est pertinent.
    """
    
    try:
        if "message" in st.experimental_get_query_params():
            user_message = st.experimental_get_query_params()["message"][0]
            if user_message.strip():
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_message}
                    ],
                    temperature=0.7,
                    max_tokens=150
                )
                return {"response": response.choices[0].message["content"]}
    except Exception as e:
        st.error(f"Erreur: {str(e)}")
        return {"response": "Désolé, une erreur est survenue."}

def add_floating_chat_to_app():
    if "chat_initialized" not in st.session_state:
        init_floating_chat()
        st.session_state.chat_initialized = True
    
    response = handle_chat_input()
    if response:
        st.session_state.chat_messages.append(response)
