from src.dataclasses.restriction_enzyme import RestrictionEnzyme


def sequence_sought_to_enzyme_name(sequence):
    return {
        "GAATTC": "EcoRI",
        "GGTNACC": "BstEII",
        "GCCNNNNNGGC": "BglI",
        "CCANNNNNNTGG": "BstXI",
    }[sequence]


RESTRICTION_ENZYMES_MARTIN_AND_MERCOLA = (
    RestrictionEnzyme(
        start_at_fraction_genome_length=0.23765735409638497,
        name="BglI",
        sequence="GCCNNNNNGGC",
    ),
    RestrictionEnzyme(
        start_at_fraction_genome_length=0.362360754735662,
        name="BstXI",
        sequence="CCANNNNNNTGG",
    ),
    RestrictionEnzyme(
        start_at_fraction_genome_length=0.413095950596385,
        name="BglI",
        sequence="GCCNNNNNGGC",
    ),
    RestrictionEnzyme(
        start_at_fraction_genome_length=0.611902968096385,
        name="BglI",
        sequence="GCCNNNNNGGC",
    ),
    RestrictionEnzyme(
        start_at_fraction_genome_length=0.709343210835662,
        name="SfiI",
        sequence="GGCCNNNNNGGCC",
    ),
    RestrictionEnzyme(
        start_at_fraction_genome_length=0.7834468277963851,
        name="BglI",
        sequence="GCCNNNNNGGC",
    ),
    RestrictionEnzyme(
        start_at_fraction_genome_length=0.819478623017831,
        name="Open reading frame 3 TSE",
        sequence="ACTAAAC",
    ),
    RestrictionEnzyme(
        start_at_fraction_genome_length=0.819478623017831,
        name="ClaI",
        sequence="ATCGAT",
    ),
    RestrictionEnzyme(
        start_at_fraction_genome_length=0.8538678803963851,
        name="PflMI",
        sequence="CCANNNNNTGG",
    ),
    RestrictionEnzyme(
        start_at_fraction_genome_length=0.8606716054178309,
        name="ScaI",
        sequence="AGTACT",
    ),
    RestrictionEnzyme(
        start_at_fraction_genome_length=0.877864587917831,
        name="AvrII",
        sequence="CCTAGG",
    ),
    RestrictionEnzyme(
        start_at_fraction_genome_length=0.9010178170963851,
        name="EcoNI",
        sequence="CCTNNNNNAGG",
    ),
    RestrictionEnzyme(
        start_at_fraction_genome_length=0.925788443917831,
        name="StuI",
        sequence="AGGCCT",
    ),
    RestrictionEnzyme(
        start_at_fraction_genome_length=0.928034238817831,
        name="Esp3I",
        sequence="CGTCTCN",
    ),
    RestrictionEnzyme(
        start_at_fraction_genome_length=0.931710347396385,
        name="AhdI",
        sequence="GACNNNNNGTC",
    ),
    RestrictionEnzyme(
        start_at_fraction_genome_length=0.976693128317831,
        name="KpnI",
        sequence="GGTACC",
    ),
    RestrictionEnzyme(
        start_at_fraction_genome_length=0.981899874957108,
        name="PacI",
        sequence="TTAATTAA",
    ),
    RestrictionEnzyme(
        start_at_fraction_genome_length=0.999304830657108,
        name="SapI",
        sequence="GCTCTTCN",
    ),
    RestrictionEnzyme(
        start_at_fraction_genome_length=0.999585532357108,
        name="NotI",
        sequence="GCGGCCGC",
    ),
)
