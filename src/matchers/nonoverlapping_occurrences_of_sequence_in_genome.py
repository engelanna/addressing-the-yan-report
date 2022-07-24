from re import compile
from sys import maxsize

from src.dataclasses import SequenceOccurrence
from typing import (
    Dict,
    Tuple,
)


class NonoverlappingOccurrencesOfSequenceInGenome:
    def __init__(self, genome: str):
        self.genome = genome

    def __call__(
        self,
        sequence: str,
        start_position: int = 0,
        end_position: int = maxsize,
    ) -> Dict[Tuple, str]:
        regexp_pattern = sequence.replace("N", r"\w")

        match_objects = list(
            compile(regexp_pattern).finditer(self.genome, start_position, end_position)
        )

        return [
            SequenceOccurrence(
                span=match_object.span(),
                sequence_sought=sequence,
                sequence_found=match_object.group(),
            )
            for match_object in match_objects
        ]
