import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error
import statsmodels.api as sm

# Load your data (ensure the dataframes are already preprocessed)
# Example: df for your sales data, forecasted values, etc.
# You should already have your training, test sets and forecasted data
df=pd.read_csv(r"C:\Users\Saurav Kumar\python files\UPWORK PROJECTS\E COMMERCE FORECASTING\your_sales_data.csv") 
# Sample sales data (replace with your data)
df_sales =pd.read_csv(r"C:\Users\Saurav Kumar\python files\UPWORK PROJECTS\E COMMERCE FORECASTING\your_sales_data.csv") 
forecasted_sales = pd.Series([201.045295,443.957125,156.453033,504.739001,18.854272,222.218530]) # Replace with actual forecast data
mae = 155.150204315472  # Replace with actual MAE value
mse = 52266.69715452657 # Replace with actual MSE value
rmse =228.61910933805723 # Replace with actual RMSE value

# Header of the dashboard
st.title("E-Commerce Sales Performance Analysis and Forecasting Dashboard")
st.write("This dashboard provides insights into the sales performance and forecasted sales for an e-commerce business.")

# Sales Overview Section
st.header("Sales Overview")
st.write("### Total Sales")
total_sales = df_sales['Purchase Amount (USD)'].sum()  # Example column name
st.write(f"Total Sales: ${total_sales:,.2f}")

# Display Metrics
st.header("Model Evaluation Metrics")
st.write(f"**Mean Absolute Error (MAE):** {mae}")
st.write(f"**Mean Squared Error (MSE):** {mse}")
st.write(f"**Root Mean Squared Error (RMSE):** {rmse}")

# Sales Distribution Plot
st.header("Sales Distribution Over Time")
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df_sales['month'], df_sales['Purchase Amount (USD)'], label="Sales", color="blue")
ax.set_xlabel("Date")
ax.set_ylabel("Sales")
ax.set_title("Sales Distribution")
st.pyplot(fig)

# Forecasted Sales Plot
# Forecasted Sales Plot - with custom month names
st.header("Forecasted Sales for the Next 6 Months")

# Use last month from existing data
months_in_data = list(df_sales['month'].values)  # Date column contains 'April', 'May', etc.
month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']

# Find index of last month
last_month = months_in_data[-1]
last_month_idx = month_order.index(last_month)

# Generate next 6 months from last known month
forecast_months = [month_order[(last_month_idx + i) % 12] for i in range(1, 7)]

# Plot forecast
fig2, ax2 = plt.subplots(figsize=(10, 6))
ax2.plot(forecast_months, forecasted_sales, label="Forecasted Sales", color="green", marker='o')
ax2.set_xlabel("Month")
ax2.set_ylabel("Sales")
ax2.set_title("Forecasted Sales for the Next 6 Months")
ax2.grid(True)
st.pyplot(fig2)

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1522202176988-66273c2fd55f"); /* Stylish ecommerce image */
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: #ffffff;
    }
    .block-container {
        background-color: rgba(0, 0, 0, 0.6);  /* Adds semi-transparent overlay for readability */
        padding: 2rem;
        border-radius: 12px;
    }
    h1, h2, h3, h4, h5, h6, p {
        color: #ffffff !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Add any additional sections you want here like user filters, or breakdowns by location, category, etc.

# To run the dashboard, run the following in your terminal:
# streamlit run sales_dashboard.py
