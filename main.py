from financial_market_intelligence.data.providers.yahoo import YahooProvider
from financial_market_intelligence.data.processing.normalizer import normalize_market_data
from financial_market_intelligence.data.processing.validator import validate_market_data
from financial_market_intelligence.features.returns import add_simple_return
from financial_market_intelligence.indicators.sma import add_sma
from financial_market_intelligence.indicators.pipeline import apply_indicators
from financial_market_intelligence.indicators.ema import add_ema
from financial_market_intelligence.signals.crossover import moving_average_crossover_signal
from financial_market_intelligence.backtesting.simple_backtester import run_backtest
from financial_market_intelligence.backtesting.metrics import calculate_performance_metrics


def run_strategy(symbol):

    provider = YahooProvider()

    raw_data = provider.get_historical_data( symbol=symbol,
        start_date="2025-01-01",
        end_date="2025-12-31")


    normalized_data = normalize_market_data(raw_data)

    validate_market_data(normalized_data)

    feature_data = apply_indicators(
        normalized_data,
          [add_simple_return,
           lambda data: add_sma(data, window=20),
           lambda data: add_ema(data, window=20),
           ])
    
    signal_data = moving_average_crossover_signal(feature_data, fast_column = "EMA_20", slow_column = "SMA_20")
    backtest_data = run_backtest(signal_data)
    metrics = calculate_performance_metrics(backtest_data)

    return metrics






def main():

    metrics = run_strategy("NVDA")

    

    
    print(f"Strategy Performance")
    print("====================")
    print(f"Final Equity : {metrics['final_equity']:.2f}")
    print(f"Total Return : {metrics['total_return']:.2f}%")
    print(f"Signal Count : {metrics['signal_count']}")
    print(f"Max Drawdown : {metrics['max_drawdown']:.2%}")




    
if __name__ == "__main__" : 
    main()