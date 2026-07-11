from financial_market_intelligence.models.execution_result import ExecutionResult


def run_backtest(execution_result: ExecutionResult):

    result = execution_result.data.copy()

    result["Strategy_Return"] = (
        result["Return"] * result["Position"])

    result["Cumulative_Return"] = (1 + result["Strategy_Return"]).cumprod()

    result["Peak"] = (result["Cumulative_Return"]).cummax()

    result["Drawdown"] = (
        result["Cumulative_Return"]
        / result["Peak"]) - 1

    return result