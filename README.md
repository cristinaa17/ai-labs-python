# Laboratoare de Inteligență Artificială 

Repository cu exerciții și aplicații practice realizate în cadrul laboratorului de **Inteligență Artificială**, folosind Python și biblioteci specifice analizei datelor, învățării automate și procesării imaginilor.

Proiectul reunește lucrări practice care ilustrează concepte fundamentale de programare și tehnici de inteligență artificială, de la prelucrarea datelor până la antrenarea modelelor de machine learning și lucrul cu imagini.

## Conținutul repository-ului

### Laboratorul 1 — Fundamente Python
Exerciții introductive de programare în Python și aplicarea conceptelor de bază.

### Laboratorul 2 — Structuri de control și exerciții practice
Exerciții folosind condiții, bucle, liste și alte structuri de programare.

### Laboratorul 3 — Funcții și prelucrarea colecțiilor
Exemple de utilizare a funcțiilor, expresiilor lambda, `map()`, `filter()` și comprehensions.

### Laboratorul 4 — Analiza datelor cu Pandas
Importarea și explorarea unui set de date, filtrarea și sortarea informațiilor și aplicarea operațiilor de analiză a datelor.

### Laboratorul 5 — Clasificare cu K-Nearest Neighbors (KNN)
Explorarea datelor, împărțirea în seturi de antrenare și testare, preprocesarea datelor și construirea unui model de clasificare.

### Laboratorul 6 — Regresie liniară
Explorarea setului de date Diabetes și aplicarea tehnicilor de regresie liniară.

### Laboratorul 7 — Arbori de decizie
Utilizarea setului de date Wine pentru construirea și antrenarea unui model bazat pe arbori de decizie.

### Laboratorul 8 — Rețele neuronale
Construirea și antrenarea unui model neuronal folosind API-ul `Sequential`.

### Laboratorul 9 — Procesarea imaginilor cu OpenCV
Exerciții de încărcare, afișare și analiză a imaginilor, împreună cu resurse pentru experimente de viziune computerizată.

## Tehnologii și biblioteci

- **Python** — limbaj de programare
- **Jupyter Notebook** — dezvoltarea și documentarea experimentelor
- **Pandas** — prelucrarea și analiza datelor
- **Scikit-learn** — algoritmi de machine learning
- **OpenCV** — procesarea imaginilor
- **NumPy** — operații numerice și manipularea datelor
- **TensorFlow/Keras** — construirea modelelor de rețele neuronale, acolo unde este utilizat în laborator

## Rulare

### 1. Clonarea repository-ului

```bash
git clone https://github.com/cristinaa17/ai-labs-python.git
cd ai-labs-python
```

### 2. Crearea unui mediu virtual

```bash
python -m venv .venv
```

Activarea mediului virtual:

**Windows**
```bash
.venv\Scripts\activate
```

**macOS / Linux**
```bash
source .venv/bin/activate
```

### 3. Instalarea bibliotecilor

Instalează bibliotecile necesare exercițiului pe care dorești să îl rulezi. De exemplu:

```bash
pip install numpy pandas matplotlib scikit-learn jupyter opencv-python
```

Pentru notebook-urile care utilizează TensorFlow, instalează separat și `tensorflow`, dacă este compatibil cu versiunea ta de Python.

### 4. Pornirea Jupyter Notebook

```bash
jupyter notebook
```

Deschide notebook-ul dorit și execută celulele în ordine. Fișierele Python pot fi rulate individual, în funcție de exercițiu.

> **Notă:** Unele lucrări folosesc seturi de date sau resurse specifice. Verifică fișierele și importurile fiecărui laborator înainte de rulare.

## Obiective de învățare

- Consolidarea cunoștințelor de programare în Python.
- Explorarea și prelucrarea seturilor de date.
- Înțelegerea etapelor de antrenare și testare a modelelor de machine learning.
- Aplicarea algoritmilor de clasificare și regresie.
- Familiarizarea cu rețelele neuronale.
- Explorarea tehnicilor de procesare a imaginilor.

## Stadiul proiectului

Repository educațional, dezvoltat în cadrul activităților universitare de laborator. Conținutul reflectă exercițiile și experimentele practice realizate pe parcursul studiului.

