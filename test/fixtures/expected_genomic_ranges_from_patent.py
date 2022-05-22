from src.constants import COLORS
from src.dataclasses import GenomicRange

from pytest import fixture


@fixture
def expected_genomic_ranges_from_patent():
    return [
        GenomicRange(6359, 1495, None, COLORS.miss, "BglI"),
        GenomicRange(10088, 1495, None, COLORS.miss, "BstXI"),
        GenomicRange(11605, 1495, None, COLORS.miss, "BglI"),
        GenomicRange(17550, 1495, None, COLORS.miss, "BglI"),
        GenomicRange(20464, 1495, None, COLORS.miss, "SfiI"),
        GenomicRange(22680, 1495, None, COLORS.miss, "BglI"),
        GenomicRange(
            23757, 1495, None, COLORS.miss, "ORF3A transcription start element"
        ),
        GenomicRange(23757, 1495, None, COLORS.miss, "ClaI"),
        GenomicRange(24786, 1495, None, COLORS.miss, "PflMI"),
        GenomicRange(24989, 1495, None, COLORS.miss, "ScaI"),
        GenomicRange(25503, 1495, None, COLORS.miss, "AvrII"),
        GenomicRange(26196, 1495, None, COLORS.miss, "EcoNI"),
        GenomicRange(26936, 1495, None, COLORS.miss, "StuI"),
        GenomicRange(27003, 1495, None, COLORS.miss, "Esp3I"),
        GenomicRange(27113, 1495, None, COLORS.miss, "Eam1101 (AhdI isoschizomer)"),
        GenomicRange(28458, 1495, None, COLORS.miss, "KpnI"),
        GenomicRange(28614, 1495, None, COLORS.miss, "PacI"),
        GenomicRange(29135, 1495, None, COLORS.miss, "SapI"),
        GenomicRange(29143, 1495, None, COLORS.miss, "NotI"),
    ]
