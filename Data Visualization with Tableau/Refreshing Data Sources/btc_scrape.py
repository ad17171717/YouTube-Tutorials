import yfinance as yf
import pandas as pd
from datetime import datetime

#read in existing DataFrame
df_existing = pd.read_excel('btc.xlsx')

'''download Bitcoin-USD conversion rate and save the time/date
when it was scraped and read it into a DataFrame'''
time = datetime.now()
df = pd.DataFrame({'BTC Last Price Price':yf.Ticker('BTC-USD').history(period='1d')['Close'][0],
                   'Date':[time.strftime('%m/%d/%Y')],
                   'Hour':[time.strftime('%H')],
                    'Hour':[time.strftime('%H')],
                    'Minute':[time.strftime('%M')],
                    'Second':[time.strftime('%S')]})

#combine the existing with the latest data and export to excel
pd.concat([df_existing,df],ignore_index=True).to_excel('btc.xlsx', index=False)