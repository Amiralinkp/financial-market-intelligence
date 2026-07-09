import pandas as pd 

def rsi_signal(data, over_sold, over_bought, rsi_column):
    
    result = data.copy()
    result["Signal"] = 0 

    buy_signal = over_sold > result[rsi_column]


    result.loc[buy_signal, "Signal"] = 1

    sell_signal = over_bought < result[rsi_column]

    result.loc[sell_signal, "Signal"] = -1

    result["Position"] = pd.NA

    result.loc[result["Signal"] == 1, ["Position"]] = 1
    result.loc[result["Signal"] == -1, ["Position"]] = 0

    result["Position"] = result["Position"].ffill()
    result["Position"] = result["Position"].fillna(0)
    result["Position"] = result["Position"].astype(int)

    return result 