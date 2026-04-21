# 📊 Content Monetization Modeler

## 🧠 Project Overview
The **Content Monetization Modeler** is a machine learning project designed to predict **YouTube ad revenue (`ad_revenue_usd`)** based on video performance metrics and contextual features.

This project helps content creators, media companies, and advertisers understand what drives revenue and make data-driven decisions.

---

## 🎯 Problem Statement
As video creators and media companies increasingly rely on platforms like YouTube for income, predicting potential ad revenue becomes essential for business planning and content strategy.

This project builds a **regression model** to estimate ad revenue for individual videos and deploys it using a **Streamlit web application**.

---

## 💼 Business Use Cases
- **Content Strategy Optimization**: Identify high-performing content categories
- **Revenue Forecasting**: Predict income from future uploads
- **Creator Support Tools**: Provide analytics insights to creators
- **Ad Campaign Planning**: Estimate ROI based on performance metrics

---

## 🛠️ Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib
- Streamlit

---

## 📂 Dataset Information
- **Name**: YouTube Monetization Modeler
- **Format**: CSV
- **Size**: ~122,000 rows
- **Target Variable**: `ad_revenue_usd`

### Features:
- `video_id`
- `date`
- `views`, `likes`, `comments`
- `watch_time_minutes`, `video_length_minutes`
- `subscribers`
- `category`, `device`, `country`
- `ad_revenue_usd` (target)

---

## 🔄 Project Workflow

### 1. Data Loading & Understanding
- Loaded dataset and inspected structure
- Checked missing values and duplicates

### 2. Exploratory Data Analysis (EDA)
- Correlation matrix
- Distribution plots
- Category-wise revenue analysis
- Target variable distribution

### 3. Data Preprocessing
- Handled missing values (~5%)
- Removed duplicate records (~2%)
- Encoded categorical variables
- Scaled numeric features

### 4. Feature Engineering
Created new features:
- Engagement Rate = (likes + comments) / views
- Avg Watch Time per View
- Watch Time to Length Ratio
- Views to Subscriber Ratio
- Like Rate & Comment Rate

### 5. Model Building
Trained and compared 5 regression models:
- Linear Regression
- Ridge Regression
- Lasso Regression
- Random Forest Regressor
- Gradient Boosting Regressor

### 6. Model Evaluation
Used metrics:
- R² Score
- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)

👉 **Best Model:** Linear Regression (based on R² Score)

### 7. Insights Generation
- Top-performing categories identified
- Revenue variation by country and device analyzed
- Engagement metrics found to strongly influence revenue

---

## 📊 Outputs Generated
- `cleaned_data.csv`
- `model_metrics.csv`
- `best_model.pkl`
- `model_insights.txt`
- EDA visualizations:
  - correlation_matrix.png
  - numeric_distributions.png
  - top_categories.png
  - target_distribution.png

---

## 🌐 Streamlit Application

### Features:
- User input for video parameters
- Revenue prediction
- Model performance display
- Business insights visualization

### ▶️ Run the App:
```bash
streamlit run app.py