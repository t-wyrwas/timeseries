from dataclasses import dataclass


@dataclass
class Timeserie:
    name: str = None

@dataclass
class Bucket:
    name: str
    timeseries: list[Timeserie]
