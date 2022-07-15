from math import comb


class ProbabilityOfKmerOccurringNTimesInText:
    def __init__(self, alphabet_size: int):
        self.alphabet_size = 4

    def __call__(self, text_length: int, kmer_length: int, kmer_occurrence_count: int):
        count_of_ways_to_intersect_n_occurences_of_kmer_with_text_length = (
            text_length - kmer_occurrence_count * kmer_length
        )

        return (
            comb(  # number of combinations
                count_of_ways_to_intersect_n_occurences_of_kmer_with_text_length
                + kmer_occurrence_count,
                kmer_occurrence_count,
            )
            * pow(
                self.alphabet_size,
                count_of_ways_to_intersect_n_occurences_of_kmer_with_text_length,
            )
            / pow(self.alphabet_size, text_length)
        )
