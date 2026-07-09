from financial_market_intelligence.strategies.moving_average import MovingAverageStrategy
from financial_market_intelligence.strategies.rsi import RSIStrategy
from financial_market_intelligence.strategies.macd import MACDStrategy

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

def build_rsi_strategies(windows, over_bought_values = None, over_sold_values = None):

    strategies = []

    if over_bought_values is None:
                over_bought_values = [70]
    if over_sold_values is None:
                over_sold_values = [30]

    for window in windows:
        for over_bought in over_bought_values:
            for over_sold in over_sold_values:
                

                strategy = RSIStrategy(
                    window = window, over_bought=over_bought, over_sold=over_sold)
                
                strategies.append(strategy)

    return strategies

def build_macd_strategies( fast_windows = None, slow_windows = None, signal_windows = None):
      
    strategies = []

    if fast_windows is None:
            fast_windows = [12]

    if slow_windows is None:
            slow_windows = [26]

    if signal_windows is None:
            signal_windows = [9]

    for signal_window in signal_windows:
        for slow_window in slow_windows:
            for fast_window in fast_windows:
                  
                  strategy = MACDStrategy(
                        fast_window=fast_window, slow_window=slow_window, signal_window=signal_window)
                  
                  strategies.append(strategy)
                  
    return strategies
      

