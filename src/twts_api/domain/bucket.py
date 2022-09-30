from dataclasses import dataclass

from twts_api.domain.timeserie import Timeserie

class Bucket:
    def __init__(self, name: str):
        self._name = name
        self._timeseries: dict = {}

    @property
    def name(self):
        return self._name

    def add(self, timeserie: Timeserie):
        self._timeseries[timeserie.name] = timeserie

    def get(self, name: str):
        return self._timeseries[name]
