from pytest import fixture

from src.dataclasses import RestrictionEnzyme
from src.restriction_enzyme_marks import RestrictionEnzymePresence


class TestRestrictionEnzymePresence:
    @fixture
    def mock_restriction_enzyme(self):
        return RestrictionEnzyme(
            start_at_fraction_genome_length=0.5,
            name="Not a real restriction enzyme, but good enough for test purposes",
            sequence="CATNNNNNNACT",
        )

    def test_presence_within_tolerance(
        self, sars_cov_2_genome, mock_restriction_enzyme, tolerance=0.05
    ):
        actual = RestrictionEnzymePresence()(
            sars_cov_2_genome, mock_restriction_enzyme, tolerance
        )
        assert True == actual

    def test_absence_within_tolerance(
        self, sars_cov_2_genome, mock_restriction_enzyme, tolerance=0.025
    ):
        actual = RestrictionEnzymePresence()(
            sars_cov_2_genome, mock_restriction_enzyme, tolerance
        )
        assert False == actual
