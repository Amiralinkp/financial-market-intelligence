from financial_market_intelligence.models.execution_result import ExecutionResult
from financial_market_intelligence.models.trade_analysis_result import TradeAnalysisResult
import numpy as np


def analyze_trades(execution_result):

    trades = execution_result.trades

    if len(trades) == 0:

        return TradeAnalysisResult(
            total_trades=0,
            winning_trades = 0 ,
            losing_trades = 0,
            breakeven_trades = 0,
            win_rate = 0.0,
            average_win = 0.0,
            average_loss = 0.0,
            largest_win = 0.0,
            largest_loss = 0.0,
            average_holding_bars = 0.0,
            payoff_ratio = 0.0,
            profit_factor = 0.0)
    
    else:
    

        total_trades = len(trades)
        
        winning_trades = sum( 1 for trade in trades if trade.trade_return > 0 )

        losing_trades = sum( 1 for trade in trades if trade.trade_return < 0 )

        breakeven_trades = sum( 1 for trade in trades if trade.trade_return == 0 )

        win_rate = (winning_trades/total_trades)*100

        wins = [trade.trade_return for trade in trades if trade.trade_return > 0]

        if wins  :
            average_win = np.mean(wins)

        else :
            average_win = 0.0

        losses = [trade.trade_return for trade in trades if trade.trade_return < 0]

        if losses :
            average_loss = np.mean(losses)

        else :
            average_loss = 0.0

        if wins:
            largest_win = max(wins)
        else:
            
            largest_win = 0.0


        if losses:
            largest_loss = min(losses)

        else:
            largest_loss = 0.0

        gross_profit = sum(wins)
        gross_loss = abs(sum(losses))

        if gross_loss == 0 :

            profit_factor = float("inf")

        else:

            profit_factor = gross_profit / gross_loss


        if average_loss == 0 :
            payoff_ratio = float("inf")

        else:
            payoff_ratio = average_win/abs(average_loss)

        holding_bars = [trade.holding_bars for trade in trades]

        average_holding_bars = (np.mean(holding_bars) if holding_bars else 0.0)

    return TradeAnalysisResult(
            total_trades= total_trades,
            winning_trades = winning_trades ,
            losing_trades = losing_trades,
            breakeven_trades = breakeven_trades,
            win_rate = win_rate,
            average_win = average_win,
            average_loss = average_loss,
            largest_win = largest_win,
            largest_loss = largest_loss,
            average_holding_bars = average_holding_bars,
            payoff_ratio = payoff_ratio,
            profit_factor = profit_factor)