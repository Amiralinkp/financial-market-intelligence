from financial_market_intelligence.models.run_result import RunResult
from financial_market_intelligence.models.trade_analysis_result import TradeAnalysisResult
from financial_market_intelligence.models.performance_metrics import PerformanceMetrics



def _generate_general_section(run_result):
    lines = []

    lines.append("")
    lines.append("TRADE SUMMARY")
    lines.append("=" * 40)
    lines.append("")

    items = [
    ("Symbol", run_result.symbol),
    ("Strategy", run_result.strategy_name),
    ("Start Date", run_result.start_date),
    ("End Date", run_result.end_date)]

    for label, value in items:
        lines.append(f"{label:<25}: {value}")

    return "\n".join(lines)

def _generate_trade_section(trade_analysis_result):

    lines = []
    items = [
    ("Total Trades", trade_analysis_result.total_trades),
    ("Winning Trades", trade_analysis_result.winning_trades),
    ("Losing Trades", trade_analysis_result.losing_trades),
    ("Breakeven Trades", trade_analysis_result.breakeven_trades),

    ("Win Rate", f"{trade_analysis_result.win_rate:.2f}%"),
    ("Average Win (%)", f"{trade_analysis_result.average_win * 100:.2f}%"),
    ("Average Loss (%)", f"{abs(trade_analysis_result.average_loss) * 100:.2f}%"),

    ("Largest Win (%)", f"{trade_analysis_result.largest_win * 100:.2f}%"),
    ("Largest Loss (%)", f"{abs(trade_analysis_result.largest_loss) * 100:.2f}%"),
    ("Profit Factor", f"{trade_analysis_result.profit_factor:.2f}"),
    ("Payoff Ratio", f"{trade_analysis_result.payoff_ratio:.2f}"),

    ("Average Holding Bars", f"{trade_analysis_result.average_holding_bars:.2f}")]

    for label, value in items:
        lines.append(f"{label:<25}: {value}")
        

    return "\n".join(lines)

def _generate_performance_section(metrics):
    lines = []
    lines.append("")
    lines.append("PERFORMANCE")
    lines.append("=" * 40)
    lines.append("")
    items = [
    ("Final Equity",f"{metrics.final_equity: .2f}"),
    ("Total Return (%)", f"{metrics.total_return: .2f}%"),
    ("Total Signals", f"{metrics.signal_count}")]
    for label, value in items:
        lines.append(f"{label:<25}: {value}")

    return "\n".join(lines)

def _generate_risk_section(metrics):
    lines = []
    lines.append("")
    lines.append("RISK")
    lines.append("=" * 40)
    lines.append("")

    items = [
    ("Maximum Drawdown (%)", f"{abs(metrics.max_drawdown) * 100:.2f}%")]
    for label, value in items:
        lines.append(f"{label:>25}: {value}")

    return "\n".join(lines)

def generate_report(run_result):

    general_section = _generate_general_section(run_result)

    trade_section = _generate_trade_section(run_result.trade_analysis_result)

    performance_section = _generate_performance_section(run_result.metrics)

    risk_section = _generate_risk_section(run_result.metrics)

    sections = [
        general_section,
        trade_section,
        performance_section,
        risk_section]

    return "\n\n".join(sections)

