from src.constants import COLORS
from src.dataclasses import GenomicRange

from pytest import fixture


@fixture
def expected_genomic_ranges_from_patent():
    return [
        GenomicRange(6480, 1524, None, COLORS.miss, "BglI"),
        GenomicRange(10280, 1524, None, COLORS.miss, "BstXI"),
        GenomicRange(11826, 1524, None, COLORS.miss, "BglI"),
        GenomicRange(17885, 1524, None, COLORS.miss, "BglI"),
        GenomicRange(20854, 1524, None, COLORS.miss, "SfiI"),
        GenomicRange(23112, 1524, None, COLORS.miss, "BglI"),
        GenomicRange(24210, 1524, None, COLORS.miss, "Open reading frame 3 TSE"),
        GenomicRange(24210, 1524, None, COLORS.miss, "ClaI"),
        GenomicRange(25258, 1524, None, COLORS.miss, "PflMI"),
        GenomicRange(25465, 1524, None, COLORS.miss, "ScaI"),
        GenomicRange(25989, 1524, None, COLORS.miss, "AvrII"),
        GenomicRange(26695, 1524, None, COLORS.miss, "EcoNI"),
        GenomicRange(27450, 1524, None, COLORS.miss, "StuI"),
        GenomicRange(27518, 1524, None, COLORS.miss, "Esp3I"),
        GenomicRange(27630, 1524, None, COLORS.miss, "AhdI"),
        GenomicRange(29001, 1524, None, COLORS.miss, "KpnI"),
        GenomicRange(29160, 1524, None, COLORS.miss, "PacI"),
        GenomicRange(29690, 1524, None, COLORS.miss, "SapI"),
        GenomicRange(29699, 1524, None, COLORS.miss, "NotI"),
    ]
