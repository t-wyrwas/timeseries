from typing import Optional

from twts_api.domain.timeserie import Timeserie

class Bucket:
    def __init__(self, name: str):
        self._name = name
        self._timeseries = set()

    @property
    def name(self):
        return self._name

    def add(self, timeserie: Timeserie):
        self._timeseries.add(timeserie)

    def get(self, name: str) -> Optional[Timeserie]:
        results = [ts for ts in filter(lambda ts: ts.name == name, self._timeseries)]
        results_len = len(results)
        assert results_len <= 1, f"Fatal! More than one ts with same unique name in bucket {self._name}."
        return results[0] if results_len > 0 else None
