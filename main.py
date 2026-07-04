from financial_market_intelligence.data.providers.yahoo import YahooProvider
from financial_market_intelligence.data.processing.normalizer import normalize_market_data
from financial_market_intelligence.data.processing.validator import validate_market_data
from financial_market_intelligence.features.returns import add_simple_return
from financial_market_intelligence.indicators.sma import add_sma
from financial_market_intelligence.indicators.pipeline import apply_indicators


def main():

    provider = YahooProvider()

    raw_data = provider.get_historical_data( symbol="NVDA",
        start_date="2025-01-01",
        end_date="2025-12-31")


    normalize_data = normalize_market_data(raw_data)

    validate_market_data(normalize_data)

    feature_data = apply_indicators(
        normalize_data,
          [add_simple_return,
           lambda data: add_sma(data, window=20)])

    print(normalize_data.head())
    print()
    print(feature_data.head(25))

if __name__ == "__main__" : 
    main()