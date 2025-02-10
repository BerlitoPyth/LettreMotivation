import streamlit as st
import streamlit.components.v1 as components

def display_presentation():
    st.write("Chargement de la présentation...")
    
    # Ajout de debug
    st.write("Debug: Début du chargement du composant HTML")
    
    presentation_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <script src="https://unpkg.com/react@17/umd/react.production.min.js"></script>
        <script src="https://unpkg.com/react-dom@17/umd/react-dom.production.min.js"></script>
        <script src="https://unpkg.com/babel-standalone@6/babel.min.js"></script>
        <style>
            body {
                margin: 0;
                padding: 0;
                font-family: system-ui, -apple-system, sans-serif;
                background-color: #0e1117;
                color: white;
            }

            .container {
                max-width: 900px;
                margin: 0 auto;
                padding: 1rem;
            }

            .section {
                background-color: #1E1F25;
                border-radius: 12px;
                padding: 1.5rem;
                margin-bottom: 1.5rem;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
            }

            .section:hover {
                transform: translateY(-2px);
                box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
            }

            .section-header {
                display: flex;
                align-items: center;
                gap: 0.75rem;
                margin-bottom: 1.25rem;
                padding-bottom: 0.75rem;
                border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            }

            .section-title {
                font-size: 1.25rem;
                font-weight: 600;
                color: #E2E8F0;
                margin: 0;
            }

            .list-container {
                padding-left: 1rem;
            }

            .list-item {
                display: flex;
                align-items: center;
                gap: 0.5rem;
                padding: 0.5rem 0;
                color: #CBD5E1;
                transition: transform 0.15s ease-in-out;
            }

            .list-item:hover {
                transform: translateX(4px);
                color: #F8FAFC;
            }

            .list-item::before {
                content: "•";
                color: #60A5FA;
                font-size: 1.2em;
            }

            .icon {
                width: 1.5rem;
                height: 1.5rem;
                color: currentColor;
                opacity: 0.9;
            }

            .badge {
                background-color: rgba(96, 165, 250, 0.1);
                color: #60A5FA;
                padding: 0.25rem 0.75rem;
                border-radius: 9999px;
                font-size: 0.875rem;
                margin-left: auto;
            }

            .title-gradient {
                background: linear-gradient(135deg, #60A5FA, #818CF8);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-size: 1.75rem;
                font-weight: 700;
                margin-bottom: 2rem;
            }
            
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(10px); }
                to { opacity: 1; transform: translateY(0); }
            }

            .animate-fade-in {
                animation: fadeIn 0.5s ease-out forwards;
            }
        </style>
    </head>
    <body>
        <div id="presentation-root"></div>
        <script type="text/babel">
            // Icônes SVG...
            const User = () => (
                <svg className="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                    <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" />
                    <circle cx="12" cy="7" r="4" />
                </svg>
            );

            const Book = () => (
                <svg className="icon text-purple-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                    <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20" />
                    <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z" />
                </svg>
            );
            
            const Briefcase = () => (
                <svg className="icon text-green-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                    <rect x="2" y="7" width="20" height="14" rx="2" ry="2" />
                    <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16" />
                </svg>
            );
            
            const Code = () => (
                <svg className="icon text-blue-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                    <polyline points="16 18 22 12 16 6" />
                    <polyline points="8 6 2 12 8 18" />
                </svg>
            );
            
            const Brain = () => (
                <svg className="icon text-yellow-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                    <path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96.44 2.5 2.5 0 0 1-2.04-.2 2.5 2.5 0 0 1 1-4.74 2.5 2.5 0 0 1 1.5-4.5Z" />
                    <path d="M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96.44 2.5 2.5 0 0 0 2.04-.2 2.5 2.5 0 0 0-1-4.74 2.5 2.5 0 0 0-1.5-4.5 2.5 2.5 0 0 0-1.5-4.5Z" />
                </svg>
            );
            
            const Heart = () => (
                <svg className="icon text-red-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                    <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" />
                </svg>
            );

            const Section = ({ icon: Icon, title, items, badge }) => (
                <div className="section animate-fade-in" style={{ animationDelay: \`\${Math.random() * 0.5}s\` }}>
                    <div className="section-header">
                        <Icon />
                        <h3 className="section-title">{title}</h3>
                        {badge && <span className="badge">{badge}</span>}
                    </div>
                    <div className="list-container">
                        {items.map((item, index) => (
                            <div key={index} className="list-item">{item}</div>
                        ))}
                    </div>
                </div>
            );

            const Presentation = () => {
                const sections = [
                    {
                        icon: Book,
                        title: "Formation en cours",
                        items: [
                            "DAEU B - Équivalent Bac Scientifique",
                            "Spécialisation en Mathématiques",
                            "Excellent niveau académique"
                        ],
                        badge: "En cours"
                    },
                    {
                        icon: Briefcase,
                        title: "Expérience Professionnelle",
                        items: [
                            "Ex-Plongeur Scaphandrier en Travaux Publics",
                            "Gestion de projets techniques complexes",
                            "Travail en équipe dans des conditions exigeantes"
                        ]
                    },
                    {
                        icon: Code,
                        title: "Compétences Techniques",
                        items: [
                            "Formation à l'École 42 - Introduction à la programmation",
                            "Certifications Python - Apprentissage autodidacte",
                            "Bases solides en algorithmique"
                        ]
                    },
                    {
                        icon: Brain,
                        title: "Points Forts",
                        items: [
                            "Capacité d'adaptation exceptionnelle",
                            "Résolution méthodique des problèmes",
                            "Rigueur et précision dans le travail"
                        ]
                    },
                    {
                        icon: Heart,
                        title: "Centres d'Intérêt",
                        items: [
                            "Passionné par les mathématiques et l'informatique",
                            "Veille technologique constante",
                            "Entrepreneur en herbe dans le gaming"
                        ]
                    }
                ];

                return (
                    <div className="container">
                        <h1 className="title-gradient">À propos de moi</h1>
                        {sections.map((section, index) => (
                            <Section key={index} {...section} />
                        ))}
                    </div>
                );
            };

            ReactDOM.render(<Presentation />, document.getElementById('presentation-root'));
        </script>
    </body>
    </html>
    """
    
    try:
        # Modification des paramètres du composant
        components.html(
            presentation_html,
            height=800,  # Augmenté pour s'assurer que tout est visible
            scrolling=False,  # Désactivé pour éviter les problèmes de scroll
            width=None  # Permet l'adaptation à la largeur
        )
        st.write("Debug: Composant HTML chargé avec succès")
    except Exception as e:
        st.error(f"Erreur lors du chargement: {str(e)}")
        # Affichage plus détaillé de l'erreur
        st.exception(e)