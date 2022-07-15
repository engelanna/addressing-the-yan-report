from pytest import fixture

from src.dataclasses import GenomicRange
from src.constants import COLORS


@fixture
def expected_genomic_ranges_from_sars_cov_2_bed_file():
    return [
        GenomicRange(0, 281, "+", COLORS.miss, "5' UTR"),
        GenomicRange(282, 21289, "+", COLORS.miss, "ORF1ab"),
        GenomicRange(21579, 3821, "+", COLORS.miss, "S"),
        GenomicRange(25409, 827, "+", COLORS.miss, "ORF3"),
        GenomicRange(26261, 227, "+", COLORS.miss, "E"),
        GenomicRange(26539, 668, "+", COLORS.miss, "M"),
        GenomicRange(27218, 185, "+", COLORS.miss, "ORF6"),
        GenomicRange(27410, 365, "+", COLORS.miss, "ORF7"),
        GenomicRange(27910, 365, "+", COLORS.miss, "ORF8"),
        GenomicRange(28290, 1259, "+", COLORS.miss, "N"),
        GenomicRange(29550, 923, "+", COLORS.miss, "3' UTR"),
    ]
