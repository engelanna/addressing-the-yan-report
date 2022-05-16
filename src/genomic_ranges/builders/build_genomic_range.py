from .. import GenomicRange


class BuildGenomicRange:
    def __call__(
        self,
        genome_length: int,
        tolerance_as_fraction_of_genome_length: float,
        restriction_enzyme_location_as_fraction_genome_length: float,
        color: str = "#E74C3C",
    ):
        width = tolerance_as_fraction_of_genome_length * genome_length
        start = (
            restriction_enzyme_location_as_fraction_genome_length * genome_length
        ) - width / 2

        return GenomicRange(
            start=round(start),
            width=round(width),
            strand=None,
            color=color,
        )
