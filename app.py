import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Business Sales Analytics",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("📊 Business Sales Analytics")
st.write("Retail Sales & Customer Insights Analysis")

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("small_sales_project_100_rows.csv")

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.header("Filters")

city = st.sidebar.multiselect(
    "Select City",
    df["City"].unique(),
    default=df["City"].unique()
)

segment = st.sidebar.multiselect(
    "Select Customer Segment",
    df["Customer_Segment"].unique(),
    default=df["Customer_Segment"].unique()
)

filtered_df = df[
    (df["City"].isin(city)) &
    (df["Customer_Segment"].isin(segment))
]

# -----------------------------
# KPI
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Orders",
    filtered_df["Order_ID"].count()
)

col2.metric(
    "Total Sales",
    f"₹{filtered_df['Total_Sales'].sum():,.0f}"
)

col3.metric(
    "Total Quantity",
    filtered_df["Quantity"].sum()
)

col4.metric(
    "Average Order Value",
    f"₹{filtered_df['Total_Sales'].mean():,.0f}"
)

st.divider()

# -----------------------------
# Data
# -----------------------------
st.subheader("📋 Sales Data")

st.dataframe(
    filtered_df,
    use_container_width=True
)

# -----------------------------
# Sales by City
# -----------------------------
st.subheader("🏙️ Sales by City")

city_sales = filtered_df.groupby("City")["Total_Sales"].sum()

st.bar_chart(city_sales)

# -----------------------------
# Orders by Customer Segment
# -----------------------------
st.subheader("👥 Orders by Customer Segment")

segment_orders = filtered_df["Customer_Segment"].value_counts()

st.bar_chart(segment_orders)

# -----------------------------
# Quantity by Product
# -----------------------------
st.subheader("📦 Quantity Sold by Product")

product_quantity = (
    filtered_df.groupby("Product")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(product_quantity)

# -----------------------------
# Pivot Table
# -----------------------------
st.subheader("🔄 Sales by City and Category")

pivot_table = pd.pivot_table(
    filtered_df,
    values="Total_Sales",
    index="City",
    columns="Category",
    aggfunc="sum",
    fill_value=0
)

st.dataframe(
    pivot_table,
    use_container_width=True
)

# -----------------------------
# Crosstab
# -----------------------------
st.subheader("💳 City vs Payment Method")

cross_table = pd.crosstab(
    filtered_df["City"],
    filtered_df["Payment_Method"]
)

st.dataframe(
    cross_table,
    use_container_width=True
)

# -----------------------------
# Correlation
# -----------------------------
st.subheader("🔗 Correlation")

corr = filtered_df.corr(numeric_only=True)

fig, ax = plt.subplots()

sns.heatmap(
    corr,
    annot=True,
    ax=ax
)

st.pyplot(fig)

# -----------------------------
# Business Insights
# -----------------------------
st.subheader("💡 Business Insights")

highest_city = (
    filtered_df.groupby("City")["Total_Sales"]
    .sum()
    .idxmax()
)

highest_product = (
    filtered_df.groupby("Product")["Total_Sales"]
    .sum()
    .idxmax()
)

highest_segment = (
    filtered_df.groupby("Customer_Segment")["Quantity"]
    .sum()
    .idxmax()
)

st.write(f"🏙️ Highest Sales City: **{highest_city}**")
st.write(f"📦 Highest Sales Product: **{highest_product}**")
st.write(f"👥 Highest Quantity Customer Segment: **{highest_segment}**")