import bs4 as bs

import requests       # This module is part of the core Python stack.

import pandas_datareader as web

import datetime as dt

import mplfinance as mpf

import matplotlib.pyplot as plt


import pickle




html = requests.get("https://www.shell.in/motorists/shell-fuels/fuel-pricing-in-india.html")


# Now, "html" here is requests.Response object.


#print()

#print(html.text)               # Calling the "text" attribute of the requests.Response object "html".



soup = bs.BeautifulSoup(html.text)          # We have created a BeautifulSoup object based on the "html data" we have just provided (as an argument).




table = soup.findAll('table')[0]




table_rows = table.findAll('tr')[1::1]


diesel_rates = []

petrol_rates = []

metros = []




for row in table_rows:

    metro = row.findAll('td')[0].text

    metros.append(metro)



    diesel_rate = row.findAll('td')[1].text

    diesel_rates.append(diesel_rate)



    petrol_rate = row.findAll('td')[3].text

    petrol_rates.append(petrol_rate)





with open("fuel_rates.pickle", "wb") as file:

    pickle.dump((metros, petrol_rates, diesel_rates), file)




with open("fuel_rates.pickle", "rb") as f:

    metros, petrol_rates, diesel_rates = pickle.load(f)





print()

print(metros)


print()


print(petrol_rates)


print()


print(diesel_rates)
