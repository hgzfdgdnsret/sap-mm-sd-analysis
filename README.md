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

## 📊 1) Visualisations et Analyses Dynamiques
L'utilisation de la bibliothèque Plotly permet une exploration interactive des données de performance. Trois axes d'analyse ont été privilégiés pour ce dossier :  

Répartition du Chiffre d'Affaires et Profitabilité (Treemap)
https://colab.research.google.com/drive/16KUxhBpkUcr8Nd3N0uV4AtEojionN9Rv#scrollTo=59ddf7b6&fullscreenOutput=true

*  Ce graphique hiérarchique permet de visualiser instantanément la concentration des revenus par client et par produit. La couleur indique la rentabilité (du rouge pour les marges faibles au vert pour les profits élevés). Il met en évidence la dépendance de l'entreprise vis-à-vis du client CUST013.  

Analyse de la Rentabilité par Référence (Bar Chart)
https://colab.research.google.com/drive/16KUxhBpkUcr8Nd3N0uV4AtEojionN9Rv#scrollTo=d7e015de&fullscreenOutput=true

*  Ce visuel classe les 10 produits générant le plus de valeur nette. Il confirme que la référence MAT021 est le pilier financier de l'activité, contrastant avec les produits à fort volume mais à faible marge.  

Corrélation Remises / Marges (Scatter Plot)
https://colab.research.google.com/drive/16KUxhBpkUcr8Nd3N0uV4AtEojionN9Rv#scrollTo=55aa40d1&fullscreenOutput=true

*  Ce nuage de points analyse l'impact des politiques de remise sur le profit final. L'absence de points dans les zones de remises élevées (>20%) confirme une discipline commerciale stricte et une protection efficace de la marge brute.


## 📈 2) Analyse Comparative & Positionnement Stratégique (2023 vs 2024)
L'utilisation du filtrage temporel dans Power BI permet d'isoler les performances annuelles et d'identifier les tendances de fond du mix-produit et de la rentabilité client.

* Rappel Power Query : Correction du typage (ABC vers 1.2) : Nous avons transformé les colonnes Net_Revenue_EUR, Margin et Standard_Cost qui étaient initialement reconnues comme du texte en nombres décimaux.

Gestion des paramètres régionaux : Pour éviter les erreurs de conversion (le fameux "Error"), nous avons configuré l'importation en mode Anglais (États-Unis). Cela a permis à Power BI de comprendre que le point (.) était le séparateur décimal utilisé par ton script Python.

Normalisation des dates : Nous avons vérifié que Order_Date était bien reconnu comme une date pour permettre la création de la hiérarchie temporelle (Année, Trimestre, Mois) indispensable à ton filtre interactif.

Vérification de l'intégrité : Nous avons contrôlé qu'aucune ligne n'était en erreur après la conversion afin de garantir que la Somme de Marge (6,31 M€) soit mathématiquement exacte.

Note technique pour ton dossier : Cette phase a permis de passer d'un fichier CSV brut à un modèle de données typé, prêt pour le calcul de mesures DAX complexes comme ton Taux de Marge %.

<img width="1249" height="721" alt="image" src="https://github.com/user-attachments/assets/62799402-e626-4404-b76e-63356a9b0c92" />

<img width="1182" height="730" alt="image" src="https://github.com/user-attachments/assets/20252d5b-a29d-4864-b79c-29e2a5fd37bc" />


1. Analyse des Indicateurs Clés (KPI)
Volume de Marge : On observe une légère contraction de la marge totale, passant de 6,31 M€ en 2023 à 6,13 M€ en 2024.

Taux de Marge : La rentabilité relative reste extrêmement stable, passant de 28,50 % à 28,14 %.

Diagnostic : Cette stabilité du taux malgré la baisse du volume absolu suggère une diminution des quantités vendues ou une réduction du périmètre client, plutôt qu'une dégradation de la performance intrinsèque des produits.

2. Évolution du Mix-Produit (Somme de marge par groupe)
Automates & Transformateurs : En 2023, ces deux groupes dominent avec respectivement 27,33 % et 23,03 % de la marge. En 2024, le groupe Automates recule à 23,89 %, tandis que les Transformateurs maintiennent leur position à 22,87 %.

Câbles & Disjoncteurs : On note une montée en puissance du segment Câbles, qui passe de 16,23 % en 2023 à 17,47 % en 2024.

Positionnement Stratégique : L'entreprise semble opérer un rééquilibrage de son portefeuille. Le recul des "Automates" (produits technologiques complexes) au profit des "Câbles" (commodités) doit être surveillé pour éviter une érosion de la valeur ajoutée à long terme.

3. Analyse de la Fidélité et Performance Client
Répartition : Le graphique "Taux de Marge % par ID client" montre une granularité constante sur les deux années.

Client CUST013 : Ce compte clé maintient une performance stable, confirmant son rôle de pilier pour la structure de coût.

Observation : Les remises accordées (visibles via les variations de revenus nets par client) sont restées sous contrôle d'une année sur l'autre, évitant une guerre des prix qui aurait pu faire chuter le taux de marge sous les 28 %.

4. Recommandations Stratégiques
Sécurisation du segment Automates : Identifier les causes de la baisse de contribution (concurrence, rupture de stock MM, ou fin de cycle de vie) pour relancer ce levier de croissance.

Optimisation du segment Câbles : Puisque ce volume augmente, négocier des accords-cadres avec les fournisseurs (Module MM) pour réduire le Standard_Cost et transformer cette hausse de volume en hausse de taux de marge.

Maintien de la Discipline : La stabilité du taux de marge à ~28 % est un point fort. Il est impératif de ne pas dégrader ce ratio pour compenser la baisse de volume observée en 2024.

