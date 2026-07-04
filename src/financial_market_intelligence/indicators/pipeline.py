import pandas as pd
from financial_market_intelligence.indicators.base import Indicator


def apply_indicators(data: pd.DataFrame, indicators: list[Indicator]):
    """
    Apply a sequence of indicators to market data.
    """
    result = data

    for indicator in indicators:
        result = indicator(result)

    return result

    