
---

# PM2.5 Temperature Prediction in Mumbai 🌫️🌡️

This project focuses on predicting **PM2.5 temperature readings in Mumbai, India**, using time series forecasting models. The objective is to forecast future temperature values based on historical PM2.5 levels to help monitor and manage air quality conditions.

---

## 📊 Overview

The dataset contains **PM2.5 air quality readings specific to Mumbai**. Before modeling, I conducted a comprehensive process that included:

- **Exploratory Data Analysis (EDA)**
- **Data Cleaning & Wrangling**
- **Visualization of trends and patterns**

---

## ⚙️ Models Used

I experimented with three different time series models, using **Mean Absolute Error (MAE)** as the performance metric:

| Model              | Baseline MAE | Train MAE | Test MAE |
|-------------------|--------------|-----------|----------|
| Linear Regression | 25.18        | 5.10      | 3.52     |
| Auto Regression   | 25.34        | 4.36      | 3.35     |
| ARIMA             | 25.51        | 4.22      | 3.38     |

### Notes:
- **Baseline MAE** represents the error of a naive prediction model.
- **Lag selection** was important:
  - Linear Regression: `lag 1`
  - AutoRegression: `lag 26`
  - ARIMA: `lag 24(Auto regression), 0(difference), lad 1(moving average)`

---
### Key Findings
- All three models significantly outperformed the baseline.
- Auto Regression had the lowest test MAE, making it the most accurate model for this dataset.
- Arima took too long to model, thereby not advisable
---

## 📈 Visualizations

Several plots were generated during the analysis:
- PM2.5 trends over time in Mumbai
- Rolling averages and moving windows
- Autocorrelation & partial autocorrelation
- Model residual diagnostics

---

## 🧹 Data Wrangling

- Converted and parsed datetime fields
- Handled missing and inconsistent data
- Ensured stationarity for ARIMA
- Created lag features for forecasting

---

## 🧰 Tech Stack

- **Python**
- **Pandas**, **NumPy**
- **Scikit-learn**, **Statsmodels**
- **Matplotlib**, **Seaborn**

---

## ✅ Conclusion

This project shows the effectiveness of time series forecasting for environmental monitoring in Mumbai. All models significantly outperformed the baseline, and **Auto Regression** was the most accurate for predicting PM2.5 temperature readings.

---

