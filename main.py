import os
from dotenv import load_dotenv
from getOptionsData import getViableOptions, getStrikes, getBids, getDay, getMonth, getStrikeBidPairs, fetchOptions, getExpireDate, isMarketOpen
from getStockData import getLow, getHigh, getOpen, calendarIncrement

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
    print(options)
    print("--------------------------------")
    
    print(viableOptions)
    print("--------------------------------")

    print("How many days do you want to run the program for?")
    daysToRun = int(input())
    for option in getStrikeBidPairs(viableOptions):
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



    strikes = getStrikes(getViableOptions(options, day))
    bids = getBids(getViableOptions(options, day))
    print(strikes)
    print(bids)

    while int(month) <= int(expireMonth) and int(day) <= int(expireDay):
        print(getLow(date))
        print("\n" + "-----------------------------------" + "\n")
        print(getHigh(date))
        print("\n" + "-----------------------------------" + "\n")
        print(getOpen(date))
        print("\n" + "-----------------------------------" + "\n")
        if strikePrice <= int(getLow(date)):
            date = calendarIncrement(date)
        else:
            balance = balance - (contracts * strikePrice)
            balance = balance + (contracts * bid)
            break


    balance = balance - (contracts * strikePrice)
    balance = balance + (contracts * bid)
    print(balance)


if __name__ == "__main__":
    main()
