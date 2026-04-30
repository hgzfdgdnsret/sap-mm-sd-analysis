# 📊 SAP Business Intelligence : Analyse de Rentabilité (MM/SD)

## 📌 Présentation du Projet
Ce projet simule une mission de consultant Data/SAP. L'enjeu est de briser le silo entre le module **MM (Achats/Matériaux)** et le module **SD (Ventes)** pour répondre à une question critique : **"Quels produits génèrent réellement du profit après déduction des coûts de revient et des remises ?"**

## ⚙️ Stack Technique
*   **Langage :** Python (Pandas)
*   **Visualisation :** Plotly (Graphiques interactifs et dynamiques)
*   **Outils Business :** Logique de flux SAP ERP (MM/SD)
*   **BI :** Export propre pour intégration Power BI

## 🛠️ Pipeline de Traitement
1.  **Extraction & Nettoyage :** Chargement des fichiers `sap-mm-materials.csv` et `sap-sd-sales.csv`. Correction des formats numériques SAP (virgules décimales).
2.  **Réconciliation (Merging) :** Fusion des flux de ventes avec le référentiel des coûts via le `Material_ID`
3.  **Ingénierie de données :** Calcul automatisé du coût total, du revenu net et de la marge brute par ligne de commande
4.  **Segmentation :** Identification des produits "Stars" (forte marge) et des produits "À risque" (faible marge malgré un gros volume)

## 📈 Résultats & Analyse (Données Réelles)

### Performance Globale
*   **Chiffre d'Affaires :** 42 865 619,82 €
*   **Marge Totale :** 12 443 428,95 €
*   **Taux de Remise Moyen :** 2,34 % (Excellente maîtrise des prix).

### Focus Produits
Top Marge : MAT021 (996 199 €) – produit moteur de rentabilité principal, doit être traité comme une priorité stratégique.  

Top Volume : MAT028 (5 429 unités) – Malgré le volume le plus élevé, la marge reste faible à 51 128 €, ce qui nécessite une optimisation des coûts ou des prix.  

Top Client : CUST013 (3 390 110 €) – client majeur (Key Account), représentant un enjeu de fidélisation critique.  

Remise Moyenne : 2,34 % – La politique tarifaire est globalement maîtrisée avec une absence de dérives commerciales sur les fortes remises.

## 📊 Visualisation Interactive
*Les graphiques générés avec Plotly permettent de naviguer dans la donnée (zoom, survol) pour isoler des anomalies de prix ou des opportunités de vente croisée.*

## 📂 Structure des fichiers
*   `/notebooks/analysis.py` : Script de traitement et de calcul.
*   `sap-mm-materials.csv` : Données de coûts et groupes d'articles.
*   `sap-sd-sales.csv` : Historique des commandes et remises.
*   `donnees_completes_analyse.csv` : Dataset final enrichi pour Power BI.

Visualisations et Analyses Dynamiques
L'utilisation de la bibliothèque Plotly permet une exploration interactive des données de performance. Trois axes d'analyse ont été privilégiés pour ce dossier :  

Répartition du Chiffre d'Affaires et Profitabilité (Treemap)
https://colab.research.google.com/drive/16KUxhBpkUcr8Nd3N0uV4AtEojionN9Rv#scrollTo=59ddf7b6&fullscreenOutput=true
Ce graphique hiérarchique permet de visualiser instantanément la concentration des revenus par client et par produit. La couleur indique la rentabilité (du rouge pour les marges faibles au vert pour les profits élevés). Il met en évidence la dépendance de l'entreprise vis-à-vis du client CUST013.  

Analyse de la Rentabilité par Référence (Bar Chart)
https://colab.research.google.com/drive/16KUxhBpkUcr8Nd3N0uV4AtEojionN9Rv#scrollTo=d7e015de&fullscreenOutput=true
Ce visuel classe les 10 produits générant le plus de valeur nette. Il confirme que la référence MAT021 est le pilier financier de l'activité, contrastant avec les produits à fort volume mais à faible marge.  

Corrélation Remises / Marges (Scatter Plot)
https://colab.research.google.com/drive/16KUxhBpkUcr8Nd3N0uV4AtEojionN9Rv#scrollTo=55aa40d1&fullscreenOutput=true
Ce nuage de points analyse l'impact des politiques de remise sur le profit final. L'absence de points dans les zones de remises élevées (>20%) confirme une discipline commerciale stricte et une protection efficace de la marge brute.
