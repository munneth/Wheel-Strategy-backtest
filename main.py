import os
from dotenv import load_dotenv
from getOptionsData import getViableOptions, getStrikes, getBids, getDay, date, options

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

    
    strikes = getStrikes(getViableOptions(options, day))
    bids = getBids(getViableOptions(options, day))
    print(strikes)
    print(bids)

if __name__ == "__main__":
    main()
