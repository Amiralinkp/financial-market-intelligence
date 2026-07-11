import pandas as pd 
from financial_market_intelligence.models.trade import Trade
from financial_market_intelligence.models.execution_result import ExecutionResult


def execute_strategy(signal_data):

    result = signal_data.copy()

    trades = []
    position = 0
    pending_order = None
    entry_price = None
    entry_date = None

    trade_id = 1

    positions = []

    for i in range(len(result)):

        current_row = result.iloc[i]


        if pending_order == 1:

            position = 1

            entry_price = current_row["Open"]
            entry_date = result.index[i]

            pending_order = None

        elif pending_order == 0:

            exit_price = current_row["Open"]
            exit_date = result.index[i]

            trade_return = (exit_price - entry_price) / entry_price

            trades.append(
                Trade(
                    trade_id=trade_id,
                    entry_date=entry_date,
                    exit_date=exit_date,
                    entry_price=entry_price,
                    exit_price=exit_price,
                    direction="LONG",
                    trade_return=trade_return))

            trade_id += 1

            position = 0

            entry_price = None
            entry_date = None

            pending_order = None

    

        positions.append(position)

        

        signal = current_row["Signal"]

        if signal == 1 and position == 0 and pending_order is None:

            pending_order = 1

        elif signal == -1 and position == 1 and pending_order is None:

            pending_order = 0

    result["Position"] = positions

    return ExecutionResult(
        trades=trades,
        data=result)

        