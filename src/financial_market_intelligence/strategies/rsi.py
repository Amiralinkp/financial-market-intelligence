from financial_market_intelligence.strategies.base import BaseStrategy
from financial_market_intelligence.signals.rsi import rsi_signal
from financial_market_intelligence.features.returns import add_simple_return
from financial_market_intelligence.indicators.rsi import add_rsi

class RSIStrategy(BaseStrategy):

    def __init__(self, window, over_bought = 70, over_sold = 30):
        self.window = window
        self.over_bought = over_bought
        self.over_sold = over_sold


    def generate_signal(self, data):

        return rsi_signal(data,self.over_sold, self.over_bought, rsi_column=f"RSI_{self.window}" )
        
        


    def get_name(self):
        return f"RSI({self.window})"
    
    def get_parameters(self):
        
        parameters = {
            "rsi_window" : self.window,
            "over_bought" : self.over_bought,
            "over_sold" : self.over_sold
        }
        return parameters


    def get_required_indicators(self):

        return[
            add_simple_return,
            lambda data: add_rsi(data, window=self.window)

        ]
