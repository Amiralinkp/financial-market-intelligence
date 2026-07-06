import pandas as pd
from financial_market_intelligence.data.providers.yahoo import YahooProvider
from financial_market_intelligence.data.processing.normalizer import normalize_market_data
from financial_market_intelligence.data.processing.validator import validate_market_data
from financial_market_intelligence.features.returns import add_simple_return
from financial_market_intelligence.indicators.sma import add_sma
from financial_market_intelligence.indicators.pipeline import apply_indicators
from financial_market_intelligence.indicators.ema import add_ema
from financial_market_intelligence.backtesting.simple_backtester import run_backtest
from financial_market_intelligence.backtesting.metrics import calculate_performance_metrics
from financial_market_intelligence.strategies.moving_average import MovingAverageStrategy

def run_strategy(symbol, strategy):
    
    provider = YahooProvider()

    raw_data = provider.get_historical_data( symbol=symbol,
        start_date="2025-01-01",
        end_date="2025-12-31")


    normalized_data = normalize_market_data(raw_data)

    validate_market_data(normalized_data)

    feature_data = apply_indicators(
        normalized_data,
          [add_simple_return,
           lambda data: add_sma(data, window=strategy.slow_window),
           lambda data: add_ema(data, window=strategy.fast_window),
           ])
    
    signal_data = strategy.generate_signal(feature_data)
    backtest_data = run_backtest(signal_data)
    metrics = calculate_performance_metrics(backtest_data)

    return metrics






def main():

    symbols = [
    "NVDA",
    "AAPL",
    "MSFT",
    "GOOG",
    "META",]

    

    ema_windows = [20,30,50]
    sma_windows = [20,30,50]


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
                    


    # best_asset = (max(result, key=lambda x:x["total_return"]))
    # worst_asset = (min(result, key=lambda x:x["total_return"]))

    df = pd.DataFrame(result)

    result_df = df[[
        "symbol",
        "ema_window",
        "sma_window",
        "total_return",
        "max_drawdown",
        "signal_count",
        "final_equity"]]

    result_df = result_df.sort_values(by="total_return", ascending=False)
    result_df["rank"] = result_df["total_return"].rank(ascending=False, method="dense").astype(int)
    result_df.to_csv("reports/strategy_results.csv", index=False)


if __name__ == "__main__" : 
    main()