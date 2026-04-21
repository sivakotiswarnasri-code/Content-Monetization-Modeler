import os
import joblib
import pandas as pd
import streamlit as st

# PAGE SETTINGS
st.set_page_config(page_title="Content Monetization Modeler", layout="wide")

# PATHS
MODEL_PATH = os.path.join("outputs", "best_model.pkl")
CLEANED_DATA_PATH = os.path.join("outputs", "cleaned_data.csv")
METRICS_PATH = os.path.join("outputs", "model_metrics.csv")
INSIGHTS_PATH = os.path.join("outputs", "model_insights.txt")

# LOAD FUNCTIONS
@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

@st.cache_data
def load_data():
    return pd.read_csv(CLEANED_DATA_PATH)

@st.cache_data
def load_metrics():
    return pd.read_csv(METRICS_PATH)

def load_insights():
    with open(INSIGHTS_PATH, "r") as f:
        return f.read()

# LOAD DATA
model = load_model()
df = load_data()
metrics_df = load_metrics()

# TITLE
st.title("📊 Content Monetization Modeler")
st.write("""
This application predicts YouTube ad revenue based on video performance metrics.
It helps creators and businesses understand revenue-driving factors.
""")

st.markdown("---")

# SIDEBAR INPUT
st.sidebar.header("Enter Details")

views = st.sidebar.number_input("Views", value=10000.0)
likes = st.sidebar.number_input("Likes", value=800.0)
comments = st.sidebar.number_input("Comments", value=120.0)
watch_time_minutes = st.sidebar.number_input("Watch Time", value=25000.0)
video_length_minutes = st.sidebar.number_input("Video Length", value=10.0)
subscribers = st.sidebar.number_input("Subscribers", value=50000.0)

category = st.sidebar.selectbox("Category", df["category"].unique())
device = st.sidebar.selectbox("Device", df["device"].unique())
country = st.sidebar.selectbox("Country", df["country"].unique())

# FEATURE ENGINEERING
safe_views = views if views != 0 else 1

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
    "year": 2025,
    "month": 6,
    "day": 15,
    "day_of_week": 2,
    "week_of_year": 24,
    "engagement_rate": (likes + comments) / safe_views,
    "avg_watch_time_per_view": watch_time_minutes / safe_views,
    "watch_time_to_length_ratio": watch_time_minutes / (video_length_minutes + 1),
    "views_subscriber_ratio": views / (subscribers + 1),
    "like_rate": likes / safe_views,
    "comment_rate": comments / safe_views
}])

# PREDICTION
if st.sidebar.button("Predict"):
    prediction = model.predict(input_df)[0]
    st.markdown("## 💰 Predicted Revenue")
    st.success(f"Estimated Ad Revenue: ${prediction:.2f}")

# MODEL METRICS
st.markdown("---")
st.subheader("📈 Model Metrics")
st.dataframe(metrics_df)

# INSIGHTS
st.markdown("---")
st.subheader("🧠 Insights")
st.text(load_insights())

# VISUALS
st.markdown("---")
st.subheader("📊 Category Revenue")

category_rev = df.groupby("category")["ad_revenue_usd"].mean().sort_values(ascending=False)
st.bar_chart(category_rev)