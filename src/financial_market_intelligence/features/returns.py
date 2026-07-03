import pandas as pd

def add_simple_return(data: pd.DataFrame):

    resault = data.copy()
    resault["Return"] = resault["Close"].pct_change()
    return resault