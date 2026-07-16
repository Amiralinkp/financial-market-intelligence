from dataclasses import dataclass
from financial_market_intelligence.models.grid_search_entry import GridSearchEntry



@dataclass
class GridSearchResult:
    results: object
    best_strategy: object
    best_symbol: str
    results: list[GridSearchEntry]