#import pandas as pd 
from financial_market_intelligence.models.performance_metrics import PerformanceMetrics


def calculate_performance_metrics(data):

    result = data.copy()
    final_equity = result["Cumulative_Return"].iloc[-1]
    total_return = (final_equity - 1) * 100 
    signal_count = len(result[result["Signal"] != 0])
    running_peak = result["Cumulative_Return"].cummax()
    drawdown = ( result["Cumulative_Return"] - running_peak ) / running_peak
    max_drawdown = drawdown.min()
    daily_returns = result["Strategy_Return"]
    annualized_volatility = daily_returns.std() * (252 ** 0.5)

    if daily_returns.std() == 0:
        sharpe_ratio = 0
    else:
        sharpe_ratio = (daily_returns.mean() / daily_returns.std()) * (252 ** 0.5)

    years = len(result) / 252
    cagr = (final_equity ** (1 / years)) - 1

    return PerformanceMetrics(

        final_equity = final_equity,

        total_return = total_return,

        signal_count = signal_count,

        max_drawdown = max_drawdown,

        sharpe_ratio=sharpe_ratio,

        annualized_volatility=annualized_volatility,
        
        cagr=cagr)

