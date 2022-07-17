from math import comb


class ProbabilityOfKmerOccurringNTimesInText:
    def __init__(self, alphabet_size: int = 4):
        self.alphabet_size = alphabet_size

    def __call__(self, text_length: int, kmer_length: int, kmer_occurrence_count: int):
        count_of_ways_to_intersect_n_occurrences_of_kmer_with_text = (
            text_length - kmer_occurrence_count * kmer_length
        )

        return (
            comb(  # number of combinations
                count_of_ways_to_intersect_n_occurrences_of_kmer_with_text
                + kmer_occurrence_count,
                kmer_occurrence_count,
            )
            * pow(
                self.alphabet_size,
                count_of_ways_to_intersect_n_occurrences_of_kmer_with_text,
            )
            / pow(self.alphabet_size, text_length)
        )
