import yfinance as yf
import time

def track_stock(ticker):
    while True:
        stock = yf.Ticker(ticker)
        data = stock.history(period='1d', interval='1m')
        latest_price = data['Close'].iloc[-1]
        print(f"{ticker} Latest Price: ${latest_price:.2f}")
        time.sleep(10)  # Update every 10 seconds

if __name__ == "__main__":
    ticker_symbol = input("Enter stock ticker symbol (e.g., AAPL, TSLA): ")
    track_stock(ticker_symbol)
