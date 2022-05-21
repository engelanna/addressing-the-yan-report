from re import compile
from sys import maxsize

from src.dataclasses import SequenceOccurrence
from typing import (
    Dict,
    Tuple,
)


class OccurrencesOfPatternInGenome:
    def __init__(self, genome: str):
        self.genome = genome

    def __call__(
        self,
        regexp_pattern: str,
        start_position: int = 0,
        end_position: int = maxsize,
    ) -> Dict[Tuple, str]:

        match_objects = list(
            compile(regexp_pattern).finditer(self.genome, start_position, end_position)
        )

        return [
            SequenceOccurrence(
                span=match_object.span(), regexp_pattern=match_object.group()
            )
            for match_object in match_objects
        ]
