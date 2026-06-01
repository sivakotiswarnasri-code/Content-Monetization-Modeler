import os
import joblib
import pandas as pd
import streamlit as st
import plotly.express as px


st.set_page_config(page_title="Content Monetization Modeler", layout="wide")

MODEL_PATH = os.path.join("outputs", "best_model.pkl")
CLEANED_DATA_PATH = os.path.join("outputs", "cleaned_data.csv")
METRICS_PATH = os.path.join("outputs", "model_metrics.csv")
INSIGHTS_PATH = os.path.join("outputs", "model_insights.txt")


@st.cache_resource
def load_model():
    if not os.path.exists(MODEL_PATH):
        st.error("Model file not found. Please run python1.ipynb first.")
        st.stop()
    return joblib.load(MODEL_PATH)


@st.cache_data
def load_data():
    if os.path.exists(CLEANED_DATA_PATH):
        return pd.read_csv(CLEANED_DATA_PATH)
    return None


@st.cache_data
def load_metrics():
    if os.path.exists(METRICS_PATH):
        return pd.read_csv(METRICS_PATH)
    return None


def load_insights():
    if os.path.exists(INSIGHTS_PATH):
        with open(INSIGHTS_PATH, "r", encoding="utf-8") as f:
            return f.read()
    return "Insights file not found."


model = load_model()
df = load_data()
metrics_df = load_metrics()

st.title("Content Monetization Modeler")
st.markdown("Predict **YouTube ad revenue** using video performance and contextual information.")

st.sidebar.header("Enter Video Details")

views = st.sidebar.number_input("Views", min_value=0.0, value=10000.0)
likes = st.sidebar.number_input("Likes", min_value=0.0, value=800.0)
comments = st.sidebar.number_input("Comments", min_value=0.0, value=120.0)
watch_time_minutes = st.sidebar.number_input("Watch Time (minutes)", min_value=0.0, value=25000.0)
video_length_minutes = st.sidebar.number_input("Video Length (minutes)", min_value=0.1, value=10.0)
subscribers = st.sidebar.number_input("Subscribers", min_value=0.0, value=50000.0)

category = st.sidebar.selectbox(
    "Category",
    ["Education", "Entertainment", "Gaming", "Music", "Tech", "Lifestyle", "News", "Sports"]
)

device = st.sidebar.selectbox(
    "Device",
    ["Mobile", "Desktop", "Tablet", "TV"]
)

country = st.sidebar.selectbox(
    "Country",
    ["India", "USA", "UK", "Canada", "Australia", "Germany", "France", "Brazil"]
)

year = st.sidebar.number_input("Year", min_value=2020, max_value=2035, value=2025)
month = st.sidebar.number_input("Month", min_value=1, max_value=12, value=6)
day = st.sidebar.number_input("Day", min_value=1, max_value=31, value=15)
day_of_week = st.sidebar.number_input("Day of Week (0=Mon, 6=Sun)", min_value=0, max_value=6, value=2)
week_of_year = st.sidebar.number_input("Week of Year", min_value=1, max_value=53, value=24)

safe_views = views if views != 0 else 1

engagement_rate = (likes + comments) / safe_views
avg_watch_time_per_view = watch_time_minutes / safe_views
watch_time_to_length_ratio = watch_time_minutes / (video_length_minutes + 1)
views_subscriber_ratio = views / (subscribers + 1)
like_rate = likes / safe_views
comment_rate = comments / safe_views

input_df = pd.DataFrame([{
    "views": views,
    "likes": likes,
    "comments": comments,
    "watch_time_minutes": watch_time_minutes,
    "video_length_minutes": video_length_minutes,
    "subscribers": subscribers,
    "category": category,
    "device": device,
    "country": country,
    "year": year,
    "month": month,
    "day": day,
    "day_of_week": day_of_week,
    "week_of_year": week_of_year,
    "engagement_rate": engagement_rate,
    "avg_watch_time_per_view": avg_watch_time_per_view,
    "watch_time_to_length_ratio": watch_time_to_length_ratio,
    "views_subscriber_ratio": views_subscriber_ratio,
    "like_rate": like_rate,
    "comment_rate": comment_rate
}])

if st.sidebar.button("Predict Revenue"):
    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Ad Revenue: ${prediction:,.2f}")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Model Performance")
    if metrics_df is not None:
        st.dataframe(metrics_df, width="stretch")
    else:
        st.warning("Metrics file not available.")

with col2:
    st.subheader("Project Insights")
    st.text(load_insights())

if df is not None:
    st.subheader("Visual Analytics")

    if "category" in df.columns and "ad_revenue_usd" in df.columns:
        category_rev = df.groupby("category")["ad_revenue_usd"].mean().sort_values(ascending=False)
        st.write("Average Revenue by Category")
        st.bar_chart(category_rev)

    if "country" in df.columns and "ad_revenue_usd" in df.columns:
        country_rev = df.groupby("country")["ad_revenue_usd"].mean().sort_values(ascending=False)
        st.write("Average Revenue by Country")
        st.bar_chart(country_rev)

    if "device" in df.columns and "ad_revenue_usd" in df.columns:
        device_rev = df.groupby("device")["ad_revenue_usd"].mean().sort_values(ascending=False)
        st.write("Average Revenue by Device")
        st.bar_chart(device_rev)

    

    if "views" in df.columns and "ad_revenue_usd" in df.columns:
        st.write("Views vs Ad Revenue")

        scatter_df = df[
            ["views", "ad_revenue_usd"]
        ].dropna().sample(3000)

        fig = px.scatter(
            scatter_df,
            x="views",
            y="ad_revenue_usd",
            title="Views vs Ad Revenue",
            opacity=0.6
        )

    st.plotly_chart(fig, use_container_width=True)
    st.subheader("Sample Cleaned Dataset")
    st.dataframe(df.head(20), width="stretch")

else:
    st.warning("Cleaned dataset not found. Please run python1.ipynb first.")