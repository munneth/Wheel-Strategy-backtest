from datetime import datetime, timedelta
import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Now you can access environment variables
api_key = os.getenv('ALPHA_API_KEY')

# Global cache for stock data
_stock_data_cache = None

def getStockData(date=None):
    """
    Get stock data once and cache it. If date is provided, it's ignored since we get full data.
    Returns the full stock data dictionary.
    """
    global _stock_data_cache
    
    if _stock_data_cache is None:
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AMZN&outputsize=full&apikey={api_key}'
        r = requests.get(url)
        data = r.json()
        _stock_data_cache = data
        print("Stock data fetched and cached")
    
    return _stock_data_cache

def getStockDataFromCache(stock_cache, date):
    """Get stock data from a cached stock data dictionary"""
    if date in stock_cache:
        daily_data = stock_cache[date]
        return {
            'low': daily_data["3. low"],
            'high': daily_data["2. high"],
            'open': daily_data["1. open"],
            'close': daily_data["4. close"]
        }
    return None

# increment date by 1 day
def calendarIncrement(date):
    # date is expected in 'YYYY-MM-DD' format
    dt = datetime.strptime(date, "%Y-%m-%d")
    next_day = dt + timedelta(days=1)
    return next_day.strftime("%Y-%m-%d")

# parse open, close, high, low from data per day - now using cached data
def getHigh(date):
    data = getStockData()  # This will use cached data if available
    if "Time Series (Daily)" in data:
        if date in data["Time Series (Daily)"]:
            high = data["Time Series (Daily)"][date]["2. high"]
            return high
        else:
            print(f"Warning: Date {date} not found in 'Time Series (Daily)'.")
            return None
    else:
        print("Warning: 'Time Series (Daily)' key not found in API response:", data)
        return None
    
def getLow(date):
    data = getStockData()  # This will use cached data if available
    if "Time Series (Daily)" in data and date in data["Time Series (Daily)"]:
        low = data["Time Series (Daily)"][date]["3. low"]
        return low
    return None

def getOpen(date):
    data = getStockData()  # This will use cached data if available
    if "Time Series (Daily)" in data and date in data["Time Series (Daily)"]:
        open_price = data["Time Series (Daily)"][date]["1. open"]
        return open_price
    return None

def getClose(date):
    data = getStockData()  # This will use cached data if available
    if "Time Series (Daily)" in data and date in data["Time Series (Daily)"]:
        close = data["Time Series (Daily)"][date]["4. close"]
        return close
    return None

# Cached versions of the functions that use the stock_cache (keeping for backward compatibility)
def getHighFromCache(stock_cache, date):
    """Get high price from cached stock data"""
    if date in stock_cache:
        return stock_cache[date]["2. high"]
    return None

def getLowFromCache(stock_cache, date):
    """Get low price from cached stock data"""
    if date in stock_cache:
        return stock_cache[date]["3. low"]
    return None

def getOpenFromCache(stock_cache, date):
    """Get open price from cached stock data"""
    if date in stock_cache:
        return stock_cache[date]["1. open"]
    return None

# Initialize cache on module import
getStockData()

    