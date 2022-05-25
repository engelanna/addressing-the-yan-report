import pandas as pd
from typing import List

from ..constants import (
    COLORS,
    RESTRICTION_ENZYMES,
)
from ..dataclasses import GenomicRange
from .build_genomic_range import BuildGenomicRange


class BuildGenomicRangeList:
    def __init__(self):
        self.build_genomic_range = BuildGenomicRange()

    def from_sars_cov_2_bed_file(self, bed_file_path: str) -> List[GenomicRange]:
        df = pd.read_csv(bed_file_path, sep="\t", header=None)
        formatted_rows = df.apply(
            lambda row: (row[1], row[2] - row[1], row[5], COLORS.miss, row[3]), axis=1
        )

        return [GenomicRange(*row) for row in formatted_rows]

    def from_locations_in_patent(
        self, genome: str, tolerance_as_fraction_of_genome_length: float = 0.05
    ) -> List[GenomicRange]:

        ranges = []
        for enzyme in RESTRICTION_ENZYMES:

            a_single_range = self.build_genomic_range.at_fraction_of_genome_length(
                genome, enzyme, tolerance_as_fraction_of_genome_length
            )

            ranges.append(a_single_range)
        return ranges
