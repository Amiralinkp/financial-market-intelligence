from dataclasses import dataclass

from financial_market_intelligence.models.performance_metrics import PerformanceMetrics


@dataclass
class GridSearchEntry:

    symbol: str

    strategy_name: str

    parameters: dict

    metrics: PerformanceMetrics

    def to_dict(self):
        return {
            "symbol": self.symbol,
            "strategy_name": self.strategy_name,

            **self.parameters,

            "total_return": self.metrics.total_return,
            "max_drawdown": self.metrics.max_drawdown,
            "signal_count": self.metrics.signal_count,
            "final_equity": self.metrics.final_equity}