import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("customer_shopping_behavior.csv")

print("First 5 Rows")
print(df.head())

print("\nDataset Info")
print(df.info())


print("\nMissing Values")
print(df.isnull().sum())

df = df.drop_duplicates()

print("\nAfter Removing Duplicates")
print(df.shape)


print("\nBasic Statistics")
print(df.describe())


total_sales = df["Purchase Amount (USD)"].sum()
print("\nTotal Sales =", total_sales)


avg_purchase = df["Purchase Amount (USD)"].mean()
print("Average Purchase =", avg_purchase)

max_purchase = df["Purchase Amount (USD)"].max()
print("Maximum Purchase =", max_purchase)



print("\nGender Distribution")
print(df["Gender"].value_counts())

print("\nTop Product Categories")
print(df["Category"].value_counts())

print("\nPayment Methods")
print(df["Payment Method"].value_counts())

print("\nSeasonal Purchases")
print(df["Season"].value_counts())


sales_by_category = df.groupby("Category")["Purchase Amount (USD)"].sum()

print("\nSales by Category")
print(sales_by_category)


sales_by_gender = df.groupby("Gender")["Purchase Amount (USD)"].sum()

print("\nSales by Gender")
print(sales_by_gender)


plt.figure(figsize=(8,5))
sales_by_category.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.show()

plt.figure(figsize=(6,4))
df["Gender"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Gender Distribution")
plt.ylabel("")
plt.show()

plt.figure(figsize=(8,5))
df["Payment Method"].value_counts().plot(kind="bar")
plt.title("Payment Method Usage")
plt.xlabel("Payment Method")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(8,5))
df["Season"].value_counts().plot(kind="bar")
plt.title("Purchases by Season")
plt.xlabel("Season")
plt.ylabel("Transactions")
plt.show()


df.to_csv("cleaned_shopping_data.csv", index=False)

print("\nClean dataset saved successfully")