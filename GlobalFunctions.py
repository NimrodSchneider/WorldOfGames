import requests
import sys


def delete_last_line():
    # Use this function to delete the last line in the STDOUT
    #cursor up one line
    sys.stdout.write('\x1b[1A')

    #delete last line
    sys.stdout.write('\x1b[2K')
# Python program to get the real-time
# currency exchange rate


# Function to get real time currency exchange
def real_time_currency_exchange_rate(from_currency, to_currency, api_key):
    # importing required libraries
    global main_url

    # base_url variable store base url
    base_url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"

    # main_url variable store complete url
    main_url = base_url + "&from_currency=" + from_currency + "&to_currency=" + to_currency + "&apikey=" + api_key

    # get method of requests module
    # return response object
    req_ob = requests.get(main_url)

    # json method return json format
    # data into python dictionary data type.

    # result contains list of nested dictionaries
    result = req_ob.json()

    return result["Realtime Currency Exchange Rate"]['5. Exchange Rate']


def get_currency():
    # currency code
    from_currency = "USD"
    to_currency = "ILS"

    # enter your api key here
    api_key = "REKDR8MZC5J20MUJ"

    # Getting Rate
    rate = float((real_time_currency_exchange_rate(from_currency, to_currency, api_key)))

    return round(rate, 2)


