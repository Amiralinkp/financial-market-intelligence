from dataclasses import dataclass
import pandas as pd 


@dataclass
class Trade:
    

    trade_id: int

    entry_date: pd.Timestamp
    exit_date: pd.Timestamp

    entry_price: float
    exit_price: float

    direction: str

    trade_return: float