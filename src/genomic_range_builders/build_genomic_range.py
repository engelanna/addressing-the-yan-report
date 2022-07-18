from src.constants import (
    COLOR_FROM_RESTRICTION_ENZYME_SEQUENCE,
    COLORS,
    RESTRICTION_ENZYMES_YAN_ET_AL,
)
from src.dataclasses import (
    GenomicRange,
    RestrictionEnzyme,
    SequenceOccurrence,
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

    def at_sequence_occurrence_coordinates(self, occurrence: SequenceOccurrence):
        return GenomicRange(
            start=occurrence.span[0],
            width=occurrence.span[1] - occurrence.span[0],
            strand=None,
            color=COLOR_FROM_RESTRICTION_ENZYME_SEQUENCE(occurrence.sequence),
            text_label=RESTRICTION_ENZYMES_YAN_ET_AL(occurrence.sequence),
        )
