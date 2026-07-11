import pandas as pd
import matplotlib.pyplot as plt 

def plot_equity_curve(backtest_data, title="Equity Curve"):

    fig, ax = plt.subplots()
    x = backtest_data.index
    y = backtest_data["Cumulative_Return"]
    ax.plot(x, y, linewidth = 2, label = "Strategy")

    ax.set_title(title)
    ax.set_xlabel("Date")
    ax.set_ylabel("Equity")
    ax.grid(True)
    ax.legend()
    fig.tight_layout()

    return fig