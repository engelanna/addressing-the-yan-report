from src.constants import COLORS
from src.dataclasses import GenomicRange

from pytest import fixture


@fixture
def expected_genomic_ranges_from_patent():
    return [
        GenomicRange(6364, 1495, None, COLORS.miss, "BglI"),
        GenomicRange(10094, 1495, None, COLORS.miss, "BstXI"),
        GenomicRange(11610, 1495, None, COLORS.miss, "BglI"),
        GenomicRange(17555, 1495, None, COLORS.miss, "BglI"),
        GenomicRange(20470, 1495, None, COLORS.miss, "SfiI"),
        GenomicRange(22685, 1495, None, COLORS.miss, "BglI"),
        GenomicRange(
            23760, 1495, None, COLORS.miss, "ORF3A transcription start element"
        ),
        GenomicRange(23760, 1495, None, COLORS.miss, "ClaI"),
        GenomicRange(24791, 1495, None, COLORS.miss, "PflMI"),
        GenomicRange(24992, 1495, None, COLORS.miss, "ScaI"),
        GenomicRange(25506, 1495, None, COLORS.miss, "AvrII"),
        GenomicRange(26201, 1495, None, COLORS.miss, "EcoNI"),
        GenomicRange(26939, 1495, None, COLORS.miss, "StuI"),
        GenomicRange(27006, 1495, None, COLORS.miss, "Esp3I"),
        GenomicRange(27118, 1495, None, COLORS.miss, "Eam1101 (AhdI isoschizomer)"),
        GenomicRange(28461, 1495, None, COLORS.miss, "KpnI"),
        GenomicRange(28618, 1495, None, COLORS.miss, "PacI"),
        GenomicRange(29139, 1495, None, COLORS.miss, "SapI"),
        GenomicRange(29147, 1495, None, COLORS.miss, "NotI"),
    ]
