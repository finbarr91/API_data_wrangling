import pandas as pd
import requests
import json
import statistics
import csv

# Collect data from the Franfurt Stock Exchange, for the ticker AFX_X, for the whole year 2017 (keep in mind that the date format is YYYY-MM-DD).
response_API = requests.get('https://www.quandl.com/api/v3/datasets/XFRA/AGB2_UADJ.json?api_key=fY8kwU37-CrUdj5hPxPR')
print(response_API.status_code)
print(type(response_API))
data = response_API.text
# print("\nData\n", data)

# Convert the returned JSON object into a Python dictionary.
data = json.loads(data)
print("type of data is", type(data))

# Calculate what the highest and lowest opening prices were for the stock in this period.
data = pd.read_csv(r'C:\ML Bootcamp program\Mini Project1_stock CSV.csv')
print(data)

print('The highest opening prices for the stock during the period is', max(data['Open'])) # The highest opening prices for the stock
print('The lowest opening prices for the stock',min(data['Open'])) # The lowest opening prices for the stock

# What was the largest change in any one day (based on High and Low price)?
high = data['High']
low = data['Low']
change =0
for i in range(len(data)):
    # print(high-low) # Each day's change (based on the high and low prices)
    change = max(high-low)# The largest change in any one day(based on High and Low prices)
print('The Largest Change in any one day(based on high and low prices) is', change)


# What was the average daily trading volume during this year?
vol = data['Volume']
sum_of_volume = sum(vol)
length_of_volume = len(vol)

Average = sum_of_volume/length_of_volume
print('The Average daily trading volume during this year is ',Average)

# What was the largest change between any two days (based on Closing Price)?
close = data['Close']
try:
    maximum = 0
    for i in range(len(close)):
        value = close[i]-close[i+1]
        print(value)
        if value>maximum:
            maximum=value
        print('The largest change between any two days is', maximum)
        break

except KeyError as key:
    pass

 # What was the median trading volume during this year.
# (Note: you may need to implement your own function for calculating the median.)

volume = data['Volume']
# print(volume)

# sort in increasing order
volume_sort = volume.sort_values( ascending=True)
print('The Median trading volume during this year is ',statistics.median(volume_sort))














