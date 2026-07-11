import matplotlib.pylab as plt 

def plot_drawdown_curve(backtest_data, title="Drawdown Curve"):

    result = backtest_data.copy()

    result["Peak"] = result["Cumulative_Return"].cummax()
    result["Drawdown"] = (
    result["Cumulative_Return"] / result["Peak"]) - 1

    fig, ax = plt.subplots(figsize=(10, 5))

    x = result.index
    y = result["Drawdown"]

    ax.plot(x, y, linewidth=2, label="Drawdown")

    ax.fill_between(x, y, 0, alpha=0.3)

    ax.set_title(title)
    ax.set_xlabel("Date")
    ax.set_ylabel("Drawdown")

    ax.grid(True)
    ax.legend()

    fig.tight_layout()

    return fig