from src.indices import KmerIndex


class ApproximateMatcher:
    def __init__(self, text: str):
        self.text = text

        self.index = None
        self.index_kmer_length = None

    def find_offsets_of_pattern(self, pattern: str, mismatches_allowed: int = 0):
        self._build_index_if_needed(pattern, mismatches_allowed)
        match_offsets = set()

        for which_partition, partition in enumerate(
            self._partitions_of_pattern(pattern, self.index_kmer_length)
        ):
            start_of_partition_within_pattern = which_partition * self.index_kmer_length
            end_of_partition_within_pattern = min(
                (which_partition + 1) * self.index_kmer_length, len(pattern)
            )

            for hit_offset in self._hit_offsets_for_partition(
                pattern, partition, start_of_partition_within_pattern
            ):
                mismatches_left = mismatches_allowed
                for i in range(0, start_of_partition_within_pattern):
                    if (
                        pattern[i]
                        != self.text[hit_offset - start_of_partition_within_pattern + i]
                    ):
                        mismatches_left -= 1
                        if mismatches_left < 0:
                            break
                for i in range(end_of_partition_within_pattern, len(pattern)):
                    if (
                        pattern[i]
                        != self.text[hit_offset - start_of_partition_within_pattern + i]
                    ):
                        mismatches_left -= 1
                        if mismatches_left < 0:
                            break
                if mismatches_left > -1:
                    match_offsets.add(hit_offset - start_of_partition_within_pattern)

        return {
            "match_offsets": sorted(list(match_offsets)),
            "count_of_matches": len(match_offsets),
        }

    def _build_index_if_needed(self, pattern: str, mismatches_allowed: int):
        kmer_length = len(pattern) // (mismatches_allowed + 1)

        if not self.index or kmer_length != self.index_kmer_length:
            self.index_kmer_length = kmer_length
            self.index = KmerIndex(self.text, kmer_length)

    def _partitions_of_pattern(self, pattern: str, kmer_length: int):
        kmer_length = 1 if kmer_length <= 0 else kmer_length

        return [
            pattern[i : i + kmer_length]
            for i in range(0, len(pattern) - kmer_length + 1, kmer_length)
        ]

    def _hit_offsets_for_partition(
        self, pattern, partition, start_of_partition_within_pattern
    ):
        allowed_range_end = len(self.text) - len(pattern) + 1

        return (
            offset
            for offset in self.index.query(partition)
            if offset - start_of_partition_within_pattern > -1
            and offset < allowed_range_end
        )
