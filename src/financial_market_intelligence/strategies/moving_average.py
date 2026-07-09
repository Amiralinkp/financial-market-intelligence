from financial_market_intelligence.strategies.base import BaseStrategy
from financial_market_intelligence.signals.crossover import moving_average_crossover_signal
from financial_market_intelligence.features.returns import add_simple_return
from financial_market_intelligence.indicators.sma import add_sma
from financial_market_intelligence.indicators.ema import add_ema





class MovingAverageStrategy(BaseStrategy):

    def __init__(self, fast_window, slow_window):
        self.fast_window = fast_window
        self.slow_window = slow_window


    def generate_signal(self, data):
        return moving_average_crossover_signal(data,
         fast_column=f"EMA_{self.fast_window}",
         slow_column=f"SMA_{self.slow_window}")
    
    def get_name(self):
        return f"EMA({self.fast_window}) / SMA({self.slow_window})"
    
    def get_parameters(self):
    
       parameters = { "ema_window" : self.fast_window,
        "sma_window" : self.slow_window }
       return parameters
    
    def get_required_indicators(self):
        
        return[add_simple_return,
            lambda data: add_sma(data, window=self.slow_window),
            lambda data: add_ema(data, window=self.fast_window),

        ]