# sap-mm-sd-analysis
Analyse des flux achats/ventes inspirés de SAP (MM/SD)

## 🎯 Objectif
Analyser les flux achats (MM) et ventes (SD) inspirés de SAP afin d'identifier des inefficacités opérationnelles et des leviers d'amélioration.

---

## 📦 Données

### 🔹 MM (Material Management)
Données liées aux matériaux et aux coûts :
- Material_ID
- Material_Group
- Standard_Cost_EUR
- Plant

👉 Permet d’analyser les coûts de production / approvisionnement

---

### 🔹 SD (Sales & Distribution)
Données liées aux ventes :
- Order_ID
- Order_Date
- Customer_ID
- Material_ID
- Quantity
- Unit_Price_EUR
- Discount_Percent
- Net_Revenue_EUR

👉 Permet d’analyser la performance commerciale

---

## 🔍 Analyses prévues

### 📊 Côté ventes (SD)
- chiffre d’affaires total
- analyse des remises (discount)
- produits les plus vendus
- performance par client

### 📦 Côté coûts (MM)
- coût moyen par produit
- analyse par groupe de matériaux
- comparaison coût vs revenu

---

## 🔗 Croisement MM / SD

- marge par produit = revenu - coût
- identification des produits peu rentables
- analyse performance globale

---

## 💡 Objectif final

Identifier :
- les produits les plus rentables
- les anomalies de prix ou de remises
- les opportunités d’optimisation business

---

## 🚀 Compétences mobilisées

- Analyse de données (Python / pandas)
- Compréhension des processus SAP MM/SD
- Logique business (coûts, revenus, marge)
