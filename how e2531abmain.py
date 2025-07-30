[33mda56853[m[33m ([m[1;36mHEAD[m[33m -> [m[1;32mmaster[m[33m, [m[1;31morigin/master[m[33m, [m[1;31morigin/HEAD[m[33m)[m Enhance error handling in fetchOptions function to use mock data on API errors. Introduce caching mechanism in getStockData.py for improved performance, allowing retrieval of stock data from cache instead of repeated API calls. Update main.py to utilize cached stock data, ensuring smoother execution and reduced API dependency.
[33me2531ab[m Refactor print statements in getOptionsData.py to enable output, and comment out print statements in getStockData.py for cleaner execution. Added output for the number of option pairs in main.py for better visibility.
[33m30cdb12[m added 9/11 to isMarketOpen() and removed messy print statement for better debugging
[33mb1053e3[m fixed date increment to avoid incrementing to closed days,
[33md1093cb[m fixed compaqriosn type error
[33md842c88[m fixed get expire date function
[33m373aed0[m modify marketopen or close function to check for weekend as well
[33md5a119a[m made getDate recurse
[33mc78b30a[m implemented isMarketOpen() function and imported to main.py
[33mccf905d[m Remove unnecessary whitespace in main.py for cleaner code formatting.
