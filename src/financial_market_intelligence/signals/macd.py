import pandas as pd


def macd_signal(data):
    result = data.copy()
    result["Signal"] = 0 


    buy_signal = (result["MACD"] > result["MACD_SIGNAL"])&(
         result["MACD"].shift(1) <= result["MACD_SIGNAL"].shift(1))
    

    result.loc[buy_signal, "Signal"] = 1

    sell_signal = (result["MACD"] < result["MACD_SIGNAL"])&(
         result["MACD"].shift(1) >= result["MACD_SIGNAL"].shift(1))


    result.loc[sell_signal, "Signal"] = -1

    result["Position"] = pd.NA

    result.loc[result["Signal"] == 1, ["Position"]] = 1
    result.loc[result["Signal"] == -1, ["Position"]] = 0

    result["Position"] = result["Position"].ffill()
    result["Position"] = result["Position"].fillna(0)
    result["Position"] = result["Position"].astype(int)

    return result 