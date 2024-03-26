#Author: Adrian Dolinay
#Description: Python script that retrieves components of the S&P 500 from a 
#Wikipedia page, saves it to a pandas DataFrame then exports stock data from
#a ticker input by the user running the script to a CSV file.

import yfinance as yf
import pandas as pd

if __name__ == '__main__':

    #read in the data into a pandas DataFrame
    df = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]

    #create and display tickers and company names for the S&P 500
    ticker_dict = {ticker: company for ticker, company in zip(df['Symbol'].values, df['Security'].values)}
    print(ticker_dict)

    #prompt a user to input a ticker
    company_ticker = input('Please Choose a Ticker to Download Data\n')

    #download the data with yfinance into a pandas DataFrame then export the data into a csv
    data_df = yf.download(f'{company_ticker}', period='1y')
    data_df.to_csv(f'/data/{company_ticker}_data.csv')