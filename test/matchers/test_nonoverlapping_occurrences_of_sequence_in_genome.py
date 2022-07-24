from pytest import fixture

from src.dataclasses import SequenceOccurrence
from src.matchers import NonoverlappingOccurrencesOfSequenceInGenome


class TestNonoverlappingOccurrencesOfSequenceInGenome:
    @fixture
    def genome(self):
        return "CAGCATCCGATCAGCGATCGATCCCAC"

    def test_exact_matching(self, genome, sequence="CAG"):
        expected = [
            SequenceOccurrence(
                span=(0, 3), sequence_sought="CAG", sequence_found="CAG"
            ),
            SequenceOccurrence(
                span=(11, 14), sequence_sought="CAG", sequence_found="CAG"
            ),
        ]
        actual = NonoverlappingOccurrencesOfSequenceInGenome(genome)(sequence)

        assert expected == actual

    def test_approximate_matching(self, genome, sequence="CNNC"):
        expected = [
            SequenceOccurrence(
                span=(0, 4), sequence_sought="CNNC", sequence_found="CAGC"
            ),
            SequenceOccurrence(
                span=(11, 15), sequence_sought="CNNC", sequence_found="CAGC"
            ),
            SequenceOccurrence(
                span=(23, 27), sequence_sought="CNNC", sequence_found="CCAC"
            ),
        ]
        actual = NonoverlappingOccurrencesOfSequenceInGenome(genome)(sequence)

        assert expected == actual
