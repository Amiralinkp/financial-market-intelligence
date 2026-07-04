import pandas as pd 


def moving_average_crossover_signal(data, fast_column, slow_column):

    result = data.copy()
    result["Signal"] = 0

    buy_signal = (result[fast_column] > result[slow_column])&(
        result[fast_column].shift(1) <= result[slow_column].shift(1))


    result.loc[buy_signal, "Signal"] = 1

    sell_signal = (result[fast_column] < result[slow_column])&(
        result[fast_column].shift(1) >= result[slow_column].shift(1))
    
    result.loc[sell_signal, "Signal"] = -1

    result["Position"] = pd.NA

    result.loc[result["Signal"] == 1, ["Position"]] = 1
    result.loc[result["Signal"] == -1, ["Position"]] = 0

    result["Position"] = result["Position"].ffill()
    result["Position"] = result["Position"].fillna(0)
    result["Position"] = result["Position"].astype(int)


    return result