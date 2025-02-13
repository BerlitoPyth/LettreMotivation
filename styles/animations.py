def get_matrix_styles():
    return """
    <style>
    @keyframes matrix-rain {
        0% { transform: translateY(-100%); }
        100% { transform: translateY(100%); }
    }
    
    .matrix-animation {
        font-family: 'Courier New', monospace;
        background-color: rgba(0, 0, 0, 0.95);
        color: #0f0;
        position: fixed;
        /* ...rest of matrix styles... */
    }
    </style>
    """
