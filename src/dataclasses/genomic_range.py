from dataclasses import dataclass


@dataclass
class GenomicRange:
    start: int
    width: int
    strand: str = "."
    color: str = "grey"
    text_label: str = ""
