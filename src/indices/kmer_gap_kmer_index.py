import bisect


class KmerGapKmerIndex:
    """Create index from subsequences of the form xx___xx, where:
    kmer_length: describes how many 'x' are at either end (2 in the example)
    gap: describes how any characters are skipped in the '__' portion (3 in the example)
    """

    def __init__(self, text, kmer_length, gap_length, mismatches_allowed=2):
        self.kmer_length = kmer_length
        self.gap_length = gap_length
        self.mismatches_allowed = mismatches_allowed
        self.text = text
        self.index = self._prepare_index(text)

    def query(self, pattern):
        matches = set()
        total_hits = 0

        for partition in self._create_queries_from_pattern(pattern):
            hits = self._fetch(partition)
            total_hits += len(hits)

            for hit in hits:
                mismatches_left = self.mismatches_allowed

                for i in range(len(pattern)):
                    if i % self.gap_length == 0:
                        continue
                    elif pattern[i] != self.text[hit + i]:
                        mismatches_left -= 1

                if mismatches_left > -1:
                    matches.add(hit)

        return (sorted(list(matches)), total_hits)

    def _fetch(self, subsequence):
        """Return index hits for first subseq of p"""
        i = bisect.bisect_left(self.index, (subsequence, -1))  # binary search
        hits = []
        while i < len(self.index):  # collect matching index entries
            if self.index[i][0] != subsequence:
                break
            hits.append(self.index[i][1])
            i += 1
        return hits

    def _prepare_index(self, text):
        index = []

        self.span = 1 + self.gap_length * (self.kmer_length - 1)
        for i in range(len(text) - self.span + 1):  # for each subseq
            index.append(
                (text[i : i + self.span : self.gap_length], i)
            )  # add (subseq, offset)
        index.sort()  # alphabetize by subseq

        return index

    def _create_queries_from_pattern(self, pattern):
        return [pattern[i :: self.gap_length] for i in range(self.gap_length)]
