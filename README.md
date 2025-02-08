# SocialNetwork (Projet en Python)

## Description
Ce projet a pour but de modéliser et analyser un réseau social à l'aide de structures de graphes. Il inclut plusieurs modules et fonctions permettant d'étudier la structure et la propagation de l'information dans le réseau.

## Fonctionnalités

### 1. Module Outils
Un module permettant de manipuler des structures de files et de piles, facilitant la réutilisation des fonctions dans divers programmes.

### 2. Analyse des graphes
- Calcul du **nombre d'arêtes** pour un graphe non orienté.
- Calcul du **nombre d'arcs** pour un graphe orienté.
- Chargement d'un graphe à partir d'une description textuelle, sous forme de **matrice d'adjacence** ou **liste d'adjacence**.

### 3. Algorithmes de parcours
- **Parcours en profondeur** (à partir d'un sommet donné).
- **Parcours en largeur** (à partir d'un sommet donné).

### 4. Analyse des communautés
- Détection si le réseau est composé d'une seule **communauté**.
- Identification du **top influenceur** (la personne la plus suivie).
- Calcul du **temps de propagation** minimum d'une information entre deux personnes.
- Détermination du **chemin de propagation** minimal d'une information.

### 5. Génération de graphes
- Création aléatoire de graphes avec plusieurs contraintes (orientation, nombre de sommets, degrés, communautés, etc.).

## Structure du Projet
```
SocialNetwork/
│
├── outils/
│   ├── __init__.py
│   ├── file.py
│   ├── pile.py
│   ├── graphe.py
│   ├── parcours.py
│   ├── communaute.py
│   ├── influenceur.py
│   ├── propagation.py
│   └── generation_graphe.py
│
├── tests/
│   ├── test_file.py
│   ├── test_pile.py
│   ├── test_graphe.py
│   ├── test_parcours.py
│   ├── test_communaute.py
│   ├── test_influenceur.py
│   ├── test_propagation.py
│   └── test_generation_graphe.py
│
├── data/
│   └── go-9-01.txt
│
├── main.py
├── run_tests.py
└── requirements.txt
```

## Installation
1. Cloner le dépôt :
   ```bash
   [git clone https://github.com/JinSeeng/SocialNetwork.git]
   ```
2. Accéder au projet.
   
3. Installer les dépendances (Si vous possédez une version antérieure à Python 3.10) :
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation
- Utiliser les fichiers de test pour vérifier le bon fonctionnement des fonctions (séparement).
- Exécuter le fichier ```main.py``` pour tester l'ensemble des fonctionnalités du projet.
