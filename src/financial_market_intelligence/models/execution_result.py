from dataclasses import dataclass

import pandas as pd

from financial_market_intelligence.models.trade import Trade


@dataclass
class ExecutionResult:

    data: pd.DataFrame

    trades: list[Trade]