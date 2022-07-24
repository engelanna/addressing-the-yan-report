from dataclasses import dataclass
from typing import Tuple


@dataclass
class SequenceOccurrence:
    span: Tuple[int, int]
    sequence_sought: str
    sequence_found: str
