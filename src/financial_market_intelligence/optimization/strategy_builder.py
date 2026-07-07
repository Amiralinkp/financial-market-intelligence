from financial_market_intelligence.strategies.moving_average import MovingAverageStrategy

strategies = []

def build_moving_average_strategies(ema_windows, sma_windows):
    
    strategies = []

    for ema in ema_windows :

        for sma in sma_windows :
            strategy = MovingAverageStrategy(
            fast_window= ema,
            slow_window= sma)

            strategies.append(strategy)

    return strategies