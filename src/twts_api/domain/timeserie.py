from typing import Union
from dataclasses import dataclass, asdict
from json import dumps

@dataclass
class Timeserie:
    name: str
    unit: str
    properties: dict[str, Union[str, int, float]]
