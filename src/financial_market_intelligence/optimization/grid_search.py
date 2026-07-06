import pandas as pd 
from financial_market_intelligence.strategies.moving_average import MovingAverageStrategy
from financial_market_intelligence.strategies.runner import run_strategy


def grid_search(symbols, ema_windows, sma_windows):
    
    result = []
    for symbol in symbols:

        for ema in ema_windows :
        
            for sma in sma_windows :
                strategy = MovingAverageStrategy(
                fast_window= ema,
                slow_window= sma)
        
                try:
                    metrics = run_strategy(symbol, strategy)
                    metrics["symbol"] = symbol
                    metrics["ema_window"] = ema
                    metrics["sma_window"] = sma
                    result.append(metrics)

                    

                except Exception as e :

                    print(f"An error occurred for {symbol} : {e}")
                    continue
    return result
