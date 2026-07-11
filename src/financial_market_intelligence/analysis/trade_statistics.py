from financial_market_intelligence.models.trade_statistics import TradeStatistics

def calculate_trade_statistics(backtest_data):

    result = backtest_data.copy()

    buy_signal = result["Signal"] == 1

    sell_signal = result["Signal"] == -1

    total_buy = buy_signal.sum()
    total_sell = sell_signal.sum()