from src.constants import COLORS
from src.dataclasses import (
    GenomicRange,
    RestrictionEnzyme,
)


class BuildGenomicRange:
    def at_fraction_of_genome_length(
        self,
        genome_length: int,
        restriction_enzyme: RestrictionEnzyme,
        tolerance_as_fraction_of_genome_length: float,
        color: str = COLORS.miss,
    ) -> GenomicRange:

        width = tolerance_as_fraction_of_genome_length * genome_length
        start = (
            restriction_enzyme.location_as_fraction_genome_length * genome_length
        ) - width / 2

        return GenomicRange(
            start=round(start),
            width=round(width),
            strand=None,
            color=color,
            text_label=restriction_enzyme.name,
        )
