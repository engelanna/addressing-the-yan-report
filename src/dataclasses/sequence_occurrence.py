from dataclasses import dataclass
from typing import Tuple


@dataclass
class SequenceOccurrence:
    span: Tuple[int, int]
    sequence: str
