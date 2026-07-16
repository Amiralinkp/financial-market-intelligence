from dataclasses import dataclass
from financial_market_intelligence.models.execution_result import ExecutionResult
from financial_market_intelligence.models.trade_analysis_result import TradeAnalysisResult
from financial_market_intelligence.models.performance_metrics import PerformanceMetrics


@dataclass
class RunResult:
    
    execution_result: ExecutionResult
    symbol: str
    strategy_name: str
    start_date: str
    end_date: str
    feature_data: object
    signal_data: object
    backtest_data: object
    metrics: PerformanceMetrics
    trade_analysis_result: TradeAnalysisResult