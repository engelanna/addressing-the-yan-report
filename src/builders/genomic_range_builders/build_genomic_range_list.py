import pandas as pd
from typing import List

from .build_genomic_range import BuildGenomicRange
from src.constants import COLORS
from src.dataclasses import GenomicRange, SequenceOccurrence


class BuildGenomicRangeList:
    def __init__(self):
        self.build_genomic_range = BuildGenomicRange()

    def from_bed_file(self, bed_file_path: str) -> List[GenomicRange]:
        df = pd.read_csv(bed_file_path, sep="\t", header=None)
        formatted_rows = df.apply(
            lambda row: (row[1], row[2] - row[1], row[5], COLORS.structure, row[3]),
            axis=1,
        )

        return [GenomicRange(*row) for row in formatted_rows]

    def from_search_results(
        self, genome: str, sequence_occurrences: List[SequenceOccurrence]
    ) -> List[GenomicRange]:
        return [
            self.build_genomic_range.at_sequence_occurrence_coordinates(occurrence)
            for occurrence in sequence_occurrences
        ]
