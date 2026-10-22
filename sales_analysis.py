import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales_data.csv')

# print(df.duplicated().sum())
# print(df.isnull().sum())

#revenue of products
df['Revenue'] = df['Quantity'] * df['Price']

#total revenue
total_revenue = df['Revenue'].sum()

#print(df.head())
print(f"Total Revenue: ${total_revenue:.2f}")


#Find the best-selling product by revenue
best_selling_product = df.groupby('Product')['Revenue'].sum().idxmax()
print(f"Best-selling product: {best_selling_product}")


# city-wise revenue analysis

city_revenue = (
    df.groupby("City")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print(city_revenue)

bars = plt.bar(city_revenue.index, city_revenue.values)
plt.bar_label(bars, fmt="%.0f")
plt.title("Revenue by City")
plt.xlabel("City")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

















#total revenue for each product
product_revenue = (
    df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print(product_revenue)

bars =plt.bar(product_revenue.index, product_revenue.values)
plt.bar_label(bars, fmt="%.0f")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



#total revenue for each category
category_revenue = (df.groupby("Category")["Revenue"].sum().sort_values(ascending = False))
print(category_revenue)



#monthly revenue analysis
df["Date"] = pd.to_datetime(df["Date"],format="%d/%m/%Y")

df["Month"] = df["Date"].dt.month

monthly_revenue = (
    df.groupby("Month")["Revenue"]
    .sum()
    .sort_index()
)

print(monthly_revenue)

plt.figure(figsize=(8, 5))
plt.plot(
    monthly_revenue.index,
    monthly_revenue.values,
    marker="o",
    linestyle="-"
)

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (₹)")
plt.xticks([1, 2, 3, 4, 5])
plt.grid(True)
plt.tight_layout()
plt.show()




#top selling product by quantity
top_selling_by_qty = (df.groupby("Product")["Quantity"].sum().idxmax())

print(f"Top-selling product by quantity: {top_selling_by_qty}")



#Best city by revenue
city_revenue = df.groupby("City")["Revenue"].sum()

highest_revenue_city = city_revenue.idxmax()
highest_revenue = city_revenue.max()

print("Best city:", highest_revenue_city)
print("Total revenue:", highest_revenue)


#Best month by revenue
month_with_highest_revenue = df.groupby("Month")["Revenue"].sum()

best_month = month_with_highest_revenue.idxmax()
highest_revenue = month_with_highest_revenue.max()

print("Best month:", best_month)
print("Highest revenue:", highest_revenue)

#Revenue percentage by product
products_revenue = df.groupby("Product")["Revenue"].sum()
total_revenue = df["Revenue"].sum()

revenue_percentage = (products_revenue / total_revenue) * 100
print(revenue_percentage.round(2))




#Revenue growth rate by month
monthly_revenue = df.groupby("Month")["Revenue"].sum()
monthly_growth = monthly_revenue.pct_change() * 100
print(monthly_growth.round(2))



monthly_revenue = df.groupby("Month")["Revenue"].sum()

monthly_report = monthly_revenue.reset_index(name="Revenue")

monthly_report["Revenue_Growth_Percent"] = (
    monthly_report["Revenue"].pct_change() * 100
)

print(monthly_report.round(2))

# 1. Best-performing product
# Laptop
# Generated ₹250,000 in revenue, the largest contribution among products.

# 2. Highest-revenue city
# Delhi
# Generated ₹180,500 in revenue across the sample orders.

# 3. Strongest month
# January
# Generated ₹107,000, the highest monthly revenue in this dataset.

# 4. Most units sold
# Mouse — 23 units
# Mouse had the highest total quantity sold, despite contributing a smaller share of revenue.

# 5. Leading category
# Electronics
# Generated ₹538,000, substantially more revenue than Accessories.



#average order value
#Each order generated an average of approximately ₹37,933 in revenue in our sample dataset.
total_revenue = df["Revenue"].sum()
no_of_orders = df["Order_ID"].count()

aov = total_revenue / no_of_orders

print("Total Revenue: ₹", total_revenue)
print("Number of Orders:", no_of_orders)
print("Average Order Value: ₹", round(aov, 2))


#Revenue percentage by electronics category
total_revenue = df["Revenue"].sum()

electronics_revenue = df.loc[
    df["Category"] == "Electronics", "Revenue"
].sum()

electronics_percentage = (
    electronics_revenue / total_revenue
) * 100

print("Electronics Revenue: ₹", electronics_revenue)
print("Total Revenue: ₹", total_revenue)
print("Electronics Revenue Percentage:", round(electronics_percentage, 2), "%")
#Business insight: Electronics contributed approximately 94.55% of total revenue in our sample dataset.

