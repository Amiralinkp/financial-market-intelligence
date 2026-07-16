import pandas as pd
import matplotlib.pyplot as plt
from financial_market_intelligence.optimization.grid_search import grid_search
from financial_market_intelligence.optimization.strategy_builder import build_moving_average_strategies , build_rsi_strategies, build_macd_strategies
from financial_market_intelligence.visualization.equity_curve import plot_equity_curve
from financial_market_intelligence.strategies.runner import run_strategy
from financial_market_intelligence.visualization.drawdown_curve import plot_drawdown_curve
from financial_market_intelligence.reporting.report_generator import generate_report


start_date = "2025-01-01"
end_date = "2025-12-31"

def main():
    symbols = [
    "NVDA",
    "AAPL",
    "MSFT",
    "GOOG",
    "META",]
    strategy_type = "macd"

    ema_windows = [20, 30, 50]
    sma_windows = [20, 30, 50]

    if strategy_type == "ma":
        strategies = build_moving_average_strategies(
            ema_windows,
            sma_windows)

    elif strategy_type == "rsi":
        strategies = build_rsi_strategies(
            windows=[14])

    elif strategy_type == "macd":
        strategies = build_macd_strategies()

    else:
        raise ValueError(f"Unknown strategy type: {strategy_type}")
        

   
    grid_result = grid_search(symbols, strategies, start_date, end_date)
    best_strategy = grid_result.best_strategy
    best_symbol = grid_result.best_symbol


    run_result = run_strategy(
        best_symbol, best_strategy, start_date, end_date)
    report = generate_report(run_result)

    print(report)
    
    fig = plot_equity_curve(
    run_result.backtest_data,
    title=f"{best_symbol} - Equity Curve")

    drawdown_fig = plot_drawdown_curve(
    run_result.backtest_data,
    title=f"{best_symbol} - Drawdown Curve")
    
    fig.savefig("reports/plots/equity_curve.png", dpi=300)

    drawdown_fig.savefig("reports/plots/drawdown_curve.png", dpi=300)



    df = pd.DataFrame([entry.to_dict() for entry in grid_result.results])


    columns = [
    "symbol",
    "total_return",
    "max_drawdown",
    "signal_count",
    "final_equity",]

    if strategy_type == "ma":
        columns[1:1] = [
            "ema_window",
            "sma_window",
        ]

    elif strategy_type == "rsi":
        columns[1:1] = [
            "window",
            "over_bought",
            "over_sold",
        ]

    elif strategy_type == "macd":
        columns[1:1] = [
            "fast_window",
            "slow_window",
            "signal_window",
        ]

    result_df = df[columns]

    result_df = result_df.sort_values(by="total_return", ascending=False)
    result_df["rank"] = result_df["total_return"].rank(ascending=False, method="dense").astype(int)
    result_df.to_csv("reports/strategy_results.csv", index=False)

if __name__ == "__main__" : 
    main()