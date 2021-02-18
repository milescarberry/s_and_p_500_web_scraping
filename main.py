import bs4 as bs               # This module will be used for web scraping.

import requests                 # This module is part of the core python stack.

import pickle

import pandas_datareader as web


import datetime as dt




html = requests.get("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")



# "html" here is a requests.models.Response object        (we got a response for the html request)

# "html" is a Response object. It contains the "response" for the html request.


soup = bs.BeautifulSoup(html.text)          # We have created a BeautifulSoup object here belonging to the bs4 module.



# "soup" here is a BeautifulSoup object.  (We have passed in the html code (in text form) as an "attribute" while creating the BeautifulSoup object.)



ticker_symbols = []




table = soup.find('table', {"class" : "wikitable sortable"})           # find the first occurring of 'table' element with class = "wikitable sortable" in the html code.





table_rows = table.findAll('tr')[1::1]              # find all the "table rows" of the table and ignore the 0th row (the table header).



# "table_rows" here is a "list" object.




for table_row in table_rows:


    ticker_symbol = table_row.findAll("td")[0].text

    ticker_symbols.append(ticker_symbol[0:len(ticker_symbol)-1:1])







with open("s_and_p_500.pickle", "rb") as file:

    ticker_symbols = pickle.load(file)




start = dt.datetime(2020,1,1)

end = dt.datetime.now()


data = web.DataReader(ticker_symbols[0], "yahoo", start, end)



print()



print(data)
