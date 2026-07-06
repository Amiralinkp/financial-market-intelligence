import pandas as pd
import yfinance as yf

from financial_market_intelligence.data.interfaces.market_data_provider import MarketDataProvider

class YahooProvider(MarketDataProvider):
    """Market data provider backed by Yahoo Finance."""

    def get_historical_data(
        self,
        symbol: str,
        start_date: str,
        end_date: str,
    ) -> pd.DataFrame:
        """Fetch historical market data from Yahoo Finance."""

        data = yf.download(
            tickers=symbol,
            start=start_date,
            end=end_date,
            progress=False,
        )

        if data.empty:
            raise ValueError(f"No market data found for symbol '{symbol}'.")

        return data