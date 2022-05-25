from pytest import fixture

from src.indices import KmerIndex


class TestKmerIndex:
    @fixture
    def subject(self, human_chromosome_1):
        return KmerIndex(genome=human_chromosome_1, kmer_length=24)

    @fixture
    def human_alu(self):
        return "GGCGCGGTGGCTCACGCCTGTAAT"

    @fixture
    def expected_match_indices(self):
        return [
            56922,
            262042,
            364263,
            657496,
            717706,
        ]

    def test_hit_offsets(self, subject, human_alu, expected_match_indices):
        actual_match_indices = subject.query(pattern=human_alu)

        assert expected_match_indices == actual_match_indices

    def test_hit_count(
        self,
        subject,
        human_alu,
    ):
        hits = subject.query(pattern=human_alu)

        assert 5 == len(hits)
