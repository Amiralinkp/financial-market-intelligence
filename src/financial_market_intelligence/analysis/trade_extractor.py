import pandas as pd



def extract_trades(backtest_data):

    result = backtest_data.copy()

    trades = []

    entry_price = None
    entry_date = None

    for i in range(len(result), -1):
        if row["Signal"] == 1:
            entry_price = row["Close"]
            entry_date = index

        if row["Signal"] == -1 and entry_price is not None:
            exit_price = row["Close"]
            exit_date = index

            trade_return = (exit_price - entry_price)/entry_price

        trades.append({
                        "Entry_Date": entry_date,
                        "Exit_Date": exit_date,
                        "Entry_Price": entry_price,
                        "Exit_Price": exit_price,
                        "Trade_Return": trade_return})
        
        entry_price = None
        entry_date = None
        
    return pd.DataFrame(trades)