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
                font-family: system-ui, -apple-system, sans-serif;
                margin: 0;
                padding: 20px;
                background: #0f172a;
            }
            .quiz-container {
                max-width: 800px;
                margin: 0 auto;
                color: white;
            }
            .card {
                background: #1e293b;
                border-radius: 8px;
                padding: 20px;
                margin-bottom: 20px;
            }
            .title {
                color: white;
                font-size: 1.5rem;
                font-weight: 600;
                margin-bottom: 1rem;
            }
            .progress-container {
                display: flex;
                align-items: center;
                gap: 1rem;
                margin-bottom: 1rem;
            }
            .progress-bar {
                flex-grow: 1;
                height: 4px;
                background: #334155;
                border-radius: 9999px;
            }
            .progress-fill {
                height: 100%;
                background: #3b82f6;
                border-radius: 9999px;
                transition: width 0.3s ease;
            }
            .button {
                width: 100%;
                padding: 1rem;
                margin: 0.5rem 0;
                background: #334155;
                color: white;
                border: 1px solid #475569;
                border-radius: 6px;
                text-align: left;
                cursor: pointer;
                font-size: 1rem;
                transition: background 0.2s;
            }
            .button:hover {
                background: #475569;
            }
            .result-section {
                padding: 1rem;
                background: #1e293b;
                border-radius: 8px;
                margin-bottom: 1rem;
            }
            .section-title {
                color: white;
                font-size: 1.2rem;
                font-weight: 600;
                margin-bottom: 0.5rem;
            }
            .section-content {
                color: #e2e8f0;
                line-height: 1.5;
            }
        </style>
    </head>
    <body>
        <div id="quiz-root"></div>
        <script type="text/babel">
            const Quiz = () => {
                const [currentStep, setCurrentStep] = React.useState(0);
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
                                match: "J'allie une solide base en mathématiques (DAEU B) à une expérience pratique en programmation, tout en ayant développé des compétences techniques précieuses lors de mon expérience de plongeur scaphandrier."
                            }
                        ]
                    },
                    // ... (autres questions)
                ];

                const handleAnswer = () => {
                    if (currentStep < questions.length - 1) {
                        setCurrentStep(currentStep + 1);
                    } else {
                        setShowResults(true);
                    }
                };

                if (showResults) {
                    return (
                        <div className="quiz-container">
                            <div className="card">
                                <h2 className="title">Mon Profil - Candidat Idéal</h2>
                                <div className="result-section">
                                    <h3 className="section-title">Passion & Détermination</h3>
                                    <p className="section-content">
                                        Passionné par les mathématiques et l'informatique depuis l'enfance, j'ai constamment cherché à développer mes compétences dans ces domaines.
                                    </p>
                                </div>
                                <div className="result-section">
                                    <h3 className="section-title">Adaptabilité & Résilience</h3>
                                    <p className="section-content">
                                        Mon parcours de plongeur scaphandrier à étudiant en DAEU B démontre ma capacité à m'adapter et à exceller dans des environnements exigeants.
                                    </p>
                                </div>
                                {/* ... autres sections ... */}
                            </div>
                        </div>
                    );
                }

                return (
                    <div className="quiz-container">
                        <div className="card">
                            <h2 className="title">Découvrez mon Profil</h2>
                            <div className="progress-container">
                                <span>Question {currentStep + 1}/{questions.length}</span>
                                <div className="progress-bar">
                                    <div 
                                        className="progress-fill"
                                        style={{ width: `${((currentStep + 1) / questions.length) * 100}%` }}
                                    />
                                </div>
                            </div>
                            <h3 className="section-title">{questions[currentStep].title}</h3>
                            <p className="section-content">{questions[currentStep].question}</p>
                            <div>
                                {questions[currentStep].options.map((option, index) => (
                                    <button
                                        key={index}
                                        className="button"
                                        onClick={handleAnswer}
                                    >
                                        {option.text}
                                    </button>
                                ))}
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
    
    components.html(quiz_html, height=600, scrolling=True)
