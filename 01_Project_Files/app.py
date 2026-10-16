import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="BMW Sales Analytics", page_icon="🚘", layout="wide")
DATA_FILE = Path(__file__).parent / "BMW sales data (2010-2024).csv"

st.markdown("""
<style>
.stApp {background:#111522;color:#f3f6ff}
.block-container {padding-top:1.2rem}
h1,h2,h3 {color:#eaf2ff}
div[data-testid="stMetric"] {background:#20283b;border:1px solid #2875c7;padding:16px;border-radius:12px}
section[data-testid="stSidebar"] {background:#171d2c}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    return pd.read_csv(DATA_FILE)

df = load_data()
st.title("🚘 BMW Sales Performance Dashboard")
st.caption("Interactive analysis of 50,000 BMW sales records • 2010–2024")

with st.sidebar:
    st.header("Filter data")
    years = st.multiselect("Year", sorted(df.Year.unique()), default=sorted(df.Year.unique()))
    regions = st.multiselect("Region", sorted(df.Region.unique()), default=sorted(df.Region.unique()))
    models = st.multiselect("Model", sorted(df.Model.unique()), default=sorted(df.Model.unique()))
    fuels = st.multiselect("Fuel type", sorted(df.Fuel_Type.unique()), default=sorted(df.Fuel_Type.unique()))
    classifications = st.multiselect("Sales classification", sorted(df.Sales_Classification.unique()), default=sorted(df.Sales_Classification.unique()))

filtered = df[
    df.Year.isin(years) & df.Region.isin(regions) & df.Model.isin(models) &
    df.Fuel_Type.isin(fuels) & df.Sales_Classification.isin(classifications)
]
if filtered.empty:
    st.warning("No records match these filters. Change one or more filters.")
    st.stop()

total_sales = filtered.Sales_Volume.sum()
avg_price = filtered.Price_USD.mean()
avg_mileage = filtered.Mileage_KM.mean()
avg_engine = filtered.Engine_Size_L.mean()
high_records = (filtered.Sales_Classification == "High").sum()

c1,c2,c3,c4,c5 = st.columns(5)
c1.metric("Total Sales Volume", f"{total_sales:,.0f}")
c2.metric("Records", f"{len(filtered):,}")
c3.metric("Average Price", f"${avg_price:,.0f}")
c4.metric("Average Mileage", f"{avg_mileage:,.0f} km")
c5.metric("High-sales Records", f"{high_records:,}")

st.divider()
left,right = st.columns(2)
with left:
    st.subheader("Yearly Sales Trend")
    yearly = filtered.groupby("Year", as_index=False).Sales_Volume.sum()
    fig = px.line(yearly, x="Year", y="Sales_Volume", markers=True, template="plotly_dark",
                  labels={"Sales_Volume":"Sales volume"}, title=None)
    fig.update_traces(line_color="#38a3ff", marker_color="#8fd0ff")
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig, use_container_width=True)
with right:
    st.subheader("Sales by Region")
    region = filtered.groupby("Region", as_index=False).Sales_Volume.sum().sort_values("Sales_Volume")
    fig = px.bar(region, x="Sales_Volume", y="Region", orientation="h", template="plotly_dark",
                 color="Sales_Volume", color_continuous_scale=["#164e8c","#39a9ff"])
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", coloraxis_showscale=False)
    st.plotly_chart(fig, use_container_width=True)

left,right = st.columns(2)
with left:
    st.subheader("Sales by Fuel Type")
    fuel = filtered.groupby("Fuel_Type", as_index=False).Sales_Volume.sum()
    fig = px.pie(fuel, names="Fuel_Type", values="Sales_Volume", hole=.58, template="plotly_dark",
                 color_discrete_sequence=["#168cff","#55b8ff","#163d70","#8bd5ff"])
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig, use_container_width=True)
with right:
    st.subheader("Top BMW Models")
    model_sales = filtered.groupby("Model", as_index=False).Sales_Volume.sum().nlargest(10,"Sales_Volume").sort_values("Sales_Volume")
    fig = px.bar(model_sales, x="Sales_Volume", y="Model", orientation="h", template="plotly_dark",
                 color="Sales_Volume", color_continuous_scale=["#164e8c","#39a9ff"])
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", coloraxis_showscale=False)
    st.plotly_chart(fig, use_container_width=True)

left,right = st.columns(2)
with left:
    st.subheader("Average Price by Model")
    prices = filtered.groupby("Model", as_index=False).Price_USD.mean().sort_values("Price_USD", ascending=False)
    fig = px.bar(prices, x="Model", y="Price_USD", template="plotly_dark", color="Price_USD",
                 color_continuous_scale=["#164e8c","#39a9ff"])
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", coloraxis_showscale=False)
    st.plotly_chart(fig, use_container_width=True)
with right:
    st.subheader("Price vs Sales Volume")
    fig = px.scatter(filtered.sample(min(2500, len(filtered)), random_state=7), x="Price_USD", y="Sales_Volume",
                     color="Fuel_Type", hover_data=["Model","Year","Region"], template="plotly_dark",
                     labels={"Price_USD":"Price (USD)","Sales_Volume":"Sales volume"})
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Vehicle Characteristics")
char1,char2,char3 = st.columns(3)
char1.metric("Average Engine Size", f"{avg_engine:.2f} L")
char2.metric("Average Vehicle Price", f"${avg_price:,.0f}")
char3.metric("High Sales Share", f"{(high_records/len(filtered))*100:.1f}%")
st.subheader("Filtered data preview")
st.dataframe(filtered.head(100), use_container_width=True)
st.download_button("Download filtered data as CSV", filtered.to_csv(index=False).encode("utf-8"),
                   "bmw_filtered_sales.csv", "text/csv")
