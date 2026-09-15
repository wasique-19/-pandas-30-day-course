import pandas as pd

# --------------------------------------------------
# 1. Create DataFrame with 12 orders
# --------------------------------------------------

orders = pd.DataFrame({
    "CustomerID": [
        101, 101, 101,
        102, 102, 102,
        103, 103, 103,
        104, 104, 104
    ],
    "Region": [
        "North", "North", "North",
        "South", "South", "South",
        "West", "West", "West",
        "North", "North", "North"
    ],
    "OrderAmount": [
        5000, 7000, 3000,       # Customer 101 = 15,000
        4000, 6000, 5000,       # Customer 102 = 15,000
        8000, 9000, 3000,       # Customer 103 = 20,000
        2000, 2500, 1500        # Customer 104 = 6,000
    ]
})

print("ORIGINAL ORDERS")
print(orders)


# --------------------------------------------------
# 2. KPI table per Region using named aggregation
# --------------------------------------------------

region_kpi = (
    orders
    .groupby("Region")
    .agg(
        TotalOrderAmount=("OrderAmount", "sum"),
        AverageOrderAmount=("OrderAmount", "mean"),
        OrderCount=("OrderAmount", "count")
    )
    .reset_index()
)

# Round average for cleaner output
region_kpi["AverageOrderAmount"] = (
    region_kpi["AverageOrderAmount"].round(2)
)

print("\n" + "=" * 60)
print("REGION KPI TABLE")
print("=" * 60)
print(region_kpi)


# --------------------------------------------------
# 3. Use filter() to keep customers
#    whose total spend is above ₹10,000
# --------------------------------------------------

threshold = 10000

customer_spend = (
    orders
    .groupby("CustomerID")
    .filter(
        lambda group: group["OrderAmount"].sum() > threshold
    )
)

print("\n" + "=" * 60)
print("CUSTOMERS WITH TOTAL SPEND ABOVE ₹10,000")
print("=" * 60)
print(customer_spend)


# --------------------------------------------------
# 4. Add customer's total spend using transform()
# --------------------------------------------------

orders["CustomerTotalSpend"] = (
    orders
    .groupby("CustomerID")["OrderAmount"]
    .transform("sum")
)


# --------------------------------------------------
# 5. Calculate each order's percentage
#    of customer's total spend
# --------------------------------------------------

orders["OrderPctOfCustomerTotal"] = (
    orders["OrderAmount"]
    / orders["CustomerTotalSpend"]
    * 100
)

orders["OrderPctOfCustomerTotal"] = (
    orders["OrderPctOfCustomerTotal"].round(2)
)


# --------------------------------------------------
# 6. Final transaction-level DataFrame
# --------------------------------------------------

print("\n" + "=" * 60)
print("ORDERS WITH % OF CUSTOMER TOTAL SPEND")
print("=" * 60)
print(orders)