from src.constants import COLORS
from src.dataclasses import (
    GenomicRange,
    RestrictionEnzyme,
)
from src.restriction_enzyme_marks.restriction_enzyme_presence import (
    RestrictionEnzymePresence,
)


class BuildGenomicRange:
    def at_fraction_of_genome_length(
        self,
        genome: str,
        restriction_enzyme: RestrictionEnzyme,
        tolerance_as_fraction_of_genome_length: float,
    ) -> GenomicRange:
        genome_length = len(genome)
        width = tolerance_as_fraction_of_genome_length * genome_length
        start = (
            restriction_enzyme.start_at_fraction_genome_length * genome_length
        ) - width / 2

        return GenomicRange(
            start=round(start),
            width=round(width),
            strand=None,
            color=self._test_output_color(
                genome, restriction_enzyme, tolerance_as_fraction_of_genome_length
            ),
            text_label=restriction_enzyme.name,
        )

    def _test_output_color(self, genome, enzyme, tolerance):
        return (
            COLORS.miss
            if RestrictionEnzymePresence()(genome, enzyme, tolerance)
            else COLORS.miss
        )
