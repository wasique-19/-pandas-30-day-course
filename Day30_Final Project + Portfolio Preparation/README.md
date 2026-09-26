# E-Commerce Capstone Project Report

## Dataset Description- 

customers.csv — X rows, 
customer demographic and signup data- orders.csv — X rows, 
order-level transaction records- order_items.csv — X rows, 
line-item level product/quantity/price data- products.csv / categories.csv — product catalog reference tables 
## Tools Used

Python, Pandas, NumPy 

## Methodology
1. Loaded and inspected 5 related tables
2. Applied systematic data-quality checks and cleaning
3. Merged into one unified analytical dataset
4. Calculated core KPIs (Revenue, AOV, order frequency)
5. Conducted EDA and answered 13 business questions

## Data-Cleaning Process

The five e-commerce tables—`customers`, `products`, `orders`, `order_items`, and `payments`—were cleaned before analysis to ensure that the KPIs were based on reliable records. Duplicate records were removed, missing values were checked and handled, and date fields such as `OrderDate` were converted to `datetime64` for time-based analysis. Categorical fields such as `City`, `Category`, and payment labels were standardized to provide consistent grouping. Numeric fields were validated so that `Quantity` and `Price` contained positive values before revenue was calculated.

The final analysis used **6 customers, 5 products, 8 unique orders, and 9 order-item records**. The resulting dataset generated **₹248,500 total revenue**.

---

## Analysis Methodology

The tables were merged using their relational keys:

* `orders.CustomerID → customers.CustomerID`
* `order_items.OrderID → orders.OrderID`
* `order_items.ProductID → products.ProductID`

Revenue was calculated using:

**Revenue = Quantity × Price**

The major KPIs were defined as follows:

| KPI                  |         Result |
| -------------------- | -------------: |
| Total Revenue        |   **₹248,500** |
| Total Unique Orders  |          **8** |
| Average Order Value  | **₹31,062.50** |
| Total Customers      |          **6** |
| Repeat Customers     |          **2** |
| Repeat-Customer Rate |     **33.33%** |

Customer-level analysis used total spend and unique order count. Customers with more than one unique order were classified as repeat customers. Customer segmentation was represented using **Premium, Regular, and New** groups.

---

## Key Findings

### 1. Customer retention is an important opportunity

**Finding:** The dataset contains 6 customers, with 2 customers making more than one purchase.

**Magnitude:** The repeat-customer rate is **33.33% (2 of 6 customers)**, meaning **66.67% of customers were not repeat customers** in the observed period.

**Implication:** Increasing repeat purchases from the current customer base could provide an additional source of revenue without relying entirely on acquiring new customers.

---

### 2. Delhi is the largest revenue-generating city

**Finding:** Delhi generated substantially more revenue than the other observed cities.

**Magnitude:** Delhi generated **₹155,000**, representing approximately **62.37% of total revenue**. Pune generated ₹54,000, Mumbai ₹30,000, Bangalore ₹5,000, and Chennai ₹4,500.

**Implication:** Delhi is the largest observed revenue market and should be examined to understand which products and customer behaviors are driving its performance.

---

### 3. Laptop is the leading revenue-generating product

**Finding:** Laptop generated the highest revenue among the five products.

**Magnitude:** Laptop generated **₹120,000**, approximately **48.29% of total revenue**. Smartphone generated ₹60,000 and Monitor generated ₹54,000.

**Implication:** Laptop sales have a substantial effect on overall business revenue, so inventory availability and customer demand for this product should be monitored carefully.

---

### 4. Electronics dominates category revenue

**Finding:** Electronics products account for most of the observed revenue.

**Magnitude:** Electronics products—Laptop, Smartphone, and Monitor—generated **₹234,000**, approximately **94.17% of the ₹248,500 total revenue**. Accessories generated the remaining **₹14,500**, approximately **5.83%**.

**Implication:** The business currently has strong dependence on Electronics. Expanding successful accessory sales could help diversify the revenue mix.

---

### 5. Average order value is ₹31,062.50

**Finding:** The business generated an average of more than ₹31,000 per unique order.

**Magnitude:** **₹248,500 total revenue ÷ 8 unique orders = ₹31,062.50 AOV.**

**Implication:** The relatively high order value provides an opportunity to investigate bundles and cross-selling strategies that could increase the value of future orders.

---

### 6. Revenue is concentrated among the highest-value customers

**Finding:** Customer-level analysis shows substantial differences in spending.

**Magnitude:** Customer 101 generated **₹95,000**, Customer 105 generated **₹60,000**, and Customer 103 generated **₹54,000**. Together, these three customers generated **₹209,000**, approximately **84.11% of total revenue**.

**Implication:** A large share of revenue comes from a small group of customers, making retention and relationship management important for protecting overall revenue.

---

### 7. Premium customers contribute the largest segment revenue

**Finding:** Based on the assigned customer segmentation, Premium customers generated the largest revenue contribution.

**Magnitude:** Premium customers (Customers 101 and 104) generated **₹99,500**, approximately **40.04% of total revenue**. Regular customers generated **₹84,000 (33.80%)**, while New customers generated **₹65,000 (26.16%)**.

**Implication:** Premium customers represent the largest segment by revenue, so retention and personalized offers for this segment could help protect a significant portion of current sales.

---

### 8. Current data does not prove product decline

**Finding:** Every product showed zero recorded revenue in the second half of the year.

**Magnitude:** Laptop changed from **₹120,000 in the first half to ₹0 in the second half**; Smartphone from ₹60,000 to ₹0; Monitor from ₹54,000 to ₹0; Headphones from ₹10,000 to ₹0; and Keyboard from ₹4,500 to ₹0.

**Implication:** These results should **not be treated as genuine 100% product declines** because the available dataset contains only first-half transactions. Complete July–December data is required before making seasonal or declining-product decisions.

---

## Business Recommendations

### 1. Increase repeat purchases

The current repeat-customer rate is **33.33%**, with 4 of 6 customers not classified as repeat customers. Introduce targeted loyalty rewards, personalized follow-ups, and post-purchase offers to encourage additional purchases.

### 2. Protect the strongest revenue markets

Delhi generated **₹155,000, or approximately 62.37% of total revenue**. Analyze the products, customers, and order patterns behind Delhi's performance and monitor the market closely.

### 3. Protect high-performing products

Laptop alone generated **₹120,000, or approximately 48.29% of total revenue**. Maintain appropriate inventory levels and monitor demand to avoid losing revenue from stock shortages or availability issues.

### 4. Diversify beyond Electronics

Electronics generated **₹234,000, or approximately 94.17% of total revenue**. Accessories generated only ₹14,500. Cross-selling accessories with Electronics purchases could help broaden the revenue mix.

### 5. Expand the dataset before seasonal decisions

The current dataset contains **8 orders**, all within the first half of the year. July–December transactions should be added before making decisions about product declines, seasonality, or the best-performing month.

---

## Conclusion

The capstone analysis generated **₹248,500 from 8 unique orders**, with an **AOV of ₹31,062.50** and a **33.33% repeat-customer rate**. Revenue is concentrated geographically in Delhi (**₹155,000**), among Electronics (**₹234,000**), and particularly in Laptop sales (**₹120,000**).

These KPIs provide a clear starting point for customer retention, product management, and market analysis. Adding a complete full-year transaction history will make future trend and product-performance conclusions substantially more reliable.