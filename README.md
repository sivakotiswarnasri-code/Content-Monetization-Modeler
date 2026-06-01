# 📊 Content Monetization Modeler

## 🧠 Project Overview
The **Content Monetization Modeler** is a Machine Learning project designed to predict **YouTube ad revenue (`ad_revenue_usd`)** based on video performance metrics and contextual information.

This project helps **content creators, media companies, and advertisers** understand what drives revenue and make **data-driven business decisions**.

---

## 🎯 Problem Statement
As video creators and media companies increasingly rely on platforms like YouTube for income, predicting potential ad revenue becomes essential for **business planning and content strategy**.

This project builds a **Regression Model** to estimate ad revenue for individual videos and deploys the prediction system using a **Streamlit web application**.

---

## 💼 Business Use Cases
- **Content Strategy Optimization** → Identify high-performing content categories
- **Revenue Forecasting** → Predict expected income from future uploads
- **Creator Support Tools** → Provide analytics insights to creators
- **Ad Campaign Planning** → Estimate ROI based on performance metrics

---

## 🛠️ Tech Stack
- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Matplotlib**
- **Joblib**
- **Streamlit**

---

## 📂 Dataset Information
- **Dataset Name:** YouTube Monetization Modeler
- **Format:** CSV
- **Dataset Size:** ~122,000 Rows
- **Target Variable:** `ad_revenue_usd`

### Features Used
- `video_id`
- `date`
- `views`
- `likes`
- `comments`
- `watch_time_minutes`
- `video_length_minutes`
- `subscribers`
- `category`
- `device`
- `country`
- `ad_revenue_usd` (Target Variable)

---

## 🔄 Project Workflow

### 1️⃣ Data Loading & Understanding
- Loaded dataset
- Inspected dataset shape and structure
- Checked missing values
- Identified duplicate records

### 2️⃣ Exploratory Data Analysis (EDA)
Performed:
- Correlation Matrix
- Numeric Distribution Plots
- Category-wise Revenue Analysis
- Country-wise Revenue Analysis
- Target Variable Distribution
- Outlier Analysis

### 3️⃣ Data Preprocessing
- Handled missing values (~5%)
- Removed duplicate records (~2%)
- Converted date features
- Encoded categorical variables using **One Hot Encoding**
- Scaled numerical features using **StandardScaler**
- Applied Outlier Treatment using **IQR Method**

### 4️⃣ Feature Engineering
Created new features:

- **Engagement Rate** = `(likes + comments) / views`
- **Average Watch Time per View**
- **Watch Time to Length Ratio**
- **Views to Subscriber Ratio**
- **Like Rate**
- **Comment Rate**

### 5️⃣ Model Building
Trained and compared **5 Regression Models**:

1. Linear Regression
2. Ridge Regression
3. Lasso Regression
4. Random Forest Regressor
5. Gradient Boosting Regressor

### 6️⃣ Model Evaluation
Used evaluation metrics:

- **R² Score**
- **RMSE (Root Mean Squared Error)**
- **MAE (Mean Absolute Error)**

### 🏆 Best Model
**Linear Regression** was selected as the final model based on the **highest R² Score (0.9526)**.

---

## 📈 Key Insights
- Technology and Gaming categories generated higher average ad revenue.
- Revenue varied across different countries and devices.
- Engagement metrics such as **likes, comments, and watch time** strongly influenced ad revenue.
- Feature engineering improved model performance.

---

## 📊 Outputs Generated

### Processed Files
- `cleaned_data.csv`
- `model_metrics.csv`
- `best_model.pkl`
- `model_insights.txt`

### EDA Visualizations
- `correlation_matrix.png`
- `numeric_distributions.png`
- `top_categories.png`
- `target_distribution.png`

---

## 🌐 Streamlit Application

### Features
✅ User input for video parameters  
✅ Revenue prediction system  
✅ Model performance comparison table  
✅ Business insights visualization  
✅ Visual analytics dashboard  
✅ Cleaned dataset preview  

### Run the Streamlit App

```bash
streamlit run app.py