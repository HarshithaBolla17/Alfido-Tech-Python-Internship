import pandas as pd
import matplotlib.pyplot as plt

# STEP 1: Load dataset
df = pd.read_csv("data.csv")

# STEP 2: Display first rows
print("FIRST 5 ROWS:")
print(df.head())

# STEP 3: Dataset information
print("\nDATASET INFO:")
print(df.info())

# STEP 4: Statistical summary
print("\nSTATISTICAL SUMMARY:")
print(df.describe())

# STEP 5: Check missing values
print("\nMISSING VALUES:")
print(df.isnull().sum())

# STEP 6: Remove missing values
df = df.dropna()

# STEP 7: Convert data types
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
df['date'] = pd.to_datetime(df['date'], dayfirst=True, errors='coerce')

# STEP 8: Filter products with price greater than 2000
filtered_df = df[df['price'] > 2000]

print("\nFILTERED PRODUCTS (PRICE > 2000):")
print(filtered_df)

# STEP 9: Group by category and calculate average price
grouped = df.groupby('category')['price'].mean()

print("\nAVERAGE PRICE BY CATEGORY:")
print(grouped)

# STEP 10: Multiple aggregations
summary = df.groupby('category').agg({
    'price': ['mean', 'max', 'min'],
    'quantity': 'sum'
})

print("\nCATEGORY SUMMARY:")
print(summary)

# STEP 11: Sort by highest price
top_products = df.sort_values(by='price', ascending=False)

print("\nPRODUCTS SORTED BY PRICE:")
print(top_products)

# STEP 12: Create bar chart
df['category'].value_counts().plot(kind='bar')

plt.title("Products by Category")
plt.xlabel("Category")
plt.ylabel("Count")

plt.show()

# STEP 13: Save cleaned dataset
df.to_csv("cleaned_data.csv", index=False)

# STEP 14: Insight Summary
print("\nINSIGHT SUMMARY:")
print("1. Dataset contains product sales information.")
print("2. Electronics products are more expensive than Clothing products.")
print("3. Laptop is the most expensive product.")
print("4. No major missing values were found after cleaning.")
print("5. Data was grouped by category to analyze average prices.")