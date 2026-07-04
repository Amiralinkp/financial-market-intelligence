#import pandas as pd 


def calculate_performance_metrics(data):

    result = data.copy()
    final_equity = result["Cumulative_Return"].iloc[-1]
    total_return = (final_equity - 1) * 100 
    signal_count = len(result[result["Signal"] != 0])
    running_peak = result["Cumulative_Return"].cummax()
    drawdown = ( result["Cumulative_Return"] - running_peak ) / running_peak
    max_drawdown = drawdown.min()


    return { "final_equity" : final_equity,
            "total_return" : total_return,
            "signal_count" : signal_count,
            "max_drawdown" : max_drawdown

    }