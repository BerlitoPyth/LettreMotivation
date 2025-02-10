import streamlit as st
import streamlit.components.v1 as components

def display_quiz():
    # HTML pour le quiz avec React
    quiz_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <script src="https://unpkg.com/react@17/umd/react.production.min.js"></script>
        <script src="https://unpkg.com/react-dom@17/umd/react-dom.production.min.js"></script>
        <script src="https://unpkg.com/babel-standalone@6/babel.min.js"></script>
        <script src="https://unpkg.com/lucide-react@latest/dist/umd/lucide-react.js"></script>
        <style>
            .quiz-container {
                max-width: 800px;
                margin: 0 auto;
                color: white;
            }
            .card {
                background-color: #0f172a;
                border-radius: 8px;
                padding: 20px;
                margin-bottom: 20px;
            }
            .card-header {
                margin-bottom: 1rem;
            }
            .card-title {
                color: white;
                font-size: 1.25rem;
                font-weight: 600;
                display: flex;
                align-items: center;
                gap: 0.5rem;
            }
            .progress-bar {
                width: 100%;
                height: 4px;
                background: #1e293b;
                border-radius: 9999px;
                margin: 1rem 0;
            }
            .progress-fill {
                height: 100%;
                background: #3b82f6;
                border-radius: 9999px;
                transition: width 0.3s ease;
            }
            .question-container {
                background: #1e293b;
                padding: 1.5rem;
                border-radius: 8px;
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
                display: flex;
                align-items: center;
                transition: background 0.3s;
            }
            .button:hover {
                background: #475569;
            }
            .result-section {
                display: flex;
                gap: 0.75rem;
                margin-bottom: 1.5rem;
            }
            .icon {
                flex-shrink: 0;
                margin-top: 0.25rem;
            }
        </style>
    </head>
    <body>
        <div id="quiz-root"></div>
        <script type="text/babel">
        import React, { useState } from 'react';
        import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
        import { Button } from '@/components/ui/button';
        import { ChevronRight, Star, Brain, Heart, Target, Book, Code, Trophy, Lightbulb } from 'lucide-react';
        
        const ProfileQuiz = () => {
          const [currentStep, setCurrentStep] = useState(0);
          const [score, setScore] = useState(0);
          const [showResults, setShowResults] = useState(false);
        
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
                  match: "Mon parcours atypique démontre ma capacité d'adaptation : d'une carrière technique exigeante en plongée, j'ai su me reconvertir avec succès vers les mathématiques et l'informatique."
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
                  match: "Le BUT Science des Données représente pour moi l'opportunité parfaite de transformer ma passion en carrière, en m'appuyant sur mes compétences techniques et analytiques déjà acquises."
                }
              ]
            }
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
            <Card className="w-full bg-slate-900">
              <CardHeader className="pb-2">
                <CardTitle className="text-xl flex items-center gap-2 text-white">
                  <Star className="w-6 h-6 text-yellow-400" />
                  Mon Profil - Candidat Idéal
                </CardTitle>
              </CardHeader>
              <CardContent className="space-y-6">
                <div className="p-6 bg-slate-800 rounded-lg space-y-6">
                  <div className="flex items-start gap-3">
                    <Heart className="w-6 h-6 text-red-400 mt-1 flex-shrink-0" />
                    <div className="space-y-1">
                      <h4 className="font-semibold text-white">Passion & Détermination</h4>
                      <p className="text-slate-200 text-sm leading-relaxed">Passionné par les mathématiques et l'informatique depuis l'enfance, j'ai constamment cherché à développer mes compétences dans ces domaines.</p>
                    </div>
                  </div>
        
                  <div className="flex items-start gap-3">
                    <Brain className="w-6 h-6 text-purple-400 mt-1 flex-shrink-0" />
                    <div className="space-y-1">
                      <h4 className="font-semibold text-white">Adaptabilité & Résilience</h4>
                      <p className="text-slate-200 text-sm leading-relaxed">Mon parcours de plongeur scaphandrier à étudiant en DAEU B démontre ma capacité à m'adapter et à exceller dans des environnements exigeants.</p>
                    </div>
                  </div>
        
                  <div className="flex items-start gap-3">
                    <Code className="w-6 h-6 text-blue-400 mt-1 flex-shrink-0" />
                    <div className="space-y-1">
                      <h4 className="font-semibold text-white">Compétences Techniques</h4>
                      <p className="text-slate-200 text-sm leading-relaxed">Formation à l'École 42, excellents résultats en mathématiques, expérience en résolution de problèmes complexes.</p>
                    </div>
                  </div>
        
                  <div className="flex items-start gap-3">
                    <Trophy className="w-6 h-6 text-green-400 mt-1 flex-shrink-0" />
                    <div className="space-y-1">
                      <h4 className="font-semibold text-white">Réussite Académique</h4>
                      <p className="text-slate-200 text-sm leading-relaxed">Excellent niveau en DAEU B, particulièrement en mathématiques, démontrant ma capacité à exceller dans un cadre académique.</p>
                    </div>
                  </div>
        
                  <div className="flex items-start gap-3">
                    <Lightbulb className="w-6 h-6 text-yellow-400 mt-1 flex-shrink-0" />
                    <div className="space-y-1">
                      <h4 className="font-semibold text-white">Vision & Projet</h4>
                      <p className="text-slate-200 text-sm leading-relaxed">Le BUT Science des Données à l'IUT de Paris - Rives de Seine représente l'alliance parfaite entre ma passion et mes aspirations professionnelles.</p>
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>
          );
        
          if (showResults) {
            return <MatchProfile />;
          }
        
          return (
            <Card className="w-full bg-slate-900">
              <CardHeader>
                <CardTitle className="text-xl text-white">Découvrez mon Profil</CardTitle>
              </CardHeader>
              <CardContent>
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
                        <Button
                          key={index}
                          variant="outline"
                          className="w-full justify-start text-left h-auto p-4 bg-slate-700 hover:bg-slate-600 text-white border-slate-600"
                          onClick={() => handleAnswer(option.points)}
                        >
                          <ChevronRight className="w-4 h-4 mr-2 flex-shrink-0" />
                          <span>{option.text}</span>
                        </Button>
                      ))}
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>
          );
        };
        
        export default ProfileQuiz;
            
            ReactDOM.render(<ProfileQuiz />, document.getElementById('quiz-root'));
        </script>
    </body>
    </html>
    """
    
    # Afficher le composant dans Streamlit
    components.html(quiz_html, height=800, scrolling=True)