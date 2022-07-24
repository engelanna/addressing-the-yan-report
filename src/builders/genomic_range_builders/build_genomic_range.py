from src.constants import (
    sequence_sought_to_color,
    COLORS,
    sequence_sought_to_enzyme_name,
)
from src.dataclasses import GenomicRange, SequenceOccurrence


class BuildGenomicRange:
    def at_sequence_occurrence_coordinates(self, occurrence: SequenceOccurrence):
        return GenomicRange(
            start=occurrence.span[0],
            width=occurrence.span[1] - occurrence.span[0],
            strand=None,
            color=sequence_sought_to_color(occurrence.sequence_sought),
            text_label=sequence_sought_to_enzyme_name(occurrence.sequence_sought),
        )
