import os
import requests
import json
from dotenv import load_dotenv
from datetime import datetime, timedelta

# Load environment variables from .env file
load_dotenv()
# Now you can access environment variables
api_key = os.getenv('ALPHA_API_KEY')

#url
#date='2024-08-01'#most volatile time period for market in 2024

# Remove the old top-level code that fetched options with a hardcoded date

def fetchOptions(date):
    url = f'https://www.alphavantage.co/query?function=HISTORICAL_OPTIONS&symbol=AMZN&apikey={api_key}&date={date}'
    r = requests.get(url)
    data = r.json()
    if 'data' in data:
        return data['data']
    else:
        print("Warning: 'data' key not found in API response:", data)
        return []


#parse date to get day
def getDay(date):
    day = int(date[8:10])
    return day

#parse date to get month
def getMonth(date):
    month = int(date[5:7])
    return month
 
def getExpireDate(strikeBidExpireArray, selectedBid, selectedStrike):
    for option in strikeBidExpireArray:
        if option[2] == selectedBid and option[1] == selectedStrike:
            return option[0]

#parse json to get all options within 30-35 day expiration from date

viableOptions = []
viableOptionsStrikes = []
viableOptionsBids = []
#print(options[0]['expiration'])


def getViableOptions(options, start_date):
    """
    Returns options expiring between 30 and 45 days after the user-input start_date.
    start_date: string in 'YYYY-MM-DD' format
    """
    viableOptions = []
    start_dt = datetime.strptime(start_date, '%Y-%m-%d')
    min_expiry = start_dt + timedelta(days=30)
    max_expiry = start_dt + timedelta(days=45)
    for option in options:
        expiration_str = option.get('expiration')
        try:
            expiration_dt = datetime.strptime(expiration_str, '%Y-%m-%d')
            if min_expiry <= expiration_dt <= max_expiry:
                viableOptions.append(option)
        except Exception as e:
            print(f"Skipping option with invalid expiration '{expiration_str}': {e}")
    return viableOptions


# parse strike price of those in the viable options array
def getStrikes(viableOptions):
    j = 0
    while j < len(viableOptions):
        viableOptionsStrikes.append(viableOptions[j]['strike'])
        print(viableOptions[j]['strike'])
        j += 1


# parse bid of those in the viable options array
def getBids(viableOptions):
    k = 0
    while k < len(viableOptions):
        viableOptionsBids.append(viableOptions[k]['bid'])
        print(viableOptions[k]['bid'])
        k += 1 


def getStrikeBidPairs(viableOptions):
    pairs = []
    for option in viableOptions:
        expiration = option.get('expiration')
        strike = option.get('strike')
        bid = option.get('bid')
        pairs.append((expiration, strike, bid))
    return pairs 