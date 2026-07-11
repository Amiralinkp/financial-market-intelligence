from dataclasses import dataclass




@dataclass
class GridSearchResult:
    results: object
    best_strategy: object
    best_symbol: str