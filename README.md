# vendor-performance-analysis
📊 Vendor Performance Data Analysis using Python, SQL, and Power BI. 🔎 Cleaned and transformed vendor data, created KPIs, and performed EDA. 📈 Interactive Power BI dashboard with delivery, cost, and profit insights. 💡 Found that high purchase volumes don’t always lead to high profits.

📌 Project Overview
This project analyzes vendor performance using Python, SQL, and Power BI. The goal is to evaluate vendors based on delivery efficiency, cost, and quality, enabling businesses to make data-driven decisions in vendor selection and contract negotiations.
🎯 Objectives
1. Identify high-performing vs. low-performing vendors.
2. Analyze vendor delivery timelines, cost variations, and product quality.
3. Provide actionable insights for procurement teams.
4. Build an interactive Power BI dashboard for business stakeholders.

🛠 Tools & Technologies
1. Python (Pandas, NumPy, Matplotlib, Seaborn) → Data cleaning & exploratory data analysis (EDA)
2. SQL (MySQL/PostgreSQL) → Data extraction & aggregation & EDA
3. Power BI → Data visualization & dashboard creation
4. CSV → Raw data storage

🔎 Approach
1️⃣ Data Collection
Extracted vendor transaction data from SQL database.
Data included: vendor ID, product categories, delivery dates, costs, freight charges, and profit margins.
2️⃣ Data Cleaning & Preparation (Python)
Handled missing values.
Removed duplicates and inconsistent vendor codes.
Created new calculated fields: Delivery_Delay, Cost_Deviation, Vendor_Score.
3️⃣ Exploratory Data Analysis (Python)
Correlation between purchase price, gross profit, and margins.
Identified vendors with frequent late deliveries.
Highlighted cost-efficient vendors.
4️⃣ SQL Analysis
Aggregated vendor performance by year/quarter.
Ranked vendors based on total transactions & reliability.
Created summary tables for integration into Power BI.
5️⃣ Power BI Dashboard
KPI Cards: On-time Delivery %, Average Cost per Vendor, Profit Margin % etc
Bar Charts: Top 10 Vendors by Purchase Volume.
etc

Line Charts: Vendor performance trend over time.

Drill-through filters for category-level analysis.
