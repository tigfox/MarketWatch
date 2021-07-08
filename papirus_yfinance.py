#!/usr/bin/env python3

import yfinance as yf
try:
    from papirus import PapirusTextPos
    display = True
except ImportError:
    display = False

ticker1 = { "name" : "ETSY" }
ticker2 = { "name" : "BBVA" }
ticker3 = { "name" : "AAPL" }
tickers = [ticker1, ticker2, ticker3]

def get_current_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0]

def write_display(tickers):
    text = PapirusTextPos(False)
    pos = 10
    for ticker in tickers:
        text.AddText(ticker['name'] + ": " + str(ticker['price']), 10, pos)
        pos = pos + 25
    text.WriteAll()

if __name__ == "__main__":
    for ticker in tickers:
        ticker['price'] = round(get_current_price(ticker['name']), 2)

    if display:
        write_display(tickers)
    else:
        for ticker in tickers:
            print(ticker['name'] + ": " + str(ticker['price']))

