import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Analysis", page_icon="📈", layout="wide")

st.title("📈 Sales Analysis")

# Load Data
df = pd.read_csv("data/cleaned_superstore.csv", encoding="utf-8-sig")

# Date Columns
df['order_date'] = pd.to_datetime(df['order_date'])

df['month'] = df['order_date'].dt.month_name()
df['year'] = df['order_date'].dt.year

# Sidebar Filters
st.sidebar.header("Filters")

selected_year = st.sidebar.selectbox(
    "Select Year",
    sorted(df['year'].unique())
)

months = ["All"] + sorted(df['month'].unique())

selected_month = st.sidebar.selectbox(
    "Select Month",
    months
)

# Filter Data
filtered_df = df[df['year'] == selected_year]

if selected_month != "All":
    filtered_df = filtered_df[
        filtered_df['month'] == selected_month
    ]

# ---------------------------------------------------
# Sales by Category
# ---------------------------------------------------

st.subheader("Sales by Category")

sales_category = (
    filtered_df.groupby('category')['sales']
    .sum()
    .reset_index()
)

fig1 = px.bar(
    sales_category,
    x='category',
    y='sales',
    title='Sales by Category',
    height=400
)

st.plotly_chart(fig1, use_container_width=True)

# ---------------------------------------------------
# Sales by Region
# ---------------------------------------------------

st.subheader("Sales by Region")

sales_region = (
    filtered_df.groupby('region')['sales']
    .sum()
    .reset_index()
)

fig2 = px.bar(
    sales_region,
    x='region',
    y='sales',
    title='Sales by Region',
    height=400
)

st.plotly_chart(fig2, use_container_width=True)

# ---------------------------------------------------
# Monthly Sales Trend
# ---------------------------------------------------

st.subheader("Monthly Sales Trend")

monthly_sales = (
    filtered_df.groupby('month')['sales']
    .sum()
    .reset_index()
)

fig3 = px.line(
    monthly_sales,
    x='month',
    y='sales',
    markers=True,
    title='Monthly Sales Trend',
    height=400
)

st.plotly_chart(fig3, use_container_width=True)

# ---------------------------------------------------
# Top 10 Products
# ---------------------------------------------------

st.subheader("Top 10 Products by Sales")

top_products = (
    filtered_df.groupby('product_name')['sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig4 = px.bar(
    top_products,
    x='sales',
    y='product_name',
    orientation='h',
    title='Top 10 Products',
    height=500
)

st.plotly_chart(fig4, use_container_width=True)