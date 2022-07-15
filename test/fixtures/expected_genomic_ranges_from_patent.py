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
        GenomicRange(23112, 1524, None, COLORS.miss, text_label="BglI"),
        GenomicRange(24210, 1524, None, COLORS.miss, text_label="ORF3A TSE"),
        GenomicRange(24210, 1524, None, COLORS.miss, text_label="ClaI"),
        GenomicRange(25258, 1524, None, COLORS.miss, text_label="PflMI"),
        GenomicRange(25465, 1524, None, COLORS.miss, text_label="ScaI"),
        GenomicRange(25989, 1524, None, COLORS.miss, text_label="AvrII"),
        GenomicRange(26695, 1524, None, COLORS.miss, text_label="EcoNI"),
        GenomicRange(27450, 1524, None, COLORS.miss, text_label="StuI"),
        GenomicRange(27518, 1524, None, COLORS.miss, text_label="Esp3I"),
        GenomicRange(27630, 1524, None, COLORS.miss, text_label="AhdI"),
        GenomicRange(29001, 1524, None, COLORS.miss, text_label="KpnI"),
        GenomicRange(29160, 1524, None, COLORS.miss, text_label="PacI"),
        GenomicRange(29690, 1524, None, COLORS.miss, text_label="SapI"),
        GenomicRange(29699, 1524, None, COLORS.miss, text_label="NotI"),
    ]
