from dataclasses import dataclass, Field

@dataclass(frozen=True)
class Timeserie:
    name: str
