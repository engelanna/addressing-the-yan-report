from pytest import fixture

from src.dataclasses import SequenceOccurrence
from src.matchers import OccurrencesOfPatternInGenome


class TestOccurrencesOfPatternInGenome:
    @fixture
    def genome(self):
        return "CAGCATCCGATCAGCGATCGATCCCAC"

    def test_exact_matching(self, genome, sequence="CAG"):
        expected = [
            SequenceOccurrence(span=(0, 3), sequence="CAG"),
            SequenceOccurrence(span=(11, 14), sequence="CAG"),
            SequenceOccurrence(span=(24, 27), sequence="CAG"),
        ]
        actual = OccurrencesOfPatternInGenome(genome)(sequence)

        assert expected == actual

    def test_approximate_matching(self, genome, sequence="CNNC"):
        expected = [
            SequenceOccurrence(span=(0, 4), sequence="CAGC"),
            SequenceOccurrence(span=(3, 7), sequence="CATC"),
            SequenceOccurrence(span=(15, 19), sequence="CAGC"),
            SequenceOccurrence(span=(22, 26), sequence="CCAC"),
        ]
        actual = OccurrencesOfPatternInGenome(genome)(sequence)

        assert expected == actual
