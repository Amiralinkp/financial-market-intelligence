
import pandas as pd


STANDARD_COLUMNS = [
    "Open",
    "High",
    "Low",
    "Close",
    "Volume",
    ]

def normalize_market_data(data: pd.DataFrame):

    normalized = data.copy()

    if isinstance(normalized.columns, pd.MultiIndex):
        normalized.columns = normalized.columns.get_level_values(0)

    normalized = normalized[STANDARD_COLUMNS]

    normalized = normalized.reindex(columns=STANDARD_COLUMNS)
    normalized = normalized.sort_index()

    return normalized