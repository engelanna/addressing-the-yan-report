from pytest import fixture

from src.dataclasses import GenomicRange
from src.constants import COLORS


@fixture
def expected_genomic_ranges_from_sars_cov_2_bed_file():
    return [
        GenomicRange(0, 280, "+", COLORS.structure, "5' untranslated region"),
        GenomicRange(281, 21289, "+", COLORS.structure, "Open reading frame 1ab"),
        GenomicRange(21578, 3821, "+", COLORS.structure, "Spike"),
        GenomicRange(25408, 827, "+", COLORS.structure, "Open reading frame 3"),
        GenomicRange(26260, 227, "+", COLORS.structure, "Envelope"),
        GenomicRange(26538, 668, "+", COLORS.structure, "Membrane"),
        GenomicRange(27217, 185, "+", COLORS.structure, "Open reading frame 6"),
        GenomicRange(27409, 365, "+", COLORS.structure, "Open reading frame 7"),
        GenomicRange(27909, 365, "+", COLORS.structure, "Open reading frame 8"),
        GenomicRange(28289, 1259, "+", COLORS.structure, "Nucleocapsid"),
        GenomicRange(29549, 923, "+", COLORS.structure, "3' untranslated region"),
    ]
