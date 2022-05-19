from pytest import fixture

from src.dataclasses import GenomicRange


@fixture
def expected_genomic_ranges_from_sars_cov_2_bed_file():
    return [
        GenomicRange(0, 265, "+", "#E74C3C", "5' UTR"),
        GenomicRange(265, 21290, "+", "#E74C3C", "ORF1ab"),
        GenomicRange(21562, 3822, "+", "#E74C3C", "S"),
        GenomicRange(25392, 828, "+", "#E74C3C", "ORF3a"),
        GenomicRange(26244, 228, "+", "#E74C3C", "E"),
        GenomicRange(26522, 669, "+", "#E74C3C", "M"),
        GenomicRange(27201, 186, "+", "#E74C3C", "ORF6"),
        GenomicRange(27393, 366, "+", "#E74C3C", "ORF7a"),
        GenomicRange(27755, 132, "+", "#E74C3C", "ORF7b"),
        GenomicRange(27893, 366, "+", "#E74C3C", "ORF8"),
        GenomicRange(28273, 1260, "+", "#E74C3C", "N"),
        GenomicRange(29557, 117, "+", "#E74C3C", "ORF10"),
        GenomicRange(29674, 229, "+", "#E74C3C", "3' UTR"),
    ]
