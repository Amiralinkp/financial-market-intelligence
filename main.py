import pandas as pd
from financial_market_intelligence.optimization.grid_search import grid_search
from financial_market_intelligence.strategies.runner import run_strategy




def main():
    symbols = [
    "NVDA",
    "AAPL",
    "MSFT",
    "GOOG",
    "META",]

    

    ema_windows = [20,30,50]
    sma_windows = [20,30,50]
    # best_asset = (max(result, key=lambda x:x["total_return"]))
    # worst_asset = (min(result, key=lambda x:x["total_return"]))
    result = grid_search(symbols, ema_windows, sma_windows)
    df = pd.DataFrame(result)

    result_df = df[[
        "symbol",
        "ema_window",
        "sma_window",
        "total_return",
        "max_drawdown",
        "signal_count",
        "final_equity"]]

    result_df = result_df.sort_values(by="total_return", ascending=False)
    result_df["rank"] = result_df["total_return"].rank(ascending=False, method="dense").astype(int)
    result_df.to_csv("reports/strategy_results.csv", index=False)


if __name__ == "__main__" : 
    main()