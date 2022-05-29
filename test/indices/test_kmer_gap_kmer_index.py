from pytest import fixture

from src.indices import KmerGapKmerIndex


class TestSubsequenceIndex:
    @fixture
    def human_alu(self):
        return "GGCGCGGTGGCTCACGCCTGTAAT"

    @fixture
    def subsequence_length(self):
        return 8

    @fixture
    def step(self):
        return 3

    def test_short_excerpt_matches(
        self,
        pattern="to-morrow and to-morrow ",
        text="to-morrow and to-morrow and to-morrow creeps in this petty pace",
    ):
        matches = KmerGapKmerIndex(text=text, kmer_length=8, step=3).query(pattern)[0]

        assert matches == [0, 14]

    def test_short_excerpt_total_hits(
        self,
        pattern="to-morrow and to-morrow ",
        text="to-morrow and to-morrow and to-morrow creeps in this petty pace",
    ):
        hit_count = KmerGapKmerIndex(text=text, kmer_length=8, step=3).query(pattern)[1]
        assert hit_count == 6

    def test_how_many_times_alu_matches_human_chromosome1(
        self, human_chromosome_1, human_alu
    ):
        matches = KmerGapKmerIndex(
            text=human_chromosome_1, kmer_length=8, step=3
        ).query(human_alu)[0]

        assert matches == [
            56922,
            84641,
            147558,
            191452,
            262042,
            273669,
            364263,
            465647,
            635931,
            657496,
            681737,
            717706,
            747359,
        ]

    def test_index_hits_while_matching_alu_to_human_chromosome1(
        self, human_chromosome_1, human_alu
    ):
        hit_count = KmerGapKmerIndex(
            text=human_chromosome_1, kmer_length=8, step=3
        ).query(human_alu)[1]

        assert hit_count == 79
