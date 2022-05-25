import bisect
from typing import (
    List,
    Range,
)

from . import SignatureToRangeList


class SubsequenceIndex:
    """Create index from all subsequences matching a signature like "x___x", where:
    "x" marks a position to be included (+) in the index
    "_" marks a position to be excluded (-) from the index

    All the other literals are illegal.

    Valid signature examples:
    xx__xx, x_x_x, x___xx

    Leading and trailing "_" will be automatically ignored ("___x_xx__" becomes "x_xx").
    """

    def __init__(self, text, signature, mismatches_allowed=2):
        self.text = text
        self.mismatches_allowed = mismatches_allowed

        if set(signature) != {"x", "_"}:
            raise TypeError("Signature may only consist of 'x' and '_'")
        else:
            self.signature = signature.strip("_")
            self.ranges_to_store = SignatureToRangeList()(self.signature)

        self.index = self._prepare_index(text, self.ranges_to_store)

    def query(self, pattern):
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

    def _prepare_index(self, text: str, signature: str, ranges: List[Range]):
        index = []

        for i in range(len(text) - len(signature) + 1):  # for each subseq

            new_entry = ""
            for range in ranges:
                new_entry += text[int(range.start) : int(range.stop)]

            index.append((new_entry, i))  # add (subseq, offset)
        index.sort()  # alphabetize by subseq

        return index

    def _subsequences_for_pattern(self, pattern):
        return [pattern[i :: self.step] for i in range(self.step)]
