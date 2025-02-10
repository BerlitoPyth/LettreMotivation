import streamlit as st
import streamlit.components.v1 as components

def display_presentation():
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
                padding: 16px;  /* Réduit de 20px à 16px pour plus de cohérence */
                font-family: system-ui, -apple-system, sans-serif;
                background-color: #0F1116;
                color: white;
            }
            
            .max-w-4xl {
                max-width: 48rem;  /* Réduit de 56rem à 48rem pour une meilleure lisibilité */
            }
            
            .mx-auto {
                margin-left: auto;
                margin-right: auto;
            }
            
            .bg-slate-800 {
                background-color: #1E293B;  /* Légèrement plus foncé pour un meilleur contraste */
            }
            
            .border-none {
                border: none;
            }
            
            .shadow-lg {
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2), 
                            0 2px 4px -1px rgba(0, 0, 0, 0.1);  /* Ombre plus subtile */
            }
            
            .p-6 {
                padding: 1.25rem;  /* Ajusté pour plus de compacité */
            }
            
            .mb-6 {
                margin-bottom: 1.5rem;
            }
            
            .flex {
                display: flex;
            }
            
            .items-center {
                align-items: center;
            }
            
            .items-start {
                align-items: flex-start;
            }
            
            .gap-3 {
                gap: 0.75rem;
            }
            
            .space-y-6 > * + * {
                margin-top: 1.5rem;
            }
            
            .space-y-2 > * + * {
                margin-top: 0.5rem;
            }
            
            .mt-1 {
                margin-top: 0.25rem;
            }
            
            .mt-2 {
                margin-top: 0.5rem;
            }
            
            .text-xl {
                font-size: 1.25rem;
                line-height: 1.75rem;
            }
            
            .font-bold {
                font-weight: 700;
            }
            
            .font-semibold {
                font-weight: 600;
            }
            
            .text-white {
                color: white;
            }
            
            .text-slate-300 {
                color: #E2E8F0;  /* Plus clair pour une meilleure lisibilité */
            }
            
            .text-blue-400 {
                color: #60a5fa;
            }
            
            .text-purple-400 {
                color: #c084fc;
            }
            
            .text-green-400 {
                color: #4ade80;
            }
            
            .text-yellow-400 {
                color: #facc15;
            }
            
            .text-red-400 {
                color: #f87171;
            }

            .icon {
                width: 1.5rem;  /* Légèrement plus grand */
                height: 1.5rem;
                opacity: 0.9;  /* Légère transparence pour plus de douceur */
            }
            
            ul {
                list-style: none;
                padding: 0;
                margin: 0;
            }

            ul li {
                position: relative;
                padding-left: 1rem;
                line-height: 1.6;  /* Meilleur espacement des lignes */
            }

            ul li:before {
                content: "•";
                position: absolute;
                left: 0;
                color: #60A5FA;  /* Bleu pour les puces */
            }

            .card {
                border-radius: 0.75rem;
                transition: transform 0.2s ease-in-out;
            }

            .card:hover {
                transform: translateY(-2px);
            }
        </style>
    </head>
    <body>
        <div id="presentation-root"></div>
        <script type="text/babel">
            const User = () => (
                <svg className="icon text-blue-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
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
                    <path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96.44 2.5 2.5 0 0 1-2.04-.2 2.5 2.5 0 0 1 1-4.74 2.5 2.5 0 0 1 1.5-4.5 2.5 2.5 0 0 1 1.5-4.5Z" />
                    <path d="M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96.44 2.5 2.5 0 0 0 2.04-.2 2.5 2.5 0 0 0-1-4.74 2.5 2.5 0 0 0-1.5-4.5 2.5 2.5 0 0 0-1.5-4.5Z" />
                </svg>
            );
            
            const Heart = () => (
                <svg className="icon text-red-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                    <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" />
                </svg>
            );

            const Presentation = () => {
                return (
                    <div className="max-w-4xl mx-auto">
                        <div className="bg-slate-800 border-none shadow-lg p-6 card">
                            <div className="flex items-center gap-3 mb-6">
                                <User />
                                <h2 className="text-xl font-bold text-white">À propos de moi</h2>
                            </div>
                            
                            <div className="space-y-6">
                                <div className="flex items-start gap-3">
                                    <Book />
                                    <div>
                                        <h3 className="font-semibold text-white">Formation en cours</h3>
                                        <ul className="text-slate-300 space-y-2 mt-2">
                                            <li>• DAEU B - Équivalent Bac Scientifique</li>
                                            <li>• Spécialisation en Mathématiques</li>
                                            <li>• Excellent niveau académique</li>
                                        </ul>
                                    </div>
                                </div>

                                <div className="flex items-start gap-3">
                                    <Briefcase />
                                    <div>
                                        <h3 className="font-semibold text-white">Expérience Professionnelle</h3>
                                        <ul className="text-slate-300 space-y-2 mt-2">
                                            <li>• Ex-Plongeur Scaphandrier en Travaux Publics</li>
                                            <li>• Gestion de projets techniques complexes</li>
                                            <li>• Travail en équipe dans des conditions exigeantes</li>
                                        </ul>
                                    </div>
                                </div>

                                <div className="flex items-start gap-3">
                                    <Code />
                                    <div>
                                        <h3 className="font-semibold text-white">Compétences Techniques</h3>
                                        <ul className="text-slate-300 space-y-2 mt-2">
                                            <li>• Formation à l'École 42 - Introduction à la programmation</li>
                                            <li>• Certifications Python - Apprentissage autodidacte</li>
                                            <li>• Bases solides en algorithmique</li>
                                        </ul>
                                    </div>
                                </div>

                                <div className="flex items-start gap-3">
                                    <Brain />
                                    <div>
                                        <h3 className="font-semibold text-white">Points Forts</h3>
                                        <ul className="text-slate-300 space-y-2 mt-2">
                                            <li>• Capacité d'adaptation exceptionnelle</li>
                                            <li>• Résolution méthodique des problèmes</li>
                                            <li>• Rigueur et précision dans le travail</li>
                                        </ul>
                                    </div>
                                </div>

                                <div className="flex items-start gap-3">
                                    <Heart />
                                    <div>
                                        <h3 className="font-semibold text-white">Centres d'Intérêt</h3>
                                        <ul className="text-slate-300 space-y-2 mt-2">
                                            <li>• Passionné par les mathématiques et l'informatique</li>
                                            <li>• Veille technologique constante</li>
                                            <li>• Entrepreneur en herbe dans le gaming</li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                );
            };

            ReactDOM.render(<Presentation />, document.getElementById('presentation-root'));
        </script>
    </body>
    </html>
    """
    
    # Ajustement de la hauteur du composant
    components.html(presentation_html, height=720, scrolling=True)  # Réduit de 800 à 720 pour plus de compacité