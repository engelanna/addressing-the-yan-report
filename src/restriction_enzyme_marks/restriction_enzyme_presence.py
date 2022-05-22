from src.dataclasses import RestrictionEnzyme
from src.matchers import NonoverlappingOccurrencesOfSequenceInGenome


class RestrictionEnzymePresence:
    def __call__(
        self,
        genome: str,
        enzyme: RestrictionEnzyme,
        tolerance_as_fraction_genome_length: float,
    ):
        half_tolerance = tolerance_as_fraction_genome_length * len(genome) / 2
        start_position = round(
            enzyme.start_at_fraction_genome_length * len(genome) - half_tolerance
        )
        end_position = round(
            enzyme.start_at_fraction_genome_length * len(genome) + half_tolerance
        )

        return bool(
            NonoverlappingOccurrencesOfSequenceInGenome(genome)(
                enzyme.sequence, start_position, end_position
            )
        )
