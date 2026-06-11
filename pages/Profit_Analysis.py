import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Profit Analysis", page_icon="💰", layout="wide")

st.title("💰 Profit Analysis")

# Load Data
df = pd.read_csv("data/cleaned_superstore.csv", encoding="utf-8-sig")

df['order_date'] = pd.to_datetime(df['order_date'])

df['month'] = df['order_date'].dt.month_name()
df['year'] = df['order_date'].dt.year

# Filters
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

filtered_df = df[df['year'] == selected_year]

if selected_month != "All":
    filtered_df = filtered_df[
        filtered_df['month'] == selected_month
    ]

# Profit by Category
st.subheader("Profit by Category")

profit_category = (
    filtered_df.groupby('category')['profit']
    .sum()
    .reset_index()
)

fig1 = px.bar(
    profit_category,
    x='category',
    y='profit',
    title='Profit by Category',
    height=400
)

st.plotly_chart(fig1, use_container_width=True)

# Profit by Region
st.subheader("Profit by Region")

profit_region = (
    filtered_df.groupby('region')['profit']
    .sum()
    .reset_index()
)

fig2 = px.bar(
    profit_region,
    x='region',
    y='profit',
    title='Profit by Region',
    height=400
)

st.plotly_chart(fig2, use_container_width=True)

# Discount vs Profit
st.subheader("Discount vs Profit")

fig3 = px.scatter(
    filtered_df,
    x='discount',
    y='profit',
    title='Discount vs Profit',
    height=450
)

st.plotly_chart(fig3, use_container_width=True)