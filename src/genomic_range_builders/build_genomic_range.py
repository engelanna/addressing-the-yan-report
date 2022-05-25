from src.constants import COLORS
from src.dataclasses import (
    GenomicRange,
    RestrictionEnzyme,
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
            color=COLORS.miss,
            text_label=restriction_enzyme.name,
        )
