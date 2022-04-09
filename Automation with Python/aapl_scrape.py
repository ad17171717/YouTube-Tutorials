import yfinance as yf
from datetime import datetime
import pandas as pd

aapl = yf.Ticker('AAPL')
now = datetime.now()


df_existing = pd.read_excel('aapl.xlsx')

df = pd.DataFrame({'Apple Bid Price':[aapl.info['bid']],
                    'Apple Ask Price':[aapl.info['ask']],
                    'Date and Time':[now.strftime("%m/%d/%Y %H:%M:%S")]})

pd.concat([df_existing,df],ignore_index=True).to_excel('aapl.xlsx', index=False)
