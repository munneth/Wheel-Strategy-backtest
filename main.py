import os
from dotenv import load_dotenv
from getOptionsData import getViableOptions, getStrikes, getBids, day, date, options

# Load environment variables from .env file
load_dotenv()
# Now you can access environment variables
api_key = os.getenv('ALPHA_API_KEY')

def main():
    strikes = getStrikes(getViableOptions(options, day))
    bids = getBids(getViableOptions(options, day))
    print(strikes)
    print(bids)

if __name__ == "__main__":
    main()
