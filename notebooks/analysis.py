import pandas as pd

# =========================
# 📂 Charger les données
# =========================

mm = pd.read_csv("sap-mm-sd-analysis/sap-mm-materials.csv", delimiter=';')
sd = pd.read_csv("sap-mm-sd-analysis/sap-sd-sales.csv", delimiter=';')

# Convert numerical columns from string to numeric, handling comma as decimal separator
sd["Net_Revenue_EUR"] = sd["Net_Revenue_EUR"].str.replace(',', '.').astype(float)
sd["Unit_Price_EUR"] = sd["Unit_Price_EUR"].str.replace(',', '.').astype(float)
mm["Standard_Cost_EUR"] = mm["Standard_Cost_EUR"].str.replace(',', '.').astype(float)

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
# 💰 Calcul des marges
# =========================

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
