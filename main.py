import os
from dotenv import load_dotenv
from getOptionsData import getViableOptions, getStrikes, getBids, getDay, getStrikeBidPairs,date, options
from getStockData import getLow, getHigh, getOpen

# Load environment variables from .env file
load_dotenv()
# Now you can access environment variables
api_key = os.getenv('ALPHA_API_KEY')



def main():

    # user input
    print("Enter the date you want to begin from")
    date = input()
    day = getDay(date)

    print("How many days do you want to run the program for?")
    daysToRun = int(input())

    print(getStrikeBidPairs(getViableOptions(options, day)))
    print("Enter what Strike price you would like, your bid will be the one associated with that strike price")
    strikePrice = int(input())

    while int(day) < daysToRun:
        print(getLow(date))
    strikes = getStrikes(getViableOptions(options, day))
    bids = getBids(getViableOptions(options, day))
    print(strikes)
    print(bids)

if __name__ == "__main__":
    main()
