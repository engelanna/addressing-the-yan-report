from . import RangeForChart

RESTRICTION_ENZYME_LOCATIONS_AS_GENOME_LENGTH_PERCENTAGES = (
    0.2378245614,
    0.3625614035,
    0.4132631579,
    0.6120701754,
    0.7095438596,
    0.7836140351,
    0.8195789474,
    0.8195789474,
    0.8540350877,
    0.8607719298,
    0.8779649123,
    0.9011850244,
    0.9258887683,
    0.9281345632,
    0.9318775547,
    0.9767934527,
    0.9820336408,
    0.9994385965,
    0.9997192982,
)


class GenerateRangesForChart:
    def __init__(self):
        self.range_for_chart = RangeForChart()

    def __call__(
        self, genome_length: int, tolerance_as_fraction_of_genome_length: float = 0.05
    ):
        ranges_for_chart = []

        for location in RESTRICTION_ENZYME_LOCATIONS_AS_GENOME_LENGTH_PERCENTAGES:
            ranges_for_chart.append(
                self.range_for_chart(
                    genome_length, tolerance_as_fraction_of_genome_length, location
                )
            )

        return ranges_for_chart
