from financial_market_intelligence.strategies.base import BaseStrategy


class RSIStrategy(BaseStrategy):

    def __init__(self, window):
        self.window = window


    def generate_signal(self, data):
        
        return data


    def get_name(self):
        return f"RSI({self.window})"