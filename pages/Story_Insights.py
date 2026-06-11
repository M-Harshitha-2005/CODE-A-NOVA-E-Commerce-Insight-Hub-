import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Story Insights",
    page_icon="📖",
    layout="wide"
)

st.title("📖 Business Story Insights")

# Load Data
df = pd.read_csv("data/cleaned_superstore.csv", encoding="utf-8-sig")

# Date Columns
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

# ---------------------------
# Generate Insights
# ---------------------------

top_category = (
    filtered_df.groupby('category')['sales']
    .sum()
    .idxmax()
)

top_profit_category = (
    filtered_df.groupby('category')['profit']
    .sum()
    .idxmax()
)

top_region = (
    filtered_df.groupby('region')['sales']
    .sum()
    .idxmax()
)

top_segment = (
    filtered_df.groupby('segment')['sales']
    .sum()
    .idxmax()
)

total_sales = filtered_df['sales'].sum()
total_profit = filtered_df['profit'].sum()

# ---------------------------
# Story
# ---------------------------

st.subheader("📊 Executive Summary")

st.success(
    f"Total Sales generated during the selected period were ${total_sales:,.0f}."
)

st.success(
    f"Total Profit generated during the selected period was ${total_profit:,.0f}."
)

st.markdown("---")

st.subheader("🏆 Key Business Findings")

st.info(
    f"Technology, Furniture, and Office Supplies were analyzed. "
    f"The highest sales came from **{top_category}**."
)

st.info(
    f"The most profitable category was **{top_profit_category}**."
)

st.info(
    f"The strongest performing region was **{top_region}**."
)

st.info(
    f"The highest revenue contribution came from the **{top_segment}** segment."
)

st.markdown("---")

st.subheader("📈 Business Recommendation")

st.warning(
    f"Focus future marketing efforts on the {top_category} category "
    f"and strengthen customer engagement in the {top_region} region "
    f"to maximize future revenue growth."
)