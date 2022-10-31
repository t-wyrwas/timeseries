from typing import Optional

from twts_api.domain.timeserie import Timeserie

class Bucket:
    def __init__(self, name: str):
        self.name = name
        self._timeseries: list[Timeserie] = list()

    def add(self, timeserie: Timeserie):
        self._timeseries.append(timeserie)

    def get_by(self, name: str) -> Optional[Timeserie]:
        results = [ts for ts in filter(lambda ts: ts.name == name, self._timeseries)]
        results_len = len(results)
        assert results_len <= 1, f"Fatal! More than one ts with same unique name in bucket {self.name}."
        return results[0] if results_len > 0 else None

    def get_all(self) -> Optional[Timeserie]:
       return self._timeseries
