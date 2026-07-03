from abc import ABC, abstractmethod

import pandas as pd

class MarketDataProvider(ABC):
    """Base interface for all market data providers."""

    @abstractmethod
    def get_historical_data(
        self,
        symbol: str,
        start_date: str,
        end_date: str,
    ) -> pd.DataFrame:
        """Fetch historical market data for a given symbol."""
        raise NotImplementedError
    

    