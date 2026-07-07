import pandas as pd


def add_rsi(data, window = 14):
    
    result = data.copy()
    delta = data["Close"].diff()

    gain = delta.clip(lower = 0)
    loss = -delta.clip(upper = 0)
    avg_gain = gain.rolling(window).mean()
    avg_loss = loss.rolling(window).mean()
    rs = avg_gain/avg_loss
    rsi = 100 - (100 /( 1 + rs))
    result[f"RSI_{window}"] = rsi 

    return result
