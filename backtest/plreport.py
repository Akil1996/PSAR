from .commanfun import historical_data, atr, volatility_measure
import talib

def psar_profitloss_strategy(df, fund):
    signal = None
    ePrice = 0
    etime = ""
    result = []
    for index, row in df.iterrows():
        # print(index,row.close, row.SAR)
        if 0 < row.SAR and signal == None:
            quantity = round(fund/row.close)
            ePrice = row.close
            etime = index
            result.append({"entryTime": index, "exitTime": "", "entryPrice": row.close, "exitPrice": "", "high": "", "low": "","indVolatility": row.ATR, "volatility": row.Volatility, "signal": "BUY",  "profit": " ", "profitPercentage": ""})
            signal = "BUY"
        if 0 > row.SAR and signal == "BUY":
            sDf = df.loc[etime : index]
            dfHigh = sDf["high"].max()
            dfLow = sDf["high"].min()
            exPrice = row.close - ePrice 
            result.append({"entryTime": "", "exitTime": index, "entryPrice": "", "exitPrice": row.close, "high": dfHigh, "low": dfLow,"indVolatility": row.ATR, "volatility": row.Volatility, "signal": "SELL",  "profit": exPrice, "profitPercentage": str(round(((exPrice/row.close)*100),2)) + " %"})
            signal = None
    return result

    

def plreport_main(stockName, psarStart, psarIncrement, psarMaxvalue, timeFrame, fromDate, toDate, fund):
    psarStart = float(psarStart)
    psarIncrement = float(psarIncrement)
    psarMaxvalue = float(psarMaxvalue)
    df = historical_data(stockName, timeFrame, fromDate, toDate)
    df["SAR"] = talib.SAREXT(df.high, df.low, startvalue=0.05, offsetonreverse=0, accelerationinitlong=0.05, accelerationlong=0.02,
           accelerationmaxlong=0.5, accelerationinitshort=0.05, accelerationshort=0.02, accelerationmaxshort=0.5)
    # df['SAR'] = talib.SAR(df.high, df.low, psarIncrement, psarMaxvalue)
    df = atr(df, 14)
    df = volatility_measure(df)
    df = df.loc[fromDate:toDate]
    df = psar_profitloss_strategy(df, fund)
    return df
