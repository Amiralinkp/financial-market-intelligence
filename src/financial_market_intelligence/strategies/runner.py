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
from financial_market_intelligence.indicators import add_rsi



def run_strategy(symbol, strategy):
    
    provider = YahooProvider()

    raw_data = provider.get_historical_data( symbol=symbol,
        start_date="2025-01-01",
        end_date="2025-12-31")


    normalized_data = normalize_market_data(raw_data)

    validate_market_data(normalized_data)
    indicators = strategy.get_required_indicators()
    feature_data = apply_indicators(normalized_data, indicators)
          
    
    signal_data = strategy.generate_signal(feature_data)
    backtest_data = run_backtest(signal_data)
    metrics = calculate_performance_metrics(backtest_data)

    return metrics