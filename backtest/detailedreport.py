from .commanfun import historical_data
from .commanfun import atr, volatility_measure
import talib


def psar_strategy(df):
    signalStatus = ""
    result_dic = []
    for index, row in df.iterrows():
        if row.close > row.SAR:
            result_dic.append({"dtime": index, "open": round(row.open, 2), "high": round(row.high,2), "low": round(row.low, 2), "close": round(row.close,2), "psarValue": round(row.SAR, 2), "indVolatility": row.ATR, "volatility": row.Volatility, "signal": "BUY"})
        if row.close < row.SAR:
            result_dic.append({"dtime": index, "open": round(row.open, 2), "high": round(row.high,2), "low": round(row.low, 2), "close": round(row.close,2), "psarValue": round(row.SAR, 2), "indVolatility": row.ATR, "volatility": row.Volatility, "signal": "SELL"})
    return result_dic


def dreport_main(stockName, psarStart, psarIncrement, psarMaxvalue, timeFrame, fromDate, toDate):
    print(psarIncrement, psarMaxvalue)
    df = historical_data(stockName, timeFrame, fromDate, toDate)
    df['SAR'] = talib.SAR(df.high, df.low, psarIncrement, psarMaxvalue)
    # a = addSAR(df)
    # print(a)
    df = atr(df, 14)
    df = volatility_measure(df)
    df = df.loc[fromDate:toDate]
    result_df = psar_strategy(df)
    return result_df
