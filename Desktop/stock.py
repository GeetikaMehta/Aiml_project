import streamlit as st,pandas as pd,numpy as np, yfinance as yf
import plotly.express as px
import matplotlib.pyplot as plt

custom_css = """
<style>
    h1, h2, h3, h4, h5, h6 {
        color: "white";
    }
    .stButton>button {
        background-color: #3498db;
        color: white;
        border-radius: 10px;
    }

</style>
"""

# Inject the CSS into the Streamlit app
st.markdown(custom_css, unsafe_allow_html=True)

st.title('Stock Dashboard')
ticker = st.sidebar.text_input('Ticker')
start_date = st.sidebar.date_input('Start Date')
end_date = st.sidebar.date_input('End Date')

data = yf.download('AAPL', start='2022-01-01', end=end_date)

# Display the first few rows of the data
print(data.head())

if ticker:
    data = yf.download(ticker, start=start_date, end=end_date)
    if data.empty:
        st.write(f"No data found for ticker: {ticker}")
    else:
        # Create a Plotly line chart
        fig = px.line(data, x=data.index, y='Close', title=f'Stock Prices for {ticker}')
        st.plotly_chart(fig)
else:
    st.write('Please enter a valid ticker and date range.')


pricing_data,fundamental_data,news=st.tabs(["Pricing Data","Fundamental Data","Top 10 News"])

with pricing_data:
    st.header('Price Movements')
    data2 = data
    data2['%Change']=data['Adj Close']/data['Adj Close'].shift(1) - 1
    data2.dropna(inplace = True)
    st.write(data2)
    annual_return = data2['data2'].mean()*252*100 
    st.write('Annual Return is',annual_return,'%')

    stdev = np.std(data['data2'].pct_change() * np.sqrt(252))  # Assuming 'Adj Close' is the column you want to use
    stdev_percent = stdev * 100  # Convert to percentage
    st.write('Standard Deviation is',stdev_percent ,'%')

with fundamental_data:
    st.write('Fundamental')

with news:
    st.write('News')

