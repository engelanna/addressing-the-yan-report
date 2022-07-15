from src.probabilities import ProbabilityOfKmerOccurringNTimesInText


class TestProbabilityOfKmerOccurringNTimesInText:
    def test(self):
        expected = (1 / 4) ** 4
        actual = ProbabilityOfKmerOccurringNTimesInText(alphabet_size=4)(
            text_length=4, kmer_length=1, kmer_occurrence_count=4
        )

        assert expected == actual
