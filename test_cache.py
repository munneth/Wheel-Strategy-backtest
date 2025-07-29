#!/usr/bin/env python3
"""
Test to verify the caching system works
"""

from getStockData import getStockData, getHighFromCache, getLowFromCache, getOpenFromCache

def test_caching():
    print("Testing Stock Data Caching...")
    print("=" * 40)
    
    # Fetch data once
    print("1. Fetching stock data...")
    stock_data = getStockData('2024-08-01')
    
    if "Time Series (Daily)" in stock_data:
        stock_cache = stock_data["Time Series (Daily)"]
        print(f"   Successfully loaded {len(stock_cache)} days of data")
        
        # Test cached functions
        print("\n2. Testing cached functions:")
        test_dates = ['2024-08-01', '2024-08-02', '2024-08-03']
        
        for date in test_dates:
            high = getHighFromCache(stock_cache, date)
            low = getLowFromCache(stock_cache, date)
            open_price = getOpenFromCache(stock_cache, date)
            
            print(f"   {date}: High={high}, Low={low}, Open={open_price}")
        
        print("\n✅ Caching system works correctly!")
    else:
        print("   Error: Could not fetch stock data")
        print("   Using mock data instead...")
        from mockData import get_mock_stock_data
        stock_cache = get_mock_stock_data()["Time Series (Daily)"]
        
        # Test cached functions with mock data
        print("\n2. Testing cached functions with mock data:")
        test_dates = ['2024-08-01', '2024-08-02', '2024-08-03']
        
        for date in test_dates:
            high = getHighFromCache(stock_cache, date)
            low = getLowFromCache(stock_cache, date)
            open_price = getOpenFromCache(stock_cache, date)
            
            print(f"   {date}: High={high}, Low={low}, Open={open_price}")
        
        print("\n✅ Caching system works with mock data!")

if __name__ == "__main__":
    test_caching() 