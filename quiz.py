import streamlit as st
import streamlit.components.v1 as components

def display_quiz():
    quiz_html = """
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
        padding: 20px;
        font-family: system-ui, -apple-system, sans-serif;
        background-color: #0f172a;
        color: white;
    }
    
    /* Classes utilitaires */
    .w-full {
        width: 100%;
    }
    
    /* Couleurs de fond */
    .bg-slate-900 {
        background-color: #0f172a;
    }
    .bg-slate-800 {
        background-color: #1e293b;
    }
    .bg-slate-700 {
        background-color: #334155;
    }
    .bg-slate-600 {
        background-color: #475569;
    }
    .bg-blue-500 {
        background-color: #3b82f6;
    }
    
    /* Couleurs de texte */
    .text-white {
        color: white;
    }
    .text-slate-300 {
        color: #cbd5e1;
    }
    .text-slate-200 {
        color: #e2e8f0;
    }
    .text-red-400 {
        color: #f87171;
    }
    .text-purple-400 {
        color: #c084fc;
    }
    .text-blue-400 {
        color: #60a5fa;
    }
    .text-green-400 {
        color: #4ade80;
    }
    .text-yellow-400 {
        color: #facc15;
    }
    
    /* Tailles de texte */
    .text-sm {
        font-size: 0.875rem;
        line-height: 1.25rem;
    }
    .text-lg {
        font-size: 1.125rem;
        line-height: 1.75rem;
    }
    .text-xl {
        font-size: 1.25rem;
        line-height: 1.75rem;
    }
    
    /* Styles de texte */
    .font-semibold {
        font-weight: 600;
    }
    .leading-relaxed {
        line-height: 1.625;
    }
    
    /* Espacement */
    .p-6 {
        padding: 1.5rem;
    }
    .p-4 {
        padding: 1rem;
    }
    .pb-2 {
        padding-bottom: 0.5rem;
    }
    .mb-6 {
        margin-bottom: 1.5rem;
    }
    .mb-3 {
        margin-bottom: 0.75rem;
    }
    .mt-1 {
        margin-top: 0.25rem;
    }
    
    /* Flex */
    .flex {
        display: flex;
    }
    .flex-1 {
        flex: 1 1 0%;
    }
    .flex-shrink-0 {
        flex-shrink: 0;
    }
    .items-center {
        align-items: center;
    }
    .items-start {
        align-items: flex-start;
    }
    .gap-2 {
        gap: 0.5rem;
    }
    .gap-3 {
        gap: 0.75rem;
    }
    
    /* Espacement vertical */
    .space-y-6 > * + * {
        margin-top: 1.5rem;
    }
    .space-y-3 > * + * {
        margin-top: 0.75rem;
    }
    .space-y-1 > * + * {
        margin-top: 0.25rem;
    }
    
    /* Bordures et coins arrondis */
    .rounded-lg {
        border-radius: 0.5rem;
    }
    .rounded-full {
        border-radius: 9999px;
    }
    
    /* Hauteurs */
    .h-1 {
        height: 0.25rem;
    }
    .h-auto {
        height: auto;
    }
    
    /* Transitions */
    .transition-all {
        transition-property: all;
        transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
        transition-duration: 150ms;
    }
    
    /* Composants spécifiques */
    .card {
        border-radius: 0.5rem;
        padding: 1.5rem;
    }
    
    .card-header {
        margin-bottom: 1rem;
    }
    
    .button {
        width: 100%;
        padding: 1rem;
        background-color: #334155;
        color: white;
        border: 1px solid #475569;
        border-radius: 0.5rem;
        display: flex;
        align-items: center;
        cursor: pointer;
        transition: background-color 0.2s;
        font-size: 1rem;
        text-align: left;
    }
    
    .button:hover {
        background-color: #475569;
    }
    
    /* Icônes */
    .icon {
        width: 1.5rem;
        height: 1.5rem;
        flex-shrink: 0;
    }
    
    .chevron-icon {
        width: 1rem;
        height: 1rem;
        margin-right: 0.5rem;
        flex-shrink: 0;
    }
    
    /* Barre de progression */
    .progress-bar {
        width: 100%;
        height: 0.25rem;
        background-color: #334155;
        border-radius: 9999px;
        overflow: hidden;
    }
    
    .progress-fill {
        height: 100%;
        background-color: #3b82f6;
        border-radius: 9999px;
        transition: width 0.3s ease;
    }
</style>
    </head>
    <body>
        <div id="quiz-root"></div>
        <script type="text/babel">
            // Composants d'icônes
            const Star = () => (
                <svg className="icon text-yellow-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                    <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>
                </svg>
            );

            const Heart = () => (
                <svg className="icon text-red-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                    <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>
                </svg>
            );

            const Brain = () => (
                <svg className="icon text-purple-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                    <path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96.44 2.5 2.5 0 0 1-2.04-.2 2.5 2.5 0 0 1 1-4.74 2.5 2.5 0 0 1 1.5-4.5 2.5 2.5 0 0 1 1.5-4.5Z"/>
                    <path d="M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96.44 2.5 2.5 0 0 0 2.04-.2 2.5 2.5 0 0 0-1-4.74 2.5 2.5 0 0 0-1.5-4.5 2.5 2.5 0 0 0-1.5-4.5Z"/>
                </svg>
            );

            const Code = () => (
                <svg className="icon text-blue-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                    <polyline points="16 18 22 12 16 6"/>
                    <polyline points="8 6 2 12 8 18"/>
                </svg>
            );

            const Trophy = () => (
                <svg className="icon text-green-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                    <path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"/>
                    <path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"/>
                    <path d="M4 22h16"/>
                    <path d="M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22"/>
                    <path d="M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22"/>
                    <path d="M18 2H6v7a6 6 0 0 0 12 0V2Z"/>
                </svg>
            );

            const Lightbulb = () => (
                <svg className="icon text-yellow-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                    <path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/>
                    <path d="M9 18h6"/>
                    <path d="M10 22h4"/>
                </svg>
            );

            const ChevronRight = () => (
                <svg className="chevron-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                    <polyline points="9 18 15 12 9 6"/>
                </svg>
            );

            const Quiz = () => {
                const [currentStep, setCurrentStep] = React.useState(0);
                const [score, setScore] = React.useState(0);
                const [showResults, setShowResults] = React.useState(false);

                const questions = [
                    {
      title: "La Motivation",
      question: "Quel type de candidat recherchez-vous pour votre formation ?",
      options: [
        {
          text: "Une personne qui suit le mouvement général vers la data science",
          points: 0
        },
        {
          text: "Un passionné ayant déjà exploré le domaine par lui-même",
          points: 1,
          match: "Ma passion pour le domaine m'a poussé à m'auto-former en programmation via l'École 42 et à choisir l'option mathématiques en DAEU B."
        }
      ]
    },
    {
      title: "L'Expérience Technique",
      question: "Quelle expérience préalable valorisez-vous le plus ?",
      options: [
        {
          text: "Des connaissances théoriques uniquement",
          points: 0
        },
        {
          text: "Une combinaison d'expérience pratique et de fondements théoriques",
          points: 1,
          match: "J'allie une solide base en mathématiques (DAEU B) à une expérience pratique en programmation, tout en ayant développé des compétences techniques précieuses lors de mon expéri[...]
        }
      ]
    },
    {
      title: "La Capacité d'Apprentissage",
      question: "Comment évaluez-vous le potentiel d'un candidat ?",
      options: [
        {
          text: "Par ses diplômes traditionnels",
          points: 0
        },
        {
          text: "Par sa capacité à apprendre et à se réinventer",
          points: 1,
          match: "Mon parcours atypique démontre ma capacité d'adaptation : d'une carrière technique exigeante en plongée, j'ai su me reconvertir avec succès vers les mathématiques et l'informat[...]
        }
      ]
    },
    {
      title: "L'Engagement",
      question: "Que recherchez-vous en termes d'implication ?",
      options: [
        {
          text: "Une approche standard des études",
          points: 0
        },
        {
          text: "Un investissement personnel fort et une vraie passion",
          points: 1,
          match: "Mon engagement se reflète dans mes excellents résultats en DAEU B et dans ma démarche d'autoformation continue en programmation."
        }
      ]
    },
    {
      title: "La Vision Long Terme",
      question: "Quelle vision du BUT Science des Données privilégiez-vous ?",
      options: [
        {
          text: "Un simple tremplin vers l'emploi",
          points: 0
        },
        {
          text: "Une étape réfléchie dans un projet professionnel construit",
          points: 1,
          match: "Le BUT Science des Données représente pour moi l'opportunité parfaite de transformer ma passion en carrière, en m'appuyant sur mes compétences techniques et analytiques déjà a[...]
        }
      ]
    }
  ];
                ];

                const handleAnswer = (points) => {
                    setScore(score + points);
                    if (currentStep < questions.length - 1) {
                        setCurrentStep(currentStep + 1);
                    } else {
                        setShowResults(true);
                    }
                };

                const MatchProfile = () => (
    <div className="w-full bg-slate-900 card">
        <div className="card-header">
            <h2 className="text-xl flex items-center gap-2 text-white">
                <Star />
                Mon Profil - Candidat Idéal
            </h2>
        </div>
        <div className="space-y-6">
            <div className="p-6 bg-slate-800 rounded-lg space-y-6">
                <div className="flex items-start gap-3">
                    <Heart />
                    <div className="space-y-1">
                        <h4 className="font-semibold text-white">Passion & Détermination</h4>
                        <p className="text-slate-200 text-sm leading-relaxed">
                            Passionné par les mathématiques et l'informatique depuis l'enfance, j'ai constamment cherché à développer mes compétences dans ces domaines.
                        </p>
                    </div>
                </div>

                <div className="flex items-start gap-3">
                    <Brain />
                    <div className="space-y-1">
                        <h4 className="font-semibold text-white">Adaptabilité & Résilience</h4>
                        <p className="text-slate-200 text-sm leading-relaxed">
                            Mon parcours de plongeur scaphandrier à étudiant en DAEU B démontre ma capacité à m'adapter et à exceller dans des environnements exigeants.
                        </p>
                    </div>
                </div>

                <div className="flex items-start gap-3">
                    <Code />
                    <div className="space-y-1">
                        <h4 className="font-semibold text-white">Compétences Techniques</h4>
                        <p className="text-slate-200 text-sm leading-relaxed">
                            Formation à l'École 42, excellents résultats en mathématiques, expérience en résolution de problèmes complexes.
                        </p>
                    </div>
                </div>

                <div className="flex items-start gap-3">
                    <Trophy />
                    <div className="space-y-1">
                        <h4 className="font-semibold text-white">Réussite Académique</h4>
                        <p className="text-slate-200 text-sm leading-relaxed">
                            Excellent niveau en DAEU B, particulièrement en mathématiques, démontrant ma capacité à exceller dans un cadre académique.
                        </p>
                    </div>
                </div>

                <div className="flex items-start gap-3">
                    <Lightbulb />
                    <div className="space-y-1">
                        <h4 className="font-semibold text-white">Vision & Projet</h4>
                        <p className="text-slate-200 text-sm leading-relaxed">
                            Le BUT Science des Données à l'IUT de Paris - Rives de Seine représente l'alliance parfaite entre ma passion et mes aspirations professionnelles.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
);

                if (showResults) {
                    return <MatchProfile />;
                }

                return (return (
                    <div className="w-full bg-slate-900 card">
                        <div className="card-header">
                            <h2 className="text-xl text-white">Découvrez mon Profil</h2>
                        </div>
                        <div className="space-y-6">
                            <div className="flex items-center gap-2 text-sm text-slate-300">
                                <span>Question {currentStep + 1}/{questions.length}</span>
                                <div className="flex-1 h-1 bg-slate-700 rounded-full">
                                    <div 
                                        className="h-1 bg-blue-500 rounded-full transition-all"
                                        style={{ width: `${((currentStep + 1) / questions.length) * 100}%` }}
                                    />
                                </div>
                            </div>

                            <div className="p-6 bg-slate-800 rounded-lg">
                                <h3 className="text-lg font-semibold mb-3 text-white">{questions[currentStep].title}</h3>
                                <p className="text-slate-200 mb-6">{questions[currentStep].question}</p>
                                
                                <div className="space-y-3">
                                    {questions[currentStep].options.map((option, index) => (
                                        <button
                                            key={index}
                                            className="button"
                                            onClick={() => handleAnswer(option.points)}
                                        >
                                            <ChevronRight />
                                            <span>{option.text}</span>
                                        </button>
                                    ))}
                                </div>
                            </div>
                        </div>
                    </div>
                );
            };

            ReactDOM.render(<Quiz />, document.getElementById('quiz-root'));
        </script>
    </body>
    </html>
    """
    
    components.html(quiz_html, height=800, scrolling=True)
