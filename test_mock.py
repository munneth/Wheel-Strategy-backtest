#!/usr/bin/env python3
"""
Simple test to verify mock data works
"""

from getOptionsData import fetchOptions, getViableOptions, getStrikeBidPairs
from getStockData import getStockData, getHigh, getLow, getOpen

def test_mock_data():
    print("Testing Mock Data...")
    print("=" * 40)
    
    test_date = '2024-08-01'
    
    # Test stock data
    print("1. Testing Stock Data:")
    stock_data = getStockData(test_date)
    print(f"   Stock data keys: {list(stock_data.keys())}")
    
    high = getHigh(test_date)
    low = getLow(test_date)
    open_price = getOpen(test_date)
    print(f"   High: {high}, Low: {low}, Open: {open_price}")
    
    # Test options data
    print("\n2. Testing Options Data:")
    options = fetchOptions(test_date)
    print(f"   Total options: {len(options)}")
    
    if options:
        print(f"   Sample option: {options[0]}")
        
        # Test viable options
        viable = getViableOptions(options, test_date)
        print(f"   Viable options (30-45 days): {len(viable)}")
        
        if viable:
            print(f"   Sample viable option: {viable[0]}")
            
            # Test strike-bid pairs
            pairs = getStrikeBidPairs(viable)
            print(f"   Strike-bid pairs: {len(pairs)}")
            if pairs:
                print(f"   Sample pair: {pairs[0]}")
    
    print("\n✅ Mock data test completed!")

if __name__ == "__main__":
    test_mock_data() 