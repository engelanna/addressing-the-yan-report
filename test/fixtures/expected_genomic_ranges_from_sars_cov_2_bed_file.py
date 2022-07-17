from pytest import fixture

from src.dataclasses import GenomicRange
from src.constants import COLORS


@fixture
def expected_genomic_ranges_from_sars_cov_2_bed_file():
    return [
        GenomicRange(0, 280, "+", COLORS.structure, "5' UTR"),
        GenomicRange(281, 21289, "+", COLORS.structure, "ORF1ab"),
        GenomicRange(21578, 3821, "+", COLORS.structure, "S"),
        GenomicRange(25408, 827, "+", COLORS.structure, "ORF3"),
        GenomicRange(26260, 227, "+", COLORS.structure, "E"),
        GenomicRange(26538, 668, "+", COLORS.structure, "M"),
        GenomicRange(27217, 185, "+", COLORS.structure, "ORF6"),
        GenomicRange(27409, 365, "+", COLORS.structure, "ORF7"),
        GenomicRange(27909, 365, "+", COLORS.structure, "ORF8"),
        GenomicRange(28289, 1259, "+", COLORS.structure, "N"),
        GenomicRange(29549, 923, "+", COLORS.structure, "3' UTR"),
    ]
