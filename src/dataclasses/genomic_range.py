from dataclasses import dataclass

from src.constants import COLORS


@dataclass
class GenomicRange:
    start: int
    width: int
    strand: str = "."
    color: str = COLORS.miss
    text_label: str = ""
