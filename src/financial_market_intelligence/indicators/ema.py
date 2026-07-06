import pandas as pd 

def add_ema(data, window):

    result = data.copy()
    result[f"EMA_{window}"] = (
        result["Close"].ewm(span=window, adjust = False)
        .mean()
    )

    return result 
