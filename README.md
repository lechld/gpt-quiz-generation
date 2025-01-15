# gpt-quiz-generation
Einführung in die Computerlinguistik (510.600, 24W)

# Vergleich von LLM-generierten Fragen und OTDB-Fragen

## Projektziel

Das Projekt untersucht, wie sich statische Quizfragen aus der Open Trivia Database (OTDB) von dynamisch generierten Fragen eines Large Language Models (LLM) unterscheiden. Der Fokus liegt dabei auf der Qualität, Diver- sität und Themenrelevanz der Fragen.
Durch den systematischen Vergleich soll ermittelt werden, ob LLMs eine sin- nvolle Ergänzung oder Alternative zu bestehenden Quiz-Datenbanken darstellen können.

## Umfang

Datenquellen:
- Open Trivia Database (OTDB): Fragen zu verschiedenen Kategorien werden über eine API abgerufen.
- Large Language Model (LLM): Ein LLM wird genutzt, um Fragen und Antwortmöglichkeiten zu denselben Kategorien zu generieren.

Kategorien:
- Das Projekt betrachtet z. B. die Themen Geschichte, Wissenschaft und Geografie.

Vergleichskriterien:
- Fragequalität: Verständlichkeit und Komplexität der Fragen.
- Diversität: Unterscheidbarkeit der Fragen innerhalb derselben Kategorie. 
- Themenrelevanz: Prüfung, ob die Fragen thematisch passend sind.

Metriken:
- Textstatistiken (z. B. Wortanzahl, Satzlänge).
- Textsimilarität (Vergleich der Fragen mittels Cosine Similarity). 
- Keyword Matching (Prüfung auf thematisch relevante Begriffe).

## Erwartete Ergebnisse

- Ein quantitativer Vergleich der LLM- und OTDB-Fragen hinsichtlich Qualität, Diversität, und Relevanz.
- Eine Einschätzung des Potenzials von LLMs für dynamische Quiz-Systeme im Vergleich zu statischen Datenbanken.