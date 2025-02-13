def get_main_styles():
    return """
    <style>
    /* Base styles */
    .main { padding: 2rem; }
    .stApp { margin-top: 0.5rem !important; }
    
    /* Titles */
    h1 {
        margin-top: 2rem !important;
        scroll-margin-top: 80px;
    }
    
    h2 {
        margin: 1rem 0 !important;
        padding: 0 !important;
    }
    
    /* Sidebar adjustments */
    .sidebar .block-container { padding-top: 0.5rem !important; }
    .stHeading { margin-top: -0.5rem !important; }
    .stRadio { margin-top: 0 !important; }
    
    /* Components */
    .stButton > button { width: 100%; }
    .stImage {
        transition: transform 0.3s ease;
    }
    .stImage:hover {
        transform: scale(1.02);
        cursor: pointer;
    }
    
    /* Utilities */
    .section-title {
        margin-top: 2rem !important;
        opacity: 0;
        transition: opacity 0.5s;
    }
    </style>
    """
