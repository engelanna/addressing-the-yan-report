class RangeForChart:
    def __call__(
        self,
        genome_length: int,
        tolerance_as_fraction_of_genome_length: float,
        restriction_enzyme_location_as_percentage_genome_length: float,
    ):
        width = tolerance_as_fraction_of_genome_length * genome_length
        start = (
            restriction_enzyme_location_as_percentage_genome_length * genome_length
        ) - width / 2

        return (
            round(start),
            round(width),
            "+",
            "#E74C3C",
        )
