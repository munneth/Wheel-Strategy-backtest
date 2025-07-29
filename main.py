import os
from dotenv import load_dotenv
from getOptionsData import getViableOptions, getStrikes, getBids, getDay, getMonth, getStrikeBidPairs, fetchOptions, getExpireDate, isMarketOpen, dateIncrementWithClose
from getStockData import getLow, getHigh, getOpen, calendarIncrement, getStockDataFromCache, getHighFromCache, getLowFromCache, getOpenFromCache, getStockData

# Load environment variables from .env file
load_dotenv()
# Now you can access environment variables
api_key = os.getenv('ALPHA_API_KEY')



def getValidMarketDate():
    """Recursively get a valid market date from user input"""
    print("Enter the date you want to begin from ---- EXAMPLE: 2024-08-01")
    date = input()
    if isMarketOpen(date):
        return date
    else:
        print("Market is closed on this date, please enter a different date")
        return getValidMarketDate()

def main():

    # user input
    print("Enter your account balance you have available to spend")
    balance = int(input())

    date = getValidMarketDate()
    
    expireDate = None
    day = getDay(date)
    expireDay = None
    month = getMonth(date)
    expireMonth = None
    options = fetchOptions(date)
    viableOptions = getViableOptions(options, date)
    strikePrice, bid = None, None
    #print(options)
    print("--------------------------------")
    
    #print(viableOptions)
    print("--------------------------------")

    print("How many days do you want to run the program for?")
    daysToRun = int(input())

    
    pairs = getStrikeBidPairs(viableOptions)
    print(f"Number of option pairs: {len(pairs)}")
    for option in pairs:
        print(str(option) + "\n")


    print("Enter what Strike price you would like, your bid will be the one associated with that strike price")
    strikePrice = float(input())
    print("Enter what bid you would like, your strike will be the one associated with that bid")
    bid = float(input())
    expireDate = getExpireDate(getStrikeBidPairs(viableOptions), bid, strikePrice)
    expireDay = getDay(expireDate)
    expireMonth = getMonth(expireDate)


    print("Enter how many contracts you would like to buy")
    contracts = int(input())



    strikes = getStrikes(getViableOptions(options, date))
    bids = getBids(getViableOptions(options, date))
    #print(strikes)
    #print(bids)

    # Fetch all stock data once at the beginning
    print("Fetching stock data for the entire period...")
    stock_data = getStockData(date)
    
    # Create a cache for stock prices by date
    stock_cache = {}
    if "Time Series (Daily)" in stock_data:
        stock_cache = stock_data["Time Series (Daily)"]
        print(f"Successfully loaded {len(stock_cache)} days of stock data")
    else:
        print("Error: Could not fetch stock data. Using mock data.")
        from mockData import get_mock_stock_data
        stock_cache = get_mock_stock_data()["Time Series (Daily)"]
        print(f"Using mock data with {len(stock_cache)} days")

    while int(month) <= int(expireMonth) and int(day) <= int(expireDay):
        # Get stock data from cache instead of making API calls
        low_price = getLowFromCache(stock_cache, date)
        high_price = getHighFromCache(stock_cache, date)
        open_price = getOpenFromCache(stock_cache, date)
        
        if low_price is None or high_price is None or open_price is None:
            print(f"Error: No stock data available for date: {date}")
            date = calendarIncrement(date)
            continue
            
        print("Low: " + low_price)
        print("\n" + "-----------------------------------" + "\n")
        print("High: " + high_price)
        print("\n" + "-----------------------------------" + "\n")
        print("Open: " + open_price)
        print("\n" + "-----------------------------------" + "\n")
        
        if float(strikePrice) <= float(low_price):
            date = dateIncrementWithClose(date)

        else:
            balance = balance - (contracts * strikePrice)
            balance = balance + (contracts * bid)
            break


    balance = balance - (contracts * strikePrice)
    balance = balance + (contracts * bid)
    print("Balance: " + str(balance))


if __name__ == "__main__":
    main()
