import pandas as pd
def report_generation_main(pl_dic, fund, fromDate, toDate):
    df = pd.DataFrame(pl_dic)
    indVolatility = df["indVolatility"].to_list()
    volatility = df["volatility"].to_list()
    dateLis = df["exitTime"].to_list()
    pos_df = df.loc[df['profit'] >= 0]
    neg_df = df.loc[df['profit'] <= 0]
    timePeriod = str(fromDate) + " / "+ str(toDate)
    initialCapital = fund
    endingCaptial = round(fund + df["profit"].sum()) 
    netProfit = round(df["profit"].sum(), 2)
    netProfitPercentage = round(((netProfit / initialCapital) * 100),1) 
    exposure = 0
    # avgProfitLoss = round(df["profit"].sum() / len(df["profit"]), 2)
    # avgProfitLossPercentage = ((round(df["profit"].sum() / len(df["profit"]), 2))/initialCapital) * 100
    # avgProfit = round(pos_df["profit"].sum() / len(pos_df["profit"]), 2)
    # avgProfitPercentage = ((round(pos_df["profit"].sum() / len(pos_df["profit"]), 2))/initialCapital) * 100
    avgProfitLoss = 0
    avgProfitLossPercentage = 0
    avgProfit = 0
    avgProfitPercentage = 0
    pos_df = df.loc[df['profit'] >= 0]
    neg_df = df.loc[df['profit'] <= 0]
    number_of_positive_trades = (len(pos_df))
    number_of_negative_trades = (len(neg_df))
    number_of_total_trades = (len(pos_df)) + (len(neg_df))
    max_profit_in_one_trade = round(pos_df["profit"].max() , 1)
    max_loss_in_one_trade = round(neg_df["profit"].min() , 1)
    pandl_of_total_positive_trade = round(pos_df["profit"].sum() , 1)
    pandl_of_total_negative_trade = round(neg_df["profit"].sum() , 1)
    pandl_of_total_trades = round(pandl_of_total_positive_trade + pandl_of_total_negative_trade, 1)
    strike_rate = round(len(pos_df) / number_of_total_trades * 100, 1)
    report_dic = {"initialCapital": initialCapital, "endingCaptial": endingCaptial, "netProfit": netProfit,
                         "netProfitPercentage": netProfitPercentage,"exposure": exposure, "avgProfitLoss": avgProfitLoss,
                         "avgProfitLossPercentage": avgProfitLossPercentage, "avgProfit": avgProfit, "avgProfitPercentage": avgProfitPercentage,
                         "number_of_positive_trades": number_of_positive_trades, "number_of_negative_trades": number_of_negative_trades,
                          "number_of_total_trades": number_of_total_trades, "max_profit_in_one_trade": max_profit_in_one_trade,
                          "max_loss_in_one_trade":max_loss_in_one_trade, "pandl_of_total_trades": pandl_of_total_trades,
                          "pandl_of_total_positive_trade": pandl_of_total_positive_trade, "pandl_of_total_negative_trade": pandl_of_total_negative_trade,
                          "strike_rate": strike_rate, "timePeriod": timePeriod, "indVolatility": indVolatility, "volatility": volatility, "dateLis": dateLis
                          }
    return report_dic