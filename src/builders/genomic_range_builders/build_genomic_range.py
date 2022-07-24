from src.constants import (
    sequence_sought_to_color,
    COLORS,
    sequence_sought_to_enzyme_name,
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
            color=sequence_sought_to_color(occurrence.sequence_sought),
            text_label=sequence_sought_to_enzyme_name(occurrence.sequence_sought),
        )
