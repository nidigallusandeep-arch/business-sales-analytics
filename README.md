# 📊 Business Sales Analytics

## 🔗 Live Demo

👉 [View Live Streamlit App](https://business-sales-analytics-hxprqvi4xcuchdxepp6evk.streamlit.app/)

---

## Project Overview

Business Sales Analytics is a small data analysis project created using **Python and Pandas**.

The project analyzes sales and customer data to understand business performance and find useful insights.

---

## 🎯 Problem Statement

The company has sales data but needs to understand its business performance.

This project analyzes the data to find:

- Which city has the most orders?
- Which customer segment buys the most?
- Which product has the highest sales?
- Which category performs best?
- Which payment method is commonly used?
- What is the relationship between sales, quantity, price, and discount?

---

## 🛠️ Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Streamlit
- Jupyter Notebook
- Git & GitHub

---

## 📊 Analysis Performed

### 1. GroupBy Analysis

Used `groupby()` to analyze:

- Orders by city
- Orders by customer segment
- Quantity by customer segment
- Average order value
- Sales by product
- Sales by category

### 2. Pivot Table

Created pivot tables to analyze:

- Sales by city and category
- Sales performance across different categories

### 3. Crosstab Analysis

Used `pd.crosstab()` to analyze:

- Orders by city and category
- City vs payment method
- Product vs payment method
- Payment method percentage by city

### 4. Correlation Analysis

Used correlation analysis to understand the relationship between:

- Quantity
- Unit Price
- Discount
- Total Sales

A correlation heatmap was also created using Seaborn.

---

## 📁 Dataset

The dataset contains **100 sales records**.

### Dataset Columns

| Column | Description |
|---|---|
| Order_ID | Unique order ID |
| Order_Date | Date of order |
| Customer_ID | Customer ID |
| City | Customer city |
| Customer_Segment | Customer type |
| Product | Product name |
| Category | Product category |
| Quantity | Quantity purchased |
| Unit_Price | Price per unit |
| Discount_Percent | Discount percentage |
| Total_Sales | Total sales amount |
| Payment_Method | Payment method |

---

## 📈 Dashboard Features

The Streamlit dashboard includes:

- 📌 Total Orders
- 💰 Total Sales
- 📦 Total Quantity
- 📊 Average Order Value
- 🏙️ Sales by City
- 👥 Orders by Customer Segment
- 📦 Quantity by Product
- 🔄 Pivot Table
- 🔢 Crosstab Analysis
- 💳 Payment Method Analysis
- 🔗 Correlation Heatmap
- 💡 Business Insights
- 🔍 City and Customer Segment Filters

---

## 📂 Project Structure

```text
Business-Sales-Analytics/
│
├── app.py
├── small_sales_project_100_rows.csv
├── requirements.txt
├── Untitled251.ipynb
└── README.md
