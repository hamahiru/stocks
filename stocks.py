import csv
import urllib2

stocks = []
url = 'http://finance.yahoo.com/d/quotes.csv?s=AAPL+GOOG+GOOGL+MDT+YNDX+QIWI+BIIB+GILD+CBI+NKE+F+FISV&f=nl1kj'
stock_info = [['AAPL',17,102.42],['GOOG',3,198],['GOOGL',7,198],['MDT',65,30.725],['YNDX',90,15.53],['QIWI',65,21.94],['BIIB',4,295.22],['GILD',22,96.465],['CBI',60,39.22],['NKE',20,63.14],['F',175,12.28],['FISV',15,88.01]]
response = urllib2.urlopen(url)
csvreader = csv.reader(response)
stocksinternet=list(csvreader)
for stock1, stock2 in zip(stock_info, stocksinternet):
    stocks.append(stock1+stock2)
print stocks


for stock in stocks:
    buy_price = stock[1] * float(stock[2])
    price_now = stock[1] * float(stock[4])
    profit = price_now - buy_price
    print (stock[0] + ": " +  str(profit))
