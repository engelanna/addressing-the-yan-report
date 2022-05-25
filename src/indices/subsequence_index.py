import bisect


class SubsequenceIndex:
    """Create index from all subsequences consisting of k characters
    spaced ival positions apart.  E.g., SubseqIndex("ATAT", 2, 2)
    extracts ("AA", 0) and ("TT", 1)."""

    def __init__(self, text, subsequence_length, step, mismatches_allowed=2):
        self.subsequence_length = subsequence_length
        self.step = step  # 1=adjacent, 2=every other, etc
        self.mismatches_allowed = mismatches_allowed
        self.text = text
        self.index = self._prepare_index(text)

    PATTERN_LENGTH = 24

    def query(self, pattern):
        assert len(pattern) == self.PATTERN_LENGTH

        matches = set()
        total_hits = 0

        for partition in self._subsequences_for_pattern(pattern):
            hits = self._fetch(partition)
            total_hits += len(hits)

            for hit in hits:
                mismatches_left = self.mismatches_allowed

                for i in range(len(pattern)):
                    if i % self.step == 0:
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

        self.span = 1 + self.step * (self.subsequence_length - 1)
        for i in range(len(text) - self.span + 1):  # for each subseq
            index.append(
                (text[i : i + self.span : self.step], i)
            )  # add (subseq, offset)
        index.sort()  # alphabetize by subseq

        return index

    def _subsequences_for_pattern(self, pattern):
        return [pattern[i :: self.step] for i in range(self.step)]
