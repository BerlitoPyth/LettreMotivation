def get_matrix_styles():
    return """
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
    """
