
import pandas as pd

REQUIRED_COLUMNS = {
    "Open",
    "High",
    "Low",
    "Close",
    "Volume"}


def validate_market_data(data:pd.DataFrame):

    missing_columns = REQUIRED_COLUMNS - set(data.columns)

    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise ValueError(f"Missing required columns: {missing}")