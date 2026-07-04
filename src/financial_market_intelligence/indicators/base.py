from collections.abc import Callable
import pandas as pd

Indicator = Callable[[pd.DataFrame], pd.DataFrame]