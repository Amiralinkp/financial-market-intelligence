import pandas as pd 

def add_ema(data, window, source_column="Close", output_column=None):

    result = data.copy()
    if output_column is None:
        output_column = f"EMA_{window}"

    result[output_column] = (
    result[source_column].ewm(span=window, adjust=False).mean())

    return result 
