import pandas as pd 
from financial_market_intelligence.strategies.moving_average import MovingAverageStrategy
from financial_market_intelligence.strategies.runner import run_strategy


def grid_search(symbols, strategies):
    
    result = []
    for symbol in symbols:
        for strategy in strategies:

            # try:
                metrics = run_strategy(symbol, strategy)
                metrics["symbol"] = symbol
                parameters = strategy.get_parameters()

                metrics.update(parameters)
                result.append(metrics)

                

            # except Exception as e :

                # print(f"An error occurred for {symbol} : {e}")
                # continue
    return result
