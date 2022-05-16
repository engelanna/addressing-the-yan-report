from typing import (
    NamedTuple,
    Optional,
)


class GenomicRange(NamedTuple):
    start: int
    width: int
    strand: Optional[str]
    color: str
