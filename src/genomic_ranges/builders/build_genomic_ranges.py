from ..constants import RestrictionEnzymeLocations
from . import BuildGenomicRange


class BuildGenomicRanges:
    def __init__(self):
        self.build_diagram_range = BuildGenomicRange()

    def __call__(
        self, genome_length: int, tolerance_as_fraction_of_genome_length: float = 0.05
    ):
        ranges = []

        for location in RestrictionEnzymeLocations.AS_GENOME_LENGTH_PERCENTAGES:
            a_single_range = self.build_diagram_range(
                genome_length, tolerance_as_fraction_of_genome_length, location
            )
            ranges.append(a_single_range)

        return ranges
