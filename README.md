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

fig_remise = px.scatter(merged, 
                        x='Discount_Percent', 
                        y='Margin',
                        color='Material_ID',
                        hover_data=['Customer_ID', 'Quantity'],
                        title="Analyse de l'impact des remises sur la marge brute")

# Ajuster la taille pour un format carré
fig_remise.update_layout(width=700, height=700)

fig_remise.show()
