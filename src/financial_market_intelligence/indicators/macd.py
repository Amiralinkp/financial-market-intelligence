import pandas as pd
from financial_market_intelligence.indicators.ema import add_ema

def add_macd(data, fast_window=12, slow_window=26, signal_window=9):

    result = data.copy()

    result = add_ema(result, window=fast_window)
    result = add_ema(result, window=slow_window)

    result["MACD"] =  result[f"EMA_{fast_window}"] - result[f"EMA_{slow_window}"]

    result = add_ema(
    result, window=signal_window, source_column="MACD", output_column="MACD_SIGNAL")


    result["MACD_HISTOGRAM"] = result["MACD"] - result["MACD_SIGNAL"]

    return result

    


    