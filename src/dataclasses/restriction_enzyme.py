from dataclasses import dataclass


@dataclass
class RestrictionEnzyme:
    start_at_fraction_genome_length: float
    name: str
    sequence: str
