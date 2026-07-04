import pandas as pd 



def add_sma(data: pd.DataFrame, window: int):

    result = data.copy()

    result[f"SMA_{window}"] = (
        result["Close"].rolling(window=window).
        mean()
    )

    return result