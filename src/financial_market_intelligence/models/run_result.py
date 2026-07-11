from dataclasses import dataclass
from financial_market_intelligence.models.execution_result import ExecutionResult

@dataclass
class RunResult:
    
    execution_result: ExecutionResult

    feature_data: object
    signal_data: object
    backtest_data: object
    metrics: object