import streamlit as st
import pandas as pd

# Page Config
st.set_page_config(
    page_title="Retail Insights Dashboard",
    page_icon="📊",
    layout="wide"
)

# Load Data
df = pd.read_csv("data/cleaned_superstore.csv", encoding="utf-8-sig")

# Date Conversion
df['order_date'] = pd.to_datetime(df['order_date'])

df['month'] = df['order_date'].dt.month_name()
df['year'] = df['order_date'].dt.year

# Sidebar Filters
st.sidebar.header("Filters")

selected_year = st.sidebar.selectbox(
    "Select Year",
    sorted(df['year'].unique())
)

# Filter Data
filtered_df = df[df['year'] == selected_year]

# Title
st.title("📊 E-Commerce-Insight-Hub")

st.markdown(
    "Analyze sales, profit and customer trends using interactive filters."
)

# KPIs
total_sales = filtered_df['sales'].sum()
total_profit = filtered_df['profit'].sum()
total_orders = filtered_df['order_id'].nunique()
total_customers = filtered_df['customer_name'].nunique()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", f"${total_sales:,.0f}")
col2.metric("Total Profit", f"${total_profit:,.0f}")
col3.metric("Total Orders", total_orders)
col4.metric("Total Customers", total_customers)

st.markdown("---")

st.subheader("Dashboard Overview")

st.info(
    f"Showing business performance for {selected_year}"
)