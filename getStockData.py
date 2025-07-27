from datetime import datetime, timedelta
import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Now you can access environment variables
api_key = os.getenv('ALPHA_API_KEY')

def getStockData(date):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AMZN&outputsize=full&apikey={api_key}'
    r = requests.get(url)
    data = r.json()
    return data

# increment date by 1 day
def calendarIncrement(date):
    # date is expected in 'YYYY-MM-DD' format
    dt = datetime.strptime(date, "%Y-%m-%d")
    next_day = dt + timedelta(days=1)
    return next_day.strftime("%Y-%m-%d")

# parse open, close, high, low from data per day
def getHigh(date):
    data = getStockData(date)
    if "Time Series (Daily)" in data:
        if date in data["Time Series (Daily)"]:
            high = data["Time Series (Daily)"][date]["2. high"]
            #print(high)
            return high
        else:
            print(f"Warning: Date {date} not found in 'Time Series (Daily)'.")
            return None
    else:
        print("Warning: 'Time Series (Daily)' key not found in API response:", data)
        return None
    
def getLow(date):
    data = getStockData(date)
    low = data["Time Series (Daily)"][date]["3. low"]
    #print(low)
    return low

def getOpen(date):
    data = getStockData(date)
    open = data["Time Series (Daily)"][date]["1. open"]
    #print(open)
    return open

getHigh('2024-08-01')

    