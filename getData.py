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
viableOptionsStrikes = []
viableOptionsBids = []
#print(options[0]['expiration'])



i = 0
while i < len(options):
    optionsExpire = options[i]['expiration']
    if optionsExpire[5:7] == '09' and (int(optionsExpire[8:10]) >= day and int(optionsExpire[8:10]) <= day+5 ):
        viableOptions.append(options[i])
        #print(options[i])
    i += 1


# parse strike price of those in the viable options array

j = 0
while j < len(viableOptions):
    viableOptionsStrikes.append(viableOptions[j]['strike'])
    print(viableOptions[j]['strike'])
    j += 1

# parse bid of those in the viable options array

k = 0
while k < len(viableOptions):
    viableOptionsBids.append(viableOptions[k]['bid'])
    print(viableOptions[k]['bid'])
    k += 1

