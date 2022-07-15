from src.genomic_range_builders import BuildGenomicRangeList
from . import RestrictionEnzymePresence


class RunBatteryOfRangeTests:
    def __init__(self):
        self.restriction_enzyme_presence = RestrictionEnzymePresence()

    def __call__(self, genome: str, mismatches_allowed: int = 0):
        # find all ClaI -> then the next ones
        # kmer or subseq index

        return BuildGenomicRangeList().from_locations_in_patent(
            genome, tolerance_as_fraction_of_genome_length=0.05
        )

    def _run_single_test(self):
        pass

    # self._test_output_color(
    #             genome, restriction_enzyme, tolerance_as_fraction_of_genome_length
    #         )
    #     # return (
    #     COLORS.miss
    #     if RestrictionEnzymePresence()(genome, enzyme, tolerance)
    #     else
    # )
