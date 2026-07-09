from financial_market_intelligence.strategies.base import BaseStrategy
from financial_market_intelligence.signals.macd import macd_signal
from financial_market_intelligence.features.returns import add_simple_return
from financial_market_intelligence.indicators.macd import add_macd



class MACDStrategy(BaseStrategy):

    def __init__(self,  fast_window=12, slow_window=26, signal_window=9):

        self.fast_window = fast_window
        self.slow_window = slow_window
        self.signal_window = signal_window


    def generate_signal(self, data):

        return macd_signal(data)


    def get_name(self):
        return (
        f"MACD("
        f"fast={self.fast_window}, "
        f"slow={self.slow_window}, "
        f"signal={self.signal_window}"
        f")")
    
    def get_parameters(self):
        
        parameters = {
            "fast_window" : self.fast_window,
            "slow_window" : self.slow_window,
            "signal_window" : self.signal_window
        }
        return parameters


    def get_required_indicators(self):

        return[
            add_simple_return,
            lambda data: add_macd(data, fast_window=self.fast_window,
                                   slow_window=self.slow_window, signal_window=self.signal_window)]


        