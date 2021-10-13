import numpy as np
import yfinance as yf
import pandas as pd
import datetime as dt





def historical_data(stockName, timeFrame, fromDate, toDate):

    if timeFrame == "day":
        fromDate = dt.date.fromisoformat(fromDate)
        sliceDate = str(fromDate -  dt.timedelta(days=60))
        data = yf.download(tickers = stockName, period = "ytd", interval = "1d",  start= sliceDate, end= toDate, group_by = 'ticker', auto_adjust = True, prepost = True, threads = True,proxy = None)
        data = data.reset_index()
        data.columns = ["dtime", "open", "high", "low", "close", "volume"]
        df = pd.DataFrame(data)
        df.set_index("dtime", inplace=True)
        return df
    



def atr(DF, n):
    df = DF.copy()
    df['H-L'] = abs(df['high'] - df['low'])
    df['H-PC'] = abs(df['high'] - df['close'].shift(1))
    df['L-PC'] = abs(df['low'] - df['close'].shift(1))
    df['TR'] = df[['H-L', 'H-PC', 'L-PC']].max(axis=1, skipna=False)
    df['ATR'] = df['TR'].ewm(com=n, min_periods=n).mean()
    df['ATR'] = df['ATR'].fillna(0)
    return df




def volatility_measure(df):
    # Compute the logarithmic returns using the Closing price 
    df['Volatility'] = round(abs(df["open"] - df["close"]),2)
    return df
    
