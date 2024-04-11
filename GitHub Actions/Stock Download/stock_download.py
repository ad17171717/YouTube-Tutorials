from datetime import datetime
import yfinance as yf
import pandas as pd
from pytz import timezone

if __name__ == '__main__':

    #read the csv into a pandas DataFrame
    df = pd.read_csv('/content/aapl_data.csv')

    #set the yfinance Ticker module to download Apple's stock data
    stock = yf.Ticker('AAPL')
    #retrieve the most recent stock price
    prices = stock.history(period='1d')
    #set the timezone to US Eastern
    tz = timezone('US/Eastern')

    #create a new pandas DataFrame with the most recent price
    #for Apple and the current date/time
    update_df = pd.DataFrame({'AAPL Price':[prices['Close'][0]],
                            'Date and Time':[datetime.now(tz).strftime("%m/%d/%Y %H:%M:%S")]})

    #combine the existing data with the new data
    df = pd.concat([df, update_df], ignore_index=True)
    #write the full data to a csv file
    df.to_csv('aapl_data.csv',index=False)