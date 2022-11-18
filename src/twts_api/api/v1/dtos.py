from typing import Union
from dataclasses import dataclass
from datetime import datetime as dt


@dataclass
class Timeserie:
    name: str = None
    unit: str = None
    properties: dict[str, Union[str, int, float]] = None

@dataclass
class Bucket:
    name: str
    timeseries: list[Timeserie]

@dataclass
class Point:
    timestamp: dt
    value: float
