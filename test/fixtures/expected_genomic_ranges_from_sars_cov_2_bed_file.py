from pytest import fixture

from src.dataclasses import GenomicRange
from src.constants import COLORS


@fixture
def expected_genomic_ranges_from_sars_cov_2_bed_file():
    return [
        GenomicRange(0, 265, "+", COLORS.miss, "5' UTR"),
        GenomicRange(265, 21290, "+", COLORS.miss, "ORF1ab"),
        GenomicRange(21562, 3822, "+", COLORS.miss, "S"),
        GenomicRange(25392, 828, "+", COLORS.miss, "ORF3a"),
        GenomicRange(26244, 228, "+", COLORS.miss, "E"),
        GenomicRange(26522, 669, "+", COLORS.miss, "M"),
        GenomicRange(27201, 186, "+", COLORS.miss, "ORF6"),
        GenomicRange(27393, 366, "+", COLORS.miss, "ORF7a"),
        GenomicRange(27755, 132, "+", COLORS.miss, "ORF7b"),
        GenomicRange(27893, 366, "+", COLORS.miss, "ORF8"),
        GenomicRange(28273, 1260, "+", COLORS.miss, "N"),
        GenomicRange(29557, 117, "+", COLORS.miss, "ORF10"),
        GenomicRange(29674, 229, "+", COLORS.miss, "3' UTR"),
    ]
