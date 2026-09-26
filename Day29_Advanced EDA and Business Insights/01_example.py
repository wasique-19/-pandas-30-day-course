import pandas as pd
import os

# ============================================================
# 1. LOAD CAPSTONE TABLES
# ============================================================

project_folder = "ecommerce_capstone"

customers = pd.read_csv(
    os.path.join(project_folder, "customers.csv")
)

products = pd.read_csv(
    os.path.join(project_folder, "products.csv")
)

orders = pd.read_csv(
    os.path.join(project_folder, "orders.csv")
)

order_items = pd.read_csv(
    os.path.join(project_folder, "order_items.csv")
)

payments = pd.read_csv(
    os.path.join(project_folder, "payments.csv")
)


# ============================================================
# 2. CLEAN / CONVERT IMPORTANT COLUMNS
# ============================================================

orders["OrderDate"] = pd.to_datetime(
    orders["OrderDate"]
)

# Ensure numeric columns are numeric
order_items["Quantity"] = pd.to_numeric(
    order_items["Quantity"],
    errors="coerce"
)

products["Price"] = pd.to_numeric(
    products["Price"],
    errors="coerce"
)


# ============================================================
# 3. MERGE TABLES
# ============================================================

full_data = (
    orders
    .merge(
        customers,
        on="CustomerID",
        how="left"
    )
    .merge(
        order_items,
        on="OrderID",
        how="left"
    )
    .merge(
        products,
        on="ProductID",
        how="left"
    )
)


# ============================================================
# CREATE CUSTOMER SEGMENT
# ============================================================

segment_map = {
    101: "Premium",
    102: "Regular",
    103: "Regular",
    104: "Premium",
    105: "New",
    106: "New"
}

full_data["CustomerSegment"] = (
    full_data["CustomerID"]
    .map(segment_map)
)


# ============================================================
# 4. CREATE REVENUE
# ============================================================

full_data["Revenue"] = (
    full_data["Quantity"] *
    full_data["Price"]
)


# ============================================================
# 5. CREATE CUSTOMER ORDER COUNTS
# ============================================================

customer_orders = (
    full_data
    .groupby("CustomerID")["OrderID"]
    .nunique()
)


# ============================================================
# 6. REPEAT-CUSTOMER RATE
# ============================================================

total_customers = customer_orders.shape[0]

repeat_customers = (
    (customer_orders > 1).sum()
)

repeat_customer_rate = (
    repeat_customers /
    total_customers
) * 100


print("\n" + "=" * 70)
print("1. REPEAT-CUSTOMER RATE")
print("=" * 70)

print(f"Total Customers   : {total_customers}")
print(f"Repeat Customers  : {repeat_customers}")
print(f"Repeat Rate       : {repeat_customer_rate:.2f}%")


# ============================================================
# 7. TOP-PERFORMING CITY BY REVENUE
# ============================================================

city_revenue = (
    full_data
    .groupby("City", as_index=False)
    .agg(
        Revenue=("Revenue", "sum")
    )
    .sort_values(
        "Revenue",
        ascending=False
    )
)

top_city = city_revenue.iloc[0]

print("\n" + "=" * 70)
print("2. TOP-PERFORMING CITY")
print("=" * 70)

print(city_revenue.to_string(index=False))

print(
    f"\nTop City: {top_city['City']} "
    f"| Revenue: ₹{top_city['Revenue']:,.2f}"
)


# ============================================================
# 8. FIRST-HALF VS SECOND-HALF PRODUCT PERFORMANCE
# ============================================================

# Create month number
full_data["Month"] = (
    full_data["OrderDate"].dt.month
)

# First half = Jan-Jun
first_half = (
    full_data[full_data["Month"] <= 6]
    .groupby("ProductName")["Revenue"]
    .sum()
)

# Second half = Jul-Dec
second_half = (
    full_data[full_data["Month"] > 6]
    .groupby("ProductName")["Revenue"]
    .sum()
)

product_comparison = pd.DataFrame({
    "FirstHalfRevenue": first_half,
    "SecondHalfRevenue": second_half
}).fillna(0)

product_comparison["Change"] = (
    product_comparison["SecondHalfRevenue"]
    - product_comparison["FirstHalfRevenue"]
)

product_comparison["ChangePercent"] = (
    product_comparison["Change"]
    /
    product_comparison["FirstHalfRevenue"].replace(
        0,
        pd.NA
    )
) * 100

product_comparison["Status"] = (
    product_comparison["Change"]
    .apply(
        lambda x:
        "Declining" if x < 0
        else "Growing"
    )
)

product_comparison = (
    product_comparison
    .reset_index()
    .sort_values(
        "Change",
        ascending=True
    )
)

print("\n" + "=" * 70)
print("3. FIRST-HALF VS SECOND-HALF PRODUCT PERFORMANCE")
print("=" * 70)

