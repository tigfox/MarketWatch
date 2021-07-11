# MarketWatch
Raspberry Pi E-Ink Stock Ticker

Uses a PapiRus E-Ink display: https://www.adafruit.com/product/3335  
On a Raspberry Pi Zero W: https://www.adafruit.com/product/3708  
You'll need the PaPiRus libraries: https://github.com/PiSupply/PaPiRus  
And either an AlphaVantage account: https://www.alphavantage.co/support/#api-key  
Or (recommended) the yfinance python library: https://github.com/ranaroussi/yfinance  
To use yfinance, it'll need to install pandas, numpy, etc. I had to install some  
additional libraries: https://numpy.org/devdocs/user/troubleshooting-importerror.html#raspberry-pi  

Then you can run the script on a cron to update the display.  
That's it.
