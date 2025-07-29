import json
from datetime import datetime, timedelta
import random

def generate_mock_stock_data():
    """Generate mock stock data for AMZN"""
    data = {"Time Series (Daily)": {}}
    base_price = 175.0  # Starting price
    
    # Generate data for 2024
    start_date = datetime(2024, 1, 1)
    for i in range(365):
        current_date = start_date + timedelta(days=i)
        date_str = current_date.strftime('%Y-%m-%d')
        
        # Generate realistic price movements
        daily_change = random.uniform(-0.03, 0.03)
        base_price *= (1 + daily_change)
        
        # Generate OHLC data
        open_price = base_price * random.uniform(0.99, 1.01)
        high_price = max(open_price, base_price) * random.uniform(1.0, 1.02)
        low_price = min(open_price, base_price) * random.uniform(0.98, 1.0)
        close_price = base_price
        
        data["Time Series (Daily)"][date_str] = {
            "1. open": f"{open_price:.4f}",
            "2. high": f"{high_price:.4f}",
            "3. low": f"{low_price:.4f}",
            "4. close": f"{close_price:.4f}",
            "5. volume": str(random.randint(1000000, 5000000))
        }
    
    return data

def generate_mock_options_data(date):
    """Generate mock options data for AMZN"""
    start_date = datetime.strptime(date, '%Y-%m-%d')
    current_price = 175.0
    
    # Generate expiration dates (30-60 days from the given date)
    expiration_dates = []
    for i in range(30, 61, 5):
        exp_date = start_date + timedelta(days=i)
        expiration_dates.append(exp_date.strftime('%Y-%m-%d'))
    
    # Generate strike prices around current stock price
    strike_prices = []
    for i in range(-15, 16, 5):  # -15% to +15% in 5% increments
        strike = current_price * (1 + i/100)
        strike_prices.append(round(strike, 2))
    
    options_data = []
    
    for expiration in expiration_dates:
        for strike in strike_prices:
            # Calculate realistic option prices
            time_to_expiry = (datetime.strptime(expiration, '%Y-%m-%d') - start_date).days
            moneyness = current_price / strike
            
            if moneyness > 1:  # In the money
                intrinsic_value = current_price - strike
                time_value = max(0.01, (time_to_expiry / 365.0) * 5)
            else:  # Out of the money
                intrinsic_value = 0
                time_value = max(0.01, (time_to_expiry / 365.0) * 3 * (1 - moneyness))
            
            theoretical_price = intrinsic_value + time_value
            bid = max(0.01, theoretical_price * random.uniform(0.8, 1.0))
            ask = bid * random.uniform(1.05, 1.15)
            
            # Create both call and put options
            for option_type in ['call', 'put']:
                option = {
                    'expiration': expiration,
                    'strike': str(strike),
                    'bid': f"{bid:.2f}",
                    'ask': f"{ask:.2f}",
                    'type': option_type,
                    'volume': str(random.randint(10, 1000)),
                    'open_interest': str(random.randint(50, 5000))
                }
                options_data.append(option)
    
    return options_data

# Global cache for mock data
_mock_stock_data = None
_mock_options_cache = {}

def get_mock_stock_data():
    global _mock_stock_data
    if _mock_stock_data is None:
        _mock_stock_data = generate_mock_stock_data()
    return _mock_stock_data

def get_mock_options_data(date):
    global _mock_options_cache
    if date not in _mock_options_cache:
        _mock_options_cache[date] = generate_mock_options_data(date)
    return _mock_options_cache[date] 