print(
    product_comparison.to_string(
        index=False
    )
)

declining_products = product_comparison[
    product_comparison["Status"] == "Declining"
]

print("\nDeclining Products:")
print(
    declining_products[
        ["ProductName", "Change", "ChangePercent"]
    ].to_string(index=False)
)


# ============================================================
# 9. CUSTOMER SEGMENT REVENUE CONTRIBUTION
# ============================================================

segment_revenue = (
    full_data
    .groupby("CustomerSegment", as_index=False)
    .agg(
        Revenue=("Revenue", "sum")
    )
)

total_revenue = segment_revenue["Revenue"].sum()

segment_revenue["RevenueContributionPercent"] = (
    segment_revenue["Revenue"]
    / total_revenue
) * 100

segment_revenue = segment_revenue.sort_values(
    "Revenue",
    ascending=False
)

print("\n" + "=" * 70)
print("4. REVENUE CONTRIBUTION BY CUSTOMER SEGMENT")
print("=" * 70)

print(
    segment_revenue.to_string(
        index=False
    )
)


# ============================================================
# 10. ADDITIONAL BUSINESS METRICS
# ============================================================

# Total orders
total_orders = full_data["OrderID"].nunique()

# AOV
order_revenue = (
    full_data
    .groupby("OrderID")["Revenue"]
    .sum()
)

aov = order_revenue.mean()

# Top product
product_revenue = (
    full_data
    .groupby("ProductName")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

top_product = product_revenue.index[0]
top_product_revenue = product_revenue.iloc[0]

# Top customer
customer_revenue = (
    full_data
    .groupby("CustomerID")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

top_customer = customer_revenue.index[0]
top_customer_revenue = customer_revenue.iloc[0]

# Top category
category_revenue = (
    full_data
    .groupby("Category")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

top_category = category_revenue.index[0]
top_category_revenue = category_revenue.iloc[0]


# ============================================================
# 11. BUSINESS INSIGHTS
# Finding + Magnitude + Implication
# ============================================================

print("\n" + "=" * 70)
print("BUSINESS INSIGHTS REPORT")
print("=" * 70)

print(
    f"""
1. CUSTOMER RETENTION
Finding: The dataset has {repeat_customers} repeat customers
out of {total_customers} total customers.
Magnitude: Repeat-customer rate is {repeat_customer_rate:.2f}%.
Implication: Customer retention is an important opportunity for
increasing repeat purchases and lifetime value.

2. CITY PERFORMANCE
Finding: {top_city['City']} generated the highest revenue.
Magnitude: Revenue from this city was
₹{top_city['Revenue']:,.2f}.
Implication: This market should be monitored for successful
products, pricing, and customer demand patterns.

3. PRODUCT PERFORMANCE
Finding: Products were compared between the first and second
half of the year.
Magnitude: {len(declining_products)} product(s) showed declining
revenue.
Implication: Declining products should be investigated for
demand changes, pricing issues, or inventory problems.

4. CUSTOMER SEGMENT CONTRIBUTION
Finding: {segment_revenue.iloc[0]['CustomerSegment']} was the
largest revenue-contributing customer segment.
Magnitude: It contributed
{segment_revenue.iloc[0]['RevenueContributionPercent']:.2f}%
of total revenue.
Implication: Maintaining this segment is important while
developing strategies to grow smaller segments.

5. PRODUCT PERFORMANCE LEADER
Finding: {top_product} generated the highest product revenue.
Magnitude: It generated ₹{top_product_revenue:,.2f}.
Implication: The product can be prioritized for availability,
promotion, and cross-selling opportunities.

6. CATEGORY PERFORMANCE
Finding: {top_category} was the highest-revenue category.
Magnitude: Category revenue was
₹{top_category_revenue:,.2f}.
Implication: Understanding what drives this category can help
replicate successful patterns in other categories.

7. CUSTOMER VALUE
Finding: Customer {top_customer} generated the highest
individual customer revenue.
Magnitude: Total spend was ₹{top_customer_revenue:,.2f}.
Implication: High-value customers can be targeted with
retention and loyalty initiatives.

8. ORDER VALUE
Finding: The average order value across unique orders was
₹{aov:,.2f}.
Magnitude: This represents the average revenue generated
per order.
Implication: Bundles, upselling, and cross-selling could be
used to increase order value.

9. OVERALL SALES SCALE
Finding: The business recorded {total_orders} unique orders.
Magnitude: These orders generated total revenue of
₹{total_revenue:,.2f}.
Implication: Order volume and revenue should be monitored
together to distinguish growth from changes in order value.

10. PRODUCT DECLINE MONITORING
Finding: First-half and second-half revenue differences reveal
which products are losing momentum.
Magnitude: {len(declining_products)} product(s) had negative
second-half changes.
Implication: These products should receive targeted review
before additional inventory or marketing investment.
"""
)