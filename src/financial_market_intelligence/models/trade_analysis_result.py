from dataclasses import dataclass


@dataclass
class TradeAnalysisResult:

    total_trades: int

    winning_trades: int

    losing_trades: int

    win_rate: float

    average_win: float

    average_loss: float

    largest_win: float

    largest_loss: float

    average_holding_bars: float

    breakeven_trades: int

    profit_factor: float

    payoff_ratio: float