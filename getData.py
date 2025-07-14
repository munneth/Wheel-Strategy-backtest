import os
import requests
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

#print(data)

#parse date to get day
day = int(date[8:10])



#parse json to get all options within 30-35 day expiration from date

