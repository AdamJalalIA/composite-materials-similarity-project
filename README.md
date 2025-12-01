[![Python](https://img.shields.io/badge/python-3.10-blue.svg)](#)
[![Streamlit](https://img.shields.io/badge/streamlit-app-red.svg)](#)
[![Status](https://img.shields.io/badge/status-completed-brightgreen.svg)](#)
[![Type](https://img.shields.io/badge/project-internship-orange.svg)](#)

# Exploration de matériaux composites intelligents | Stage AptiSkills



**Stage L3 Matériaux / Data / Informatique**  
**Durée** : 1 mois  
**Encadré par** : AptiSkills  
**Technologies** : Python • Streamlit • SQLite • FAISS • Scikit-learn

## Objectifs

Concevoir une plateforme bout-en-bout capable de nettoyer les données composites MHK (Sandia National Laboratories), de modéliser la contrainte maximale via un algorithme supervisé, de rechercher des matériaux similaires selon des critères métier (hydrogène, corrosion, contraintes) et d'exposer ces capacités dans une interface Streamlit utilisable en production interne.

## Démonstration

### Interface de recherche de similarité
L'interface principale permet de définir les propriétés d'un matériau de référence pour trouver des matériaux similaires dans la base de données.

![Interface de recherche](docs/01_interface_accueil.png)

### Exploration des matériaux avec filtres
L'onglet d'exploration libre offre des filtres personnalisés et affiche un tableau interactif des matériaux correspondants, accompagné d'une visualisation des performances mécaniques.

![Exploration avec filtres](docs/02_exploration_tableau.png)

### Configuration de la recherche de similarité
Définissez les caractéristiques du matériau recherché (taux de fibre, module élastique, déformation maximale, épaisseur, nombre de cycles).

![Formulaire de recherche](docs/screenshots/03_similarite_formulaire.png)

### Résultats de la recherche FAISS
Les résultats affichent les matériaux les plus similaires avec leurs caractéristiques détaillées et une visualisation de leur positionnement dans l'espace des caractéristiques via FAISS.

![Résultats avec visualisation](docs/04_similarite_resultats.png)


## Résultats

### Base de données

- **74 matériaux composites** nettoyés et structurés
- **2 560 lignes** de données brutes transformées
- **21 types** de matériaux/résines : Adhesive, Epoxy (EP, EP-10, EP-9, EP1, EP3), PA6, PA11, PET, PETG, PP, TP, UA, UP2, UP4, VE, VE2, VE7, HDPE
- **7 propriétés** mécaniques documentées (Vf %, Épaisseur, Max Stress, Module E, Max % Strain, Cycles, Fréquence/Moisture)

### Modèle de prédiction

- **Précision** : 88 % de variance expliquée (R²) sur la contrainte maximale
- **Algorithme** : Pipeline `LinearRegression` (scikit-learn) avec encodage One-Hot
- **Features** : Vf %, Module d'Young (E), Max % Strain, Épaisseur, Cycles, Type de résine

### Recherche de similarité

- **FAISS** : Index vectoriel L2, requêtes <1 s sur 1 279 vecteurs normalisés
- **Critères** : Contraintes mécaniques, fréquence, module E, résistance à l'humidité/corrosion
- Interface permettant de trouver des matériaux alternatifs rapidement

### Impact pour AptiSkills

- Réduction du temps de recherche manuelle : de plusieurs heures à quelques minutes
- Base de données structurée exploitable pour futurs projets
- Outil métier déployable pour ingénieurs matériaux

## Ce que j'ai appris

### Compétences Data Engineering

- **Nettoyage de données complexes** : Extraction et normalisation depuis Excel multi-feuilles hétérogènes (MHK Database)
- **Modélisation relationnelle** : Conception MCD et alimentation automatique des tables Résine/Matériau/Test
- **Optimisation SQL** : Requêtes SQLite performantes pour l'analyse descriptive

### Compétences Machine Learning

- **Régression supervisée** : Prédiction de Max Stress avec pipeline scikit-learn complet
- **Recherche vectorielle** : FAISS pour similarité multidimensionnelle et mise à l'échelle rapide
- **Feature engineering** : Sélection et standardisation des variables physiques clés

### Compétences Produit

- **Interface métier** : Streamlit adapté aux workflows des ingénieurs
- **Communication technique** : Restitutions synthétiques auprès des encadrants AptiSkills
- **Gestion de projet** : Planification d'un sprint d'1 mois avec livrables hebdomadaires

## Installation

### Prérequis

- Python 3.10+
- pip

### Installation rapide

```bash git clone https://github.com/AdamJalalIA/composite-materials-similarity-project
cd composite-materials-similarity-project
pip install -r requirements.txt
```

### Lancement

```bash
streamlit run src/app.py
```

Application accessible sur http://localhost:8501

## Utilisation

### Pour les ingénieurs matériaux>

1. **Explorer** : Naviguez dans la base nettoyée avec filtres (résine, lay-up, performances)
2. **Analyser** : Visualisez les performances mécaniques (contrainte, module E, cycles)
3. **Comparer** : Trouvez des matériaux similaires selon les critères mécaniques via FAISS

**Documentation complète** : Consultez [USAGE.md](USAGE.md) pour le guide détaillé

## Contexte

Les matériaux composites polymères (PA6, PEEK, PPS...) renforcés par fibres (carbone, verre, aramide) sont prometteurs pour des usages variés :
- Réservoirs hydrogène (type IV / V)
- Milieux marins extrêmes (corrosion, humidité, contraintes mécaniques - applications MHK)
- Pièces structurelles allégées

Mais les données expérimentales (Excel multi-feuilles, tableaux complexes…) sont souvent :
- Dispersées et non standardisées
- Difficiles à exploiter directement
- Riches mais sous-utilisées

Le projet a consisté à transformer cette masse d'informations en une base exploitable, interrogeable et visualisable facilement par des ingénieurs ou chercheurs.

**Source des données** : [Sandia National Laboratories - MHK Materials Database](https://energy.sandia.gov/programs/renewable-energy/wind-power/rotor-innovation/rotor-reliability/mhk-materials-database/)

## Architecture du projet

```text
┌───────────────────────────────────────────────┐
│ Données nettoyées (.csv)                      │ ← MHK_material_database_cleaned.csv
└────────────────┬──────────────────────────────┘
                 ↓
┌───────────────────────────────────────────────┐
│ Modélisation relationnelle (MCD)              │
│ Tables : Matériau, Résine, Essai              │
└────────────────┬──────────────────────────────┘
                 ↓
┌───────────────────────────────────────────────┐
│ Stockage et requêtes SQL : SQLite + pandas    │
└────────────────┬──────────────────────────────┘
                 ↓
┌───────────────────────────────────────────────┐
│ Modèle de régression (scikit-learn)           │
│ → Prédiction de Max Stress                    │
└────────────────┬──────────────────────────────┘
                 ↓
┌───────────────────────────────────────────────┐
│ Recherche vectorielle (FAISS)                 │
│ → Matériaux aux propriétés similaires         │
└────────────────┬──────────────────────────────┘
                 ↓
┌───────────────────────────────────────────────┐
│ Interface Streamlit                           │
│ → Exploration, filtres, graphiques            │
└──────────────────────────────────────────────┘
```

## Auteur

Adam Jalal - Stage L3 Matériaux / Data / Informatique
Aptiskills - 2025
