from dataclasses import dataclass


@dataclass
class RestrictionEnzyme:
    location_as_fraction_genome_length: float
    name: str
    sequence: str
