import pandas as pd
import yfinance as yf
import datetime
import json


def fetch_sp500_tickers():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    tables = pd.read_html(url)
    sp500_df = tables[0]
    tickers = sp500_df['Symbol'].str.strip().tolist()  
    company_names = sp500_df['Security'].str.strip().tolist()  
    return list(zip(tickers, company_names)) 


def fetch_realtime_data(ticker_info):
    print("Fetching real-time stock prices...")
    stock_data = []

    for ticker, company_name in ticker_info[:50]:  
        try:
            stock = yf.Ticker(ticker)
            data = stock.history(period="1d")
            if not data.empty:
                latest = data.iloc[-1]
                stock_data.append({
                    "Symbol": ticker,
                    "Company": company_name,  
                    "Date": latest.name.date().isoformat(),
                    "Open": latest["Open"],
                    "High": latest["High"],
                    "Low": latest["Low"],
                    "Close": latest["Close"],
                    "Volume": int(latest["Volume"])
                })
                print(f"{company_name} ({ticker}) - {latest['Close']}")
        except Exception as e:
            print(f"Error fetching data for {company_name} ({ticker}): {e}")

    today = datetime.datetime.today().strftime('%Y-%m-%d')
    filename = f"real_time_stock_data_{today}.json"

    with open(filename, "w") as json_file:
        json.dump(stock_data, json_file, indent=4)

    print(f"Data saved to {filename}")  


if __name__ == "__main__":
    ticker_info = fetch_sp500_tickers() 
    fetch_realtime_data(ticker_info)  
