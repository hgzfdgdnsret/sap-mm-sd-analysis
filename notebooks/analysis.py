import pandas as pd

# =========================
# 📂 Télécharger les données (si non déjà présentes)
# =========================
!git clone https://github.com/hgzfdgdnsret/sap-mm-sd-analysis

# =========================
# 📂 Charger les données
# =========================

mm = pd.read_csv("sap-mm-sd-analysis/sap-mm-materials.csv", delimiter=';')
sd = pd.read_csv("sap-mm-sd-analysis/sap-sd-sales.csv", delimiter=';')

# Convert numerical columns from string to numeric, handling comma as decimal separator
# Using pd.to_numeric with errors='coerce' for robustness
sd["Net_Revenue_EUR"] = pd.to_numeric(sd["Net_Revenue_EUR"].astype(str).str.replace(',', '.'), errors='coerce')
sd["Unit_Price_EUR"] = pd.to_numeric(sd["Unit_Price_EUR"].astype(str).str.replace(',', '.'), errors='coerce')
sd["Discount_Percent"] = pd.to_numeric(sd["Discount_Percent"].astype(str).str.replace(',', '.'), errors='coerce') # Added for robustness
mm["Standard_Cost_EUR"] = pd.to_numeric(mm["Standard_Cost_EUR"].astype(str).str.replace(',', '.'), errors='coerce')

# =========================
# 📊 Analyse SD (ventes)
# =========================

# Chiffre d'affaires total
total_revenue = sd["Net_Revenue_EUR"].sum()
print("Chiffre d'affaires total :", total_revenue)

# Produits les plus vendus
top_products = sd.groupby("Material_ID")["Quantity"].sum().sort_values(ascending=False)
print("\nTop produits (quantité) :")
print(top_products.head())

# Clients les plus rentables
top_clients = sd.groupby("Customer_ID")["Net_Revenue_EUR"].sum().sort_values(ascending=False)
print("\nTop clients :")
print(top_clients.head())

# =========================
# 🔗 Fusion MM + SD
# =========================

merged = pd.merge(sd, mm, on="Material_ID", how="left")

# =========================
# 🧽 Nettoyage et enrichissement des données
# =========================

# Remplacer les valeurs manquantes (NaN) après la fusion
# Si un produit n'a pas de coût dans MM, on met le coût moyen pour ne pas fausser les calculs
merged["Standard_Cost_EUR"] = merged["Standard_Cost_EUR"].fillna(merged["Standard_Cost_EUR"].mean())

# Supprimer les lignes où la quantité est 0 ou négative (erreurs de saisie)
merged = merged[merged["Quantity"] > 0]

# Créer des catégories de clients basées sur leur revenu
def segment_client(revenue):
    if revenue > 3300000: return 'Diamant'
    elif revenue > 3200000: return 'Or'
    else: return 'Argent'

# Appliquer la fonction pour créer une nouvelle colonne
merged["Customer_Segment"] = merged["Net_Revenue_EUR"].apply(segment_client)

# Convertir en format Date réel
merged["Order_Date"] = pd.to_datetime(merged["Order_Date"])

# Extraire le mois et le trimestre
merged["Month"] = merged["Order_Date"].dt.month
merged["Quarter"] = merged["Order_Date"].dt.quarter

# =========================
# 💰 Calcul des marges
# =========================

# Ces calculs sont faits après le nettoyage et l'enrichissement
merged["Total_Cost"] = merged["Standard_Cost_EUR"] * merged["Quantity"]
merged["Margin"] = merged["Net_Revenue_EUR"] - merged["Total_Cost"]

# Marge totale
total_margin = merged["Margin"].sum()
print("\nMarge totale :", total_margin)

# Produits les plus rentables
top_margin_products = merged.groupby("Material_ID")["Margin"].sum().sort_values(ascending=False)
print("\nTop produits (marge) :")
print(top_margin_products.head())

# Produits les moins rentables
low_margin_products = merged.groupby("Material_ID")["Margin"].sum().sort_values()
print("\nProduits les moins rentables :")
print(low_margin_products.head())

# =========================
# ⚠️ Analyse des remises
# =========================

avg_discount = sd["Discount_Percent"].mean()
print("\nRemise moyenne :", avg_discount)

high_discount = sd[sd["Discount_Percent"] > 20]
print("\nCommandes avec forte remise : Jarder :")
print(high_discount.head())

# =========================
# 📈 Résumé Statistique Global
# =========================
print("\n--- Résumé Statistique Global ---")
print(merged.describe())

# =========================
# 💾 Exportation finale pour Power BI
# =========================
merged.to_csv("sap_analysis_final.csv", index=False)
print("\nFichier 'sap_analysis_final.csv' créé avec succès !")
# Optionnel : export format parquet (plus léger/rapide)
# merged.to_parquet("sap_analysis_final.parquet")
