import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Input Data Creation (10 products)
data = {
    "Product": ["Cola", "Chips", "Milk", "Juice", "Biscuits", "Yogurt", "Water", "Nuts", "Cheese", "Soda"],
    "Category": ["beverages ", "SNACKS", " Dairy", "beverages", "Snacks", "DAIRY ", " beverages", "SNACKS", "Dairy", "beverages"],
    "Price": ["Rs. 1,250", "Rs. 90", "Rs. 450", "Rs. 120", "Rs. 180", "Rs. 250", "Rs. 80", "Rs. 350", "Rs. 600", "Rs. 110"],
    "Stock": [40, 120, 60, 85, 110, 45, 150, 75, 30, 95]
}

df = pd.DataFrame(data)

# (a) Clean Category text with .str.strip() and .str.title()
df["Category"] = df["Category"].str.strip().str.title()

# (b) Clean Price text and convert to float
df["Price"] = df["Price"].str.replace("Rs. ", "", regex=False).str.replace(",", "").astype(float)

# (c) Label encoding for Category
df["Category_Code"] = df["Category"].astype("category").cat.codes

print("Cleaned Inventory DataFrame:")
print(df)

# Aggregations for plots
avg_price_cat = df.groupby("Category")["Price"].mean()
total_stock_cat = df.groupby("Category")["Stock"].sum()

# (d) Side-by-side subplots (1 row, 2 columns)
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Bar plot: Average Price per Category
axes[0].bar(avg_price_cat.index, avg_price_cat.values, color=["#4C78A8", "#F58518", "#54A24B"])
axes[0].set_title("Average Price per Category")
axes[0].set_xlabel("Category")
axes[0].set_ylabel("Average Price (Rs.)")

# Pie chart: Share of Total Stock
axes[1].pie(total_stock_cat.values, labels=total_stock_cat.index, autopct="%1.1f%%", startangle=90, colors=["#4C78A8", "#F58518", "#54A24B"])
axes[1].set_title("Total Stock Share by Category")

plt.tight_layout()
plt.savefig("inventory_plots.png")
plt.show()
print("Saved inventory_plots.png")
