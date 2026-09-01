import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# =========================
# 1. Setup
# =========================
os.makedirs("visualizations", exist_ok=True)

df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")

# =========================
# 2. Inspect Data
# =========================
print("\n--- DATA SHAPE ---")
print(df.shape)

print("\n--- COLUMNS ---")
print(df.columns.tolist())

print("\n--- FIRST 5 ROWS ---")
print(df.head())

print("\n--- DATA TYPES ---")
print(df.dtypes)

print("\n--- INFO ---")
df.info()

print("\n--- DESCRIBE ---")
print(df.describe())

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

print("\n--- DUPLICATES ---")
print(df.duplicated().sum())

# =========================
# 3. Data Cleaning
# =========================
df = df.drop_duplicates()

df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")

# Remove rows with invalid important values
df = df.dropna(subset=["Order Date", "Sales", "Profit"])

# =========================
# 4. Data Transformation
# =========================
df["Order Month"] = df["Order Date"].dt.to_period("M").astype(str)
df["Order Year"] = df["Order Date"].dt.year
df["Shipping Days"] = (
    df["Ship Date"] - df["Order Date"]
).dt.days

# =========================
# 5. Analysis
# =========================
sales_by_category = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

profit_by_category = (
    df.groupby("Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

sales_by_region = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

sales_by_subcategory = (
    df.groupby("Sub-Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

monthly_sales = (
    df.groupby("Order Month")["Sales"]
    .sum()
)

top_customers = (
    df.groupby("Customer Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

profit_by_subcategory = (
    df.groupby("Sub-Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

discount_profit = (
    df.groupby("Discount")["Profit"]
    .mean()
)

# =========================
# 6. NumPy Statistics
# =========================
print("\n--- STATISTICS ---")
print("Mean Sales:", np.mean(df["Sales"]))
print("Median Sales:", np.median(df["Sales"]))
print("Standard Deviation:", np.std(df["Sales"]))
print("Minimum Sales:", np.min(df["Sales"]))
print("Maximum Sales:", np.max(df["Sales"]))

# =========================
# 7. Visualizations
# =========================

# Sales by Category
plt.figure(figsize=(8, 5))
plt.bar(sales_by_category.index, sales_by_category.values)
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("visualizations/sales_by_category.png", dpi=150)
plt.close()

# Profit by Category
plt.figure(figsize=(8, 5))
plt.bar(profit_by_category.index, profit_by_category.values)
plt.title("Total Profit by Category")
plt.xlabel("Category")
plt.ylabel("Total Profit")
plt.tight_layout()
plt.savefig("visualizations/profit_by_category.png", dpi=150)
plt.close()

# Sales Over Time
plt.figure(figsize=(12, 5))
plt.plot(monthly_sales.index, monthly_sales.values, marker="o")
plt.title("Sales Over Time")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=90, fontsize=7)
plt.tight_layout()
plt.savefig("visualizations/sales_over_time.png", dpi=150)
plt.close()

# Sales Distribution
plt.figure(figsize=(8, 5))
plt.hist(df["Sales"], bins=30)
plt.title("Distribution of Sales")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("visualizations/sales_distribution.png", dpi=150)
plt.close()

# Sales vs Profit
plt.figure(figsize=(8, 5))
plt.scatter(df["Sales"], df["Profit"], alpha=0.4)
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("visualizations/sales_vs_profit.png", dpi=150)
plt.close()

# Sales by Region
plt.figure(figsize=(8, 5))
plt.bar(sales_by_region.index, sales_by_region.values)
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("visualizations/sales_by_region.png", dpi=150)
plt.close()

# Sales by Sub-Category
plt.figure(figsize=(10, 6))
plt.barh(
    sales_by_subcategory.index,
    sales_by_subcategory.values
)
plt.title("Total Sales by Sub-Category")
plt.xlabel("Total Sales")
plt.ylabel("Sub-Category")
plt.tight_layout()
plt.savefig("visualizations/sales_by_subcategory.png", dpi=150)
plt.close()

# Top 10 Customers
plt.figure(figsize=(10, 6))
plt.barh(
    top_customers.index[::-1],
    top_customers.values[::-1]
)
plt.title("Top 10 Customers by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Customer")
plt.tight_layout()
plt.savefig("visualizations/top_customers.png", dpi=150)
plt.close()

# Profit by Sub-Category
plt.figure(figsize=(10, 6))
plt.barh(
    profit_by_subcategory.index,
    profit_by_subcategory.values
)
plt.title("Profit by Sub-Category")
plt.xlabel("Total Profit")
plt.ylabel("Sub-Category")
plt.tight_layout()
plt.savefig("visualizations/profit_by_subcategory.png", dpi=150)
plt.close()

# Discount Impact
plt.figure(figsize=(8, 5))
plt.plot(
    discount_profit.index,
    discount_profit.values,
    marker="o"
)
plt.title("Average Profit by Discount")
plt.xlabel("Discount")
plt.ylabel("Average Profit")
plt.tight_layout()
plt.savefig("visualizations/discount_impact.png", dpi=150)
plt.close()

# =========================
# 8. Insights
# =========================
print("\n--- KEY INSIGHTS ---")

print(
    "Top category by sales:",
    sales_by_category.index[0]
)

print(
    "Top category by profit:",
    profit_by_category.index[0]
)

print(
    "Top region by sales:",
    sales_by_region.index[0]
)

print(
    "Top sub-category by sales:",
    sales_by_subcategory.index[0]
)

print(
    "Top customer by sales:",
    top_customers.index[0]
)

print(
    "Most profitable sub-category:",
    profit_by_subcategory.index[0]
)

# =========================
# 9. Validation
# =========================
print("\n--- VALIDATION ---")

assert df.duplicated().sum() == 0
assert df["Order Date"].isnull().sum() == 0
assert df["Sales"].isnull().sum() == 0
assert df["Profit"].isnull().sum() == 0

print("Duplicates:", df.duplicated().sum())
print("Missing Order Dates:", df["Order Date"].isnull().sum())
print("Missing Sales:", df["Sales"].isnull().sum())
print("Missing Profit:", df["Profit"].isnull().sum())

print("\n================================")
print("PROJECT COMPLETED SUCCESSFULLY")
print("================================")