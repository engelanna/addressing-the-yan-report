import bisect


class KmerIndex:
    """A queryable index of substrings of length k.
    The substrings come from the genome you pass to the constructor.
    """

    def __init__(
        self,
        genome: str,
        kmer_length: int = 30,
    ):
        self.genome = genome
        self.kmer_length = kmer_length

        self.index = self._build_the_index()

    def query(self, pattern: str) -> list:
        """Return index hits for first k-mer of pattern"""
        kmer = pattern[: self.kmer_length]  # query with first k-mer
        i = bisect.bisect_left(self.index, (kmer, -1))  # binary search

        hits = []
        while i < len(self.index):  # collect matching index entries
            if self.index[i][0] != kmer:
                break
            hits.append(self.index[i][1])
            i += 1
        return hits

    def _build_the_index(self) -> list:
        """Create index from all k-length substrings of genome"""
        index = []

        range_of_all_possible_matches = range(len(self.genome) - self.kmer_length + 1)

        for i in range_of_all_possible_matches:
            index.append(
                (self.genome[i : i + self.kmer_length], i)
            )  # add (k-mer, offset) pair
        index.sort()  # alphabetize by k-mer

        return index
