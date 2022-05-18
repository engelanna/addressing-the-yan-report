import pandas as pd
from typing import List

from ...constants import RestrictionEnzymeLocations
from .. import GenomicRange
from . import BuildGenomicRange


class BuildGenomicRangeList:
    def __init__(self):
        self.build_genomic_range = BuildGenomicRange()

    def from_locations_in_patent(
        self, genome_length: int, tolerance_as_fraction_of_genome_length: float = 0.05
    ) -> List[GenomicRange]:
        ranges = []

        for location in RestrictionEnzymeLocations.AS_GENOME_LENGTH_PERCENTAGES:
            a_single_range = self.build_genomic_range.at_fraction_of_genome_length(
                genome_length, location, tolerance_as_fraction_of_genome_length
            )
            ranges.append(a_single_range)

        return ranges

    def from_bed_file(self, bed_file_path: str) -> List[GenomicRange]:
        return list(
            pd.read_csv(
                "assets/bed/genes_sars_cov_2_nc_045512.2.bed",
                sep="\t",
                header=None,
            ).apply(lambda row: (row[1], row[2] - row[1], row[5], "#E74C3C"), axis=1)
        )
