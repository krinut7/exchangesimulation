from exchangesimulation import constants
from dataclasses import dataclass


@dataclass
class Fluctuation:
    formula: str
    variable: str = "x"
