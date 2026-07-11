from dataclasses import dataclass


@dataclass
class TradeStatistics:

    total_trades: int

    winning_trades: int

    losing_trades: int

    win_rate: float

    average_trade: float

    best_trade: float

    worst_trade: float

    profit_factor: float