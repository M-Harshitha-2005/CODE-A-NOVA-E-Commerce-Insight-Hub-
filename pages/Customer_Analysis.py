import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Customer Analysis",
    
    layout="wide"
)

st.title(" Customer Analysis")

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

# Sales by Segment
st.subheader("Sales by Segment")

segment_sales = (
    filtered_df.groupby('segment')['sales']
    .sum()
    .reset_index()
)

fig1 = px.pie(
    segment_sales,
    names='segment',
    values='sales',
    title='Sales by Segment'
)

st.plotly_chart(fig1, use_container_width=True)

# Top Customers
st.subheader("Top 10 Customers")

top_customers = (
    filtered_df.groupby('customer_name')['sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig2 = px.bar(
    top_customers,
    x='sales',
    y='customer_name',
    orientation='h',
    title='Top 10 Customers',
    height=500
)

st.plotly_chart(fig2, use_container_width=True)

# Orders by Segment
st.subheader("Orders by Segment")

segment_orders = (
    filtered_df.groupby('segment')['order_id']
    .count()
    .reset_index()
)

fig3 = px.bar(
    segment_orders,
    x='segment',
    y='order_id',
    title='Orders by Segment',
    height=400
)

st.plotly_chart(fig3, use_container_width=True)