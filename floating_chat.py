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
        width: 60px;
        height: 60px;
        border-radius: 30px;
        background: #2D3748;
        box-shadow: 0 2px 12px rgba(0,0,0,0.2);
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        color: white;
        border: none;
        transition: transform 0.3s ease;
        z-index: 999999;
    }

    #chat-button:hover {
        transform: scale(1.1);
    }

    #chat-window {
        position: fixed;
        bottom: 90px;
        right: 20px;
        width: 380px;
        height: 500px;
        background: #1E1F25;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        display: none;
        flex-direction: column;
        overflow: hidden;
        z-index: 999999;
        opacity: 0;
        visibility: hidden;
        transition: opacity 0.3s ease, visibility 0.3s ease;
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

    #chat-window.open {
        display: flex !important;
        opacity: 1;
        visibility: visible;
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
        <button id="chat-button">💬</button>
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
        // Éléments du DOM
        const chatButton = document.getElementById('chat-button');
        const chatWindow = document.getElementById('chat-window');
        const chatClose = document.querySelector('.chat-close');
        const chatInput = document.querySelector('.chat-input');
        const chatBody = document.getElementById('chatBody');
        const suggestionChips = document.querySelectorAll('.suggestion-chip');

        // Fonction pour basculer l'affichage du chat
        function toggleChat() {
            chatWindow.classList.toggle('open');
        }

        // Fonction pour ajouter un message
        function appendMessage(message, isUser = false) {
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${isUser ? 'user-message' : 'bot-message'} animate-in`;
            messageDiv.textContent = message;
            chatBody.appendChild(messageDiv);
            chatBody.scrollTop = chatBody.scrollHeight;
        }

        // Fonction pour envoyer un message
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

        // Event Listeners
        chatButton.addEventListener('click', toggleChat);
        chatClose.addEventListener('click', toggleChat);

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

    <script>
    (function() {
        function initChat() {
            const chatButton = document.getElementById('chat-button');
            const chatWindow = document.getElementById('chat-window');
            const chatClose = document.querySelector('.chat-close');

            if (!chatButton || !chatWindow || !chatClose) {
                console.error('Chat elements not found');
                return;
            }

            console.log('Chat elements found:', { chatButton, chatWindow, chatClose });

            function toggleChat(event) {
                if (event) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                chatWindow.classList.toggle('open');
                console.log('Chat toggled:', chatWindow.classList.contains('open'));
            }

            // Remove previous event listeners
            chatButton.replaceWith(chatButton.cloneNode(true));
            chatClose.replaceWith(chatClose.cloneNode(true));

            // Get fresh references
            const newChatButton = document.getElementById('chat-button');
            const newChatClose = document.querySelector('.chat-close');

            // Add new event listeners
            newChatButton.onclick = toggleChat;
            newChatClose.onclick = toggleChat;
        }

        // Initialize immediately
        initChat();

        // Initialize after DOM content loaded
        document.addEventListener('DOMContentLoaded', initChat);

        // Periodically check for elements
        const initInterval = setInterval(initChat, 1000);
        setTimeout(() => clearInterval(initInterval), 5000);
    })();
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
        # Utiliser st.query_params au lieu de st.experimental_get_query_params
        if "message" in st.query_params:
            user_message = st.query_params["message"]
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
    
    # Utiliser st.query_params
    if "message" in st.query_params:
        return handle_chat_input()
