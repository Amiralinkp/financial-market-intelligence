from financial_market_intelligence.data.providers.yahoo import YahooProvider
from financial_market_intelligence.data.processing.normalizer import normalize_market_data
from financial_market_intelligence.data.processing.validator import validate_market_data
from financial_market_intelligence.features.returns import add_simple_return


def main():

    provider = YahooProvider()

    raw_data = provider.get_historical_data( symbol="NVDA",
        start_date="2025-01-01",
        end_date="2025-12-31")


    normalize_data = normalize_market_data(raw_data)

    validate_market_data(normalize_data)

    feature_data = add_simple_return(normalize_data)

    print(normalize_data.head())
    print()
    print(feature_data.head())

if __name__ == "__main__" : 
    main()