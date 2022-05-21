from pytest import fixture

from src.dataclasses import SequenceOccurrence
from src.matchers import OccurrencesOfPatternInGenome


class TestOccurrencesOfPatternInGenome:
    @fixture
    def genome(self):
        return "CAGGATCCGATCAGCGATCGATCGCAG"

    def test_exact_matching(self, genome, sequence="CAG"):
        expected = [
            SequenceOccurrence(span=(0, 3), sequence="CAG"),
            SequenceOccurrence(span=(11, 14), sequence="CAG"),
            SequenceOccurrence(span=(24, 27), sequence="CAG"),
        ]
        actual = OccurrencesOfPatternInGenome(genome)(sequence)

        assert expected == actual

    def test_approximate_matching(self, genome, sequence="CAGA"):
        expected = [
            SequenceOccurrence(span=(0, 3), sequence="CAG"),
            SequenceOccurrence(span=(11, 14), sequence="CAG"),
            SequenceOccurrence(span=(24, 27), sequence="CAG"),
        ]
        actual = OccurrencesOfPatternInGenome(genome)(sequence)

        assert expected == actual
