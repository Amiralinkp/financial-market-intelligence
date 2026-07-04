#import pandas as pd

def run_backtest(data):
    
    result = data.copy()
    result["Strategy_Return"] = result["Return"] * result["Position"]

    result["Cumulative_Return"] = (
        (1 + result["Strategy_Return"]).cumprod())

    return result