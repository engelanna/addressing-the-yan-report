from pytest import fixture
from src.matchers import ApproximateMatcher


class TestApproximateMatcher:
    @fixture
    def pattern(self):
        return "ATTCTGGA"

    @fixture
    def text(self):
        return "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT"

    @fixture
    def max_mismatches(self):
        return 3

    def test_offsets(self, pattern, text, max_mismatches):
        expected_offsets = [6, 7, 26, 27]
        actual_offsets = ApproximateMatcher(text).find_offsets_of_pattern(
            pattern, max_mismatches
        )["match_offsets"]

        assert expected_offsets == actual_offsets

    def test_hits_count(self, pattern, text, max_mismatches):
        expected_hits_count = 4
        actual_hits_count = ApproximateMatcher(text).find_offsets_of_pattern(
            pattern, max_mismatches
        )["count_of_matches"]

        assert expected_hits_count == actual_hits_count

    def test_matches_at_the_very_beginning(self):
        expected_hits_count = 11
        actual_hits_count = ApproximateMatcher(
            "AACAAGCTGATAAACATTTAAAGAG"
        ).find_offsets_of_pattern("AAAAA", 2)["count_of_matches"]

        assert expected_hits_count == actual_hits_count

    def test_ignoring_instances_with_less_than_max_mismatches(
        self, text="TTTTTTAAATTTTAAATTTTTT", pattern="AAA", max_mismatches=2
    ):
        actual_offsets = ApproximateMatcher(text).find_offsets_of_pattern(
            pattern, max_mismatches
        )["match_offsets"]

        assert [4, 5, 6, 7, 8, 11, 12, 13, 14, 15] == actual_offsets

    def test_no_off_by_one_error_at_the_beginning(
        self,
        text=(
            "GAGCGCTGGGTTAACTCGCTACTTCCCGACGAGCGCTGTGGCGCAAATTGGCGATGA"
            "AACTGCAGAGAGAACTGGTCATCCAACTGAATTCTCCCCGCTATCGCATTTTGATGC"
            "GCGCCGCGTCGATT"
        ),
        pattern="GAGCGCTGG",
        max_mismatches=2,
    ):
        actual_offsets = ApproximateMatcher(text).find_offsets_of_pattern(
            pattern, max_mismatches
        )["match_offsets"]

        assert [0, 30, 66] == actual_offsets

    def test_no_off_by_one_error_at_the_end(
        self,
        text=(
            "CCAAATCCCCTCATGGCATGCATTCCCGCAGTATTTAATCCTTTCATTCTGCATATAA"
            "GTAGTGAAGGTATAGAAACCCGTTCAAGCCCGCAGCGGTAAAACCGAGAACCATGA"
            "TGAATGCACGGCGATTGCGCCATAATCCAAACA"
        ),
        pattern="AATCCTTTCA",
        max_mismatches=3,
    ):
        actual_offsets = ApproximateMatcher(text).find_offsets_of_pattern(
            pattern, max_mismatches
        )["match_offsets"]

        assert [3, 36, 74, 137] == actual_offsets

    def test_counting_overlaps_correctly(
        self,
        text=(
            "CCGTCATCCGTCATCCTCGCCACGTTGGCATGCATTCCGTCATCCCGTCAGGCATACT"
            "TCTGCATATAAGTACAAACATCCGTCATGTCAAAGGGAGCCCGCAGCGGTAAAACC"
            "GAGAACCATGATGAATGCACGGCGATTGC"
        ),
        pattern="CCGTCATCC",
        max_mismatches=3,
    ):
        actual_offsets = ApproximateMatcher(text).find_offsets_of_pattern(
            pattern, max_mismatches
        )["match_offsets"]

        assert [0, 7, 36, 44, 48, 72, 79, 112] == actual_offsets

    def test_not_only_counting_below_max_mismatches(
        self,
        text="AAAAAA",
        pattern="TTT",
        max_mismatches=3,
    ):
        actual_offsets = ApproximateMatcher(text).find_offsets_of_pattern(
            pattern, max_mismatches
        )["match_offsets"]

        assert [0, 1, 2, 3] == actual_offsets

    def test_only_perfect_matches_mode(
        self, text="CCACCT", pattern="CCA", max_mismatches=0
    ):
        actual_offsets = ApproximateMatcher(text).find_offsets_of_pattern(
            pattern, max_mismatches
        )["match_offsets"]

        assert [0] == actual_offsets
