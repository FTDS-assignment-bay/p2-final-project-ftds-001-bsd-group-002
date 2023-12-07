import streamlit as st
import pandas as pd
import pickle
import numpy as np
import  matplotlib.pyplot as plt
import plotly.express as px


#read csv files
df_gold = pd.read_csv('gold_historical_data.csv')

# Create a Streamlit app
st.title('Gold Closing Price Line Chart')

# Assuming 'train' has a 'Date' column and 'Close' column
# If your DataFrame has different column names, modify accordingly

fig = px.line(df_gold, x='Date', y='Close', title='Gold Closing Price', labels={'Close': 'Closing Price'})
fig.update_layout(xaxis_title='Date', yaxis_title='Closing Price')


# Display the chart using Streamlit
st.plotly_chart(fig, use_container_width=True)


