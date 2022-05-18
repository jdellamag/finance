#Data Source
import imp
import yfinance as yf

msft = yf.Ticker("MSFT")

# get stock info
msft.info

# print all stock info
# print(msft.info)

# get historical market data
hist = msft.history(period="max")
# print(hist)

# variables
stock = input("What stock ticker do you want to look at?  ")
days = int(input("How many days back do you want to look  "))
freq = int(input("How many hours apart should numbers be pulled?  "))

today = 




print("\nStock: ", stock, "\n")
print("Today's Close: ", days, "\n")