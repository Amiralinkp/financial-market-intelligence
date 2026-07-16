import pandas as pd 
from financial_market_intelligence.strategies.moving_average import MovingAverageStrategy
from financial_market_intelligence.strategies.runner import run_strategy
from financial_market_intelligence.models.grid_search_result import GridSearchResult
from financial_market_intelligence.models.grid_search_entry import GridSearchEntry
from financial_market_intelligence.models.performance_metrics import PerformanceMetrics

def grid_search(symbols, strategies, start_date, end_date):
    

    result = []
    best_return = float("-inf")

    best_strategy = None
    best_symbol = None
    for symbol in symbols:
        for strategy in strategies:

            try:
                
                run_result = run_strategy(symbol, strategy, start_date, end_date)
                parameters = strategy.get_parameters()


                entry = GridSearchEntry(
                        symbol = symbol,
                        strategy_name = strategy.__class__.__name__ ,
                        parameters = parameters,
                        metrics = run_result.metrics)
                
                result.append(entry)

                if entry.metrics.total_return > best_return:

                    best_return = entry.metrics.total_return
                    best_strategy = strategy
                    best_symbol = entry.symbol

                

            except Exception as e :

                print(f"An error occurred for {symbol} : {e}")
                continue
    return GridSearchResult(
        results=result,
        best_strategy=best_strategy,
        best_symbol=best_symbol)
