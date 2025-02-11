import streamlit as st
import openai

def init_floating_chat():
    # Configuration de l'API OpenAI
    openai.api_key = st.secrets["OPENAI_API_KEY"]
    
    # Initialisation de l'état du chat
    if 'chat_messages' not in st.session_state:
        st.session_state.chat_messages = []

    st.markdown("""
    <style>
    /* Styles de base */
    #floating-chat-container {
        position: fixed;
        bottom: 20px;
        right: 20px;
        z-index: 9999;
        font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* Bouton de chat */
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
    }

    #chat-button:hover {
        transform: scale(1.1);
    }

    /* Fenêtre de chat */
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
    }

    /* En-tête du chat */
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
    }

    .chat-close:hover {
        opacity: 1;
    }

    /* Corps du chat */
    .chat-body {
        flex-grow: 1;
        padding: 16px;
        overflow-y: auto;
        display: flex;
        flex-direction: column;
        gap: 12px;
    }

    /* Messages */
    .message {
        max-width: 80%;
        padding: 10px 14px;
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

    /* Zone de saisie */
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

    /* Suggestions */
    .suggestions {
        padding: 16px;
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
    }

    .suggestion-chip {
        padding: 6px 12px;
        background: rgba(49, 130, 206, 0.1);
        color: #3182CE;
        border-radius: 16px;
        font-size: 12px;
        cursor: pointer;
        transition: all 0.2s ease;
    }

    .suggestion-chip:hover {
        background: rgba(49, 130, 206, 0.2);
    }

    /* Animations */
    @keyframes slideUp {
        from { transform: translateY(20px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }

    .chat-window.open {
        display: flex;
        animation: slideUp 0.3s ease;
    }
    </style>

    <div id="floating-chat-container">
        <button id="chat-button" onclick="toggleChat()">💬</button>
        <div id="chat-window">
            <div class="chat-header">
                <div class="chat-header-title">
                    <span>💬</span>
                    <span>Chat avec Adrien</span>
                </div>
                <span class="chat-close" onclick="toggleChat()">✕</span>
            </div>
            <div class="chat-body" id="chatBody">
                <div class="message bot-message">
                    Bonjour ! Je suis Adrien. N'hésitez pas à me poser des questions sur mon profil ou mes motivations !
                </div>
                <div class="suggestions">
                    <div class="suggestion-chip" onclick="sendSuggestion(this)">Pourquoi le BUT SD ?</div>
                    <div class="suggestion-chip" onclick="sendSuggestion(this)">Ton parcours ?</div>
                    <div class="suggestion-chip" onclick="sendSuggestion(this)">Tes motivations ?</div>
                </div>
            </div>
            <div class="chat-input-container">
                <input type="text" class="chat-input" placeholder="Posez votre question..."
                    onkeypress="handleKeyPress(event)">
            </div>
        </div>
    </div>

    <script>
    function toggleChat() {
        const chatWindow = document.getElementById('chat-window');
        chatWindow.classList.toggle('open');
    }

    function appendMessage(message, isUser = false) {
        const chatBody = document.getElementById('chatBody');
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${isUser ? 'user-message' : 'bot-message'}`;
        messageDiv.textContent = message;
        chatBody.appendChild(messageDiv);
        chatBody.scrollTop = chatBody.scrollHeight;
    }

    function handleKeyPress(event) {
        if (event.key === 'Enter') {
            const input = event.target;
            const message = input.value.trim();
            if (message) {
                sendMessage(message);
                input.value = '';
            }
        }
    }

    function sendSuggestion(element) {
        sendMessage(element.textContent);
    }

    async function sendMessage(message) {
        appendMessage(message, true);
        
        try {
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({message: message})
            });
            
            const data = await response.json();
            appendMessage(data.response);
        } catch (error) {
            console.error('Error:', error);
            appendMessage('Désolé, une erreur est survenue. Veuillez réessayer.');
        }
    }
    </script>
    """, unsafe_allow_html=True)

def handle_chat_input():
    # Système de prompt pour GPT
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

    # Endpoint pour recevoir les messages du chat
    if st.request_method == "POST":
        data = st.request_json()
        user_message = data["message"]

        # Appel à l'API GPT
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

def add_floating_chat_to_app():
    init_floating_chat()
    handle_chat_input()