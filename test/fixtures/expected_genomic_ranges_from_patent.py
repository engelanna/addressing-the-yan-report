from src.dataclasses import GenomicRange

from pytest import fixture


@fixture
def expected_genomic_ranges_from_patent():
    return [
        GenomicRange(6364, 1495, None, "#E74C3C", "BglI"),
        GenomicRange(10094, 1495, None, "#E74C3C", "BstXI"),
        GenomicRange(11610, 1495, None, "#E74C3C", "BglI"),
        GenomicRange(17555, 1495, None, "#E74C3C", "BglI"),
        GenomicRange(20470, 1495, None, "#E74C3C", "SfiI"),
        GenomicRange(22685, 1495, None, "#E74C3C", "BglI"),
        GenomicRange(23760, 1495, None, "#E74C3C", "ORF3A transcription start element"),
        GenomicRange(23760, 1495, None, "#E74C3C", "ClaI"),
        GenomicRange(24791, 1495, None, "#E74C3C", "PflMI"),
        GenomicRange(24992, 1495, None, "#E74C3C", "ScaI"),
        GenomicRange(25506, 1495, None, "#E74C3C", "AvrII"),
        GenomicRange(26201, 1495, None, "#E74C3C", "EcoNI"),
        GenomicRange(26939, 1495, None, "#E74C3C", "StuI"),
        GenomicRange(27006, 1495, None, "#E74C3C", "Esp3I"),
        GenomicRange(27118, 1495, None, "#E74C3C", "Eam1101 (AhdI isoschizomer)"),
        GenomicRange(28461, 1495, None, "#E74C3C", "KpnI"),
        GenomicRange(28618, 1495, None, "#E74C3C", "PacI"),
        GenomicRange(29139, 1495, None, "#E74C3C", "SapI"),
        GenomicRange(29147, 1495, None, "#E74C3C", "NotI"),
    ]
