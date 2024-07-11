import requests
import pandas as pd
import matplotlib.pyplot as plt

API_KEY = 'Your api key'
symbol = 'AAPL'
function = 'TIME_SERIES_DAILY'
url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={API_KEY}'

response = requests.get(url)
data = response.json()

# JSON data into a DataFrame
df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient='index')
df = df.astype(float)
df.index = pd.to_datetime(df.index)
df.sort_index(inplace=True)
print(df.head())
df.to_csv('stock_data.csv')
df['SMA_50'] = df['4. close'].rolling(window=50).mean()
df['SMA_200'] = df['4. close'].rolling(window=200).mean()

plt.figure(figsize=(14, 7))
plt.plot(df['4. close'], label='Close Price')
plt.plot(df['SMA_50'], label='50-Day SMA')
plt.plot(df['SMA_200'], label='200-Day SMA')
plt.title('Stock Price and Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()
