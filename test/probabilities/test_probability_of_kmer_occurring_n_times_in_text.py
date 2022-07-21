from src.probabilities import ProbabilityOfKmerOccurringNTimesInText


class TestProbabilityOfKmerOccurringNTimesInText:
    def test_example_from_bioinformatics_algorithms(self):
        expected = 12 / 16
        actual = ProbabilityOfKmerOccurringNTimesInText(alphabet_size=2)(
            text_length=4, kmer_length=2, kmer_occurrence_count=1
        )

        assert expected == actual

    def test_four_of_the_same_letter_in_four_letter_text(self):
        expected = (1 / 4) ** 4
        actual = ProbabilityOfKmerOccurringNTimesInText(alphabet_size=4)(
            text_length=4, kmer_length=1, kmer_occurrence_count=4
        )

        assert expected == actual
