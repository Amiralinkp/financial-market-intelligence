import pandas as pd 
from financial_market_intelligence.strategies.moving_average import MovingAverageStrategy
from financial_market_intelligence.strategies.runner import run_strategy
from financial_market_intelligence.models.grid_search_result import GridSearchResult

def grid_search(symbols, strategies):
    

    result = []
    best_return = float("-inf")

    best_strategy = None
    best_symbol = None
    for symbol in symbols:
        for strategy in strategies:

            try:
                run_result = run_strategy(symbol, strategy)
                metrics = run_result.metrics.copy()
                
                metrics["symbol"] = symbol

                parameters = strategy.get_parameters()
                metrics.update(parameters)

                result.append(metrics)
                if metrics["total_return"] > best_return:

                    best_return = metrics["total_return"]
                    best_strategy = strategy
                    best_symbol = symbol

                

            except Exception as e :

                print(f"An error occurred for {symbol} : {e}")
                continue
    return GridSearchResult(
        results=result,
        best_strategy=best_strategy,
        best_symbol=best_symbol)
