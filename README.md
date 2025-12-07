# Customer Shopping Behavior Analysis

## Project Overview
This project aims to analyze customer shopping behavior using transactional, demographic, and purchase data. The goal is to uncover insights on customer segments, purchasing patterns, product preferences, and revenue contributions to inform marketing, sales, and business strategies.

The analysis leverages **Python (Pandas, Seaborn, Matplotlib)** for data cleaning and exploration, **SQL** for querying aggregated metrics, and **Power BI** for interactive visualizations.

---

## Repository Contents

| File | Description |
|------|-------------|
| `customer_shopping_behavior.csv` | Raw dataset containing customer transactions, demographics, and purchase details. |
| `Customer_behavior_analysis.ipynb` | Python notebook performing data cleaning, feature engineering, exploratory data analysis (EDA), and visualizations. |
| `Customer_behavior_analysis.sql` | SQL queries for analyzing revenue, discounts, top products, shipping comparisons, and customer segmentation. |
| `Customer Behavior.pbix` | Power BI report visualizing key metrics such as revenue by segment, purchase trends, and seasonal patterns. |
| `README.md` | Documentation describing the project, dataset, and analyses. |

---

## Data Description
The dataset `customer_shopping_behavior.csv` contains the following fields:

- `customer_id` : Unique identifier for each customer  
- `age` : Customer age  
- `gender` : Customer gender  
- `item_purchased` : Name of the purchased item  
- `category` : Item category  
- `purchase_amount` : Amount spent per transaction  
- `location` : Customer location  
- `size` : Size of the purchased item  
- `color` : Color of the purchased item  
- `season` : Season of purchase  
- `review_rating` : Customer review rating  
- `subscription_status` : Whether customer has a subscription  
- `shipping_type` : Type of shipping selected  
- `discount_applied` : Whether a discount was applied  
- `previous_purchases` : Number of previous purchases  
- `payment_method` : Payment method used  
- `age_group` : Derived age group based on `age`  
- `purchase_frequency_days` : Derived numeric representation of purchase frequency  
- `customer_segement` : Derived segment (`New`, `Returning`, `Loyal`)  

---

## Analysis Performed

### Python / Jupyter Notebook
- Data Cleaning and preprocessing (handling nulls, renaming columns, creating derived columns like `age_group` and `customer_segement`)  
- Exploratory Data Analysis (EDA):
  - Distribution of numeric variables (purchase amount, review rating, age, etc.)  
  - Countplots for categorical variables (gender, category, subscription status, shipping type, payment method, etc.)  
  - Barplots for revenue by gender, discount usage by age group, and subscription status per customer segment  
  - Stacked bar chart of purchase amount by season and category with values annotated  

### SQL Queries
- Total revenue by gender  
- Customers who used a discount but spent above average  
- Top 5 products by average review rating  
- Comparison of average purchase amount between standard and express shipping  
- Average spend and total revenue for subscribers vs non-subscribers  
- Top 5 products with the highest percentage of discounted purchases  
- Customer segmentation counts (New, Returning, Loyal)  
- Top 3 most purchased products within each category  
- Subscription behavior of repeat buyers  
- Revenue contribution by age group  

### Power BI
- Interactive dashboards visualizing:
  - Purchase trends over seasons and categories  
  - Revenue distribution across customer segments and age groups  
  - Subscription and discount impact on purchases  
  - Top products and categories  

---

## Tools & Technologies
- **Python:** Pandas, NumPy, Matplotlib, Seaborn  
- **SQL:** PostgreSQL for aggregation and querying  
- **Power BI:** Interactive dashboards and visualizations  

---

## Key Insights
- Revenue is influenced by customer segments, age groups, and gender.  
- Discounts increase sales for certain age groups but may not always correlate with higher purchase amounts.  
- Subscription customers generally spend more on average.  
- Top products can be identified by purchase frequency and review ratings to guide marketing and inventory decisions.  
- Seasonal trends impact category-specific purchases.  

---

## How to Use
1. Open `Customer_behavior_analysis.ipynb` in Jupyter Notebook to explore the dataset, preprocessing, and visualizations.  
2. Run SQL queries in `Customer_behavior_analysis.sql` on a PostgreSQL database with the table `customer` loaded.  
3. Open `Customer Behavior.pbix` in Power BI to view interactive dashboards and insights.  

---

## License
This project is for educational and demonstration purposes only. The data and analysis should not be used for commercial purposes without permission.

