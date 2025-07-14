import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Now you can access environment variables
api_key = os.getenv('ALPHA_API_KEY')


#url
date='2024-08-01'#most volatile time period for market in 2024
url = f'https://www.alphavantage.co/query?function=HISTORICAL_OPTIONS&symbol=AMZN&apikey={api_key}&date={date}'
r = requests.get(url)
data = r.json()


#print(data.data[0])

#parse date to get day
day = int(date[8:10])



#parse json to get all options within 30-35 day expiration from date

options = data["data"]
viableOptions = []

print(options[0]['expiration'])

i = 0
while i < len(options):
    optionsExpire = options[i]['expiration']
    expire_day = int(optionsExpire[8:10])
    expire_month = optionsExpire[5:7]
    
    if expire_month == '09':
        # For September options from August 1st
        # September 1st = 31 days, September 2nd = 32 days, etc.
        days_diff = 31 + expire_day - 1  # 31 days to Sept 1st, then add remaining days
        
        if 30 <= days_diff <= 35:
            viableOptions.append(options[i])
            print(f"Found option expiring in {days_diff} days: {options[i]['contractID']}")
    i += 1
