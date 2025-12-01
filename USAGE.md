# Guide d'utilisation

## Vue d'ensemble

Cette application Streamlit permet d'explorer la base de données de matériaux composites MHK (Marine Hydrokinetic), d'analyser leurs performances mécaniques et d'obtenir des recommandations de matériaux similaires grâce à un index FAISS.

**Source des données** : [Sandia National Laboratories - MHK Materials Database](https://energy.sandia.gov/programs/renewable-energy/wind-power/rotor-innovation/rotor-reliability/mhk-materials-database/)

## Prérequis

- Données disponibles dans `data/processed/materiaux.db`
- Application lancée : `streamlit run app.py`
- Port par défaut : http://localhost:8501

## Fonctionnalités

### 1. Exploration libre de la base de données

**Comment** :
- Ouvrir l'onglet « Exploration libre »
- Choisir les filtres : Vf %, Module E, déformation maximale, épaisseur, nombre de cycles
- Observer le message indiquant le nombre de matériaux correspondants
- Consulter le tableau interactif des matériaux filtrés
- Visualiser le graphique "Visualisation des performances mécaniques" (Contrainte maximale vs Vf %)

**Cas d'usage** :
- Consulter tous les matériaux avec un taux de fibre spécifique
- Filtrer par nombre de cycles pour applications fatigue
- Analyser la relation entre taux de fibre et contrainte maximale
- Identifier les matériaux haute performance dans la base

### 2. Recherche de similarité (FAISS)

**Comment** :
- Accéder à l'onglet « Recherche de similarité »
- Entrer les caractéristiques cibles : Taux de fibre Vf (%), Module E (GPa), Déformation maximale (%), Épaisseur (mm), Nombre de cycles
- Cliquer sur "Lancer la recherche"
- Examiner les matériaux similaires trouvés avec leurs propriétés détaillées
- Visualiser le positionnement des matériaux similaires dans l'espace FAISS

**Cas d'usage** :
- Trouver une alternative à un matériau existant
- Identifier des matériaux équivalents mais moins coûteux ou plus disponibles
- Benchmarker un matériau cible contre la base de données complète
- Découvrir des matériaux avec des propriétés mécaniques similaires

## Exemples concrets

### Exemple 1 : Recherche matériau pour réservoir hydrogène

**Objectif** : Trouver un composite résistant pour application H₂ haute pression

1. **Critères** : Vf élevé (55-65%), Module E > 60 GPa, cycles > 10000
2. **Action** : Onglet "Recherche de similarité" → Entrer Vf = 60%, Module E = 65 GPa, Cycles = 15000
3. **Résultats** : Liste des 5 matériaux les plus proches avec visualisation FAISS
4. **Analyse** : Comparaison des propriétés détaillées (contrainte max, déformation, épaisseur)
5. **Validation** : Tests physiques sur échantillons sélectionnés

### Exemple 2 : Analyse comparative de matériaux

**Objectif** : Comparer plusieurs matériaux pour application structurelle

1. **Onglet Exploration libre** → Ajuster filtres :
   - Vf : 40-60%
   - Module E : 50-80 GPa
   - Déformation max : 1-3%
2. **Observation** : "X matériaux correspondent aux critères sélectionnés"
3. **Analyse tableau** : Tri par contrainte maximale décroissante
4. **Visualisation** : Graphique montrant la distribution des performances
5. **Décision** : Shortlist de 3-5 matériaux pour phase de prototypage

### Exemple 3 : Analyse corrosion marine (MHK)

**Objectif** : Sélectionner matériaux pour hydroliennes en milieu salin

1. **Onglet Exploration libre** → Ajuster critères :
   - Cycles élevés (>50000 pour durabilité)
   - Module E élevé pour rigidité structurelle
2. **Analyse** : Visualisation des performances mécaniques
3. **Résultats** : Identification des matériaux haute endurance
4. **Export mental** : Liste retenue pour revue technique avec bureau d'études
5. **Décision** : Shortlist pour phase de prototypage marine

### Exemple 4 : Optimisation propriétés mécaniques

**Objectif** : Trouver un équilibre optimal entre rigidité et déformation

1. **Onglet Recherche de similarité** → Définir compromis cible :
   - Module E : 60 GPa (rigidité)
   - Déformation max : 2% (flexibilité)
   - Vf : 50% (manufacturabilité)
2. **Recherche** → Top 5 matériaux proches du compromis idéal
3. **Analyse** : Visualisation FAISS montrant le positionnement relatif
4. **Sélection** : Matériau avec meilleur équilibre selon cahier des charges
5. **Tests** : Validation sur pièce prototype

## Notes importantes

### Précision des données
- Base de données issue de tests expérimentaux validés (Sandia Labs)
- Données représentatives d'applications éoliennes offshore et hydroliennes
- Propriétés mécaniques mesurées en conditions contrôlées

### Limites
- Données MHK orientées applications énergies marines
- Certains matériaux exotiques peuvent manquer
- Conditions environnementales spécifiques (température extrême, pression) non systématiquement documentées

### Usage industriel
- **Pré-screening** et études de faisabilité
- Comparaisons rapides et benchmarking matériaux
- **Toujours valider** par tests physiques normés avant production
- Consulter ingénieurs matériaux pour décisions critiques

### Recherche FAISS
- Similarité calculée dans un espace normalisé à 5 dimensions
- Distance L2 utilisée pour mesurer la proximité
- Résultats quasi-instantanés (<1s) sur 1279+ vecteurs
- Visualisation 2D (déformation vs module E) pour interprétation rapide

### Source et crédibilité
- Base officielle Sandia National Laboratories (DOE/MSU)
- Données validées sur éoliennes et structures MHK
- Référence académique et industrielle reconnue

## Support

Pour toute question sur l'utilisation :
- Consulter la documentation complète dans `README.md`
- Vérifier les notebooks Jupyter (`01_preprocessing`, `02_analysis`) pour détails techniques
