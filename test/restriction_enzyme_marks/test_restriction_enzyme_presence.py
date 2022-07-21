from pytest import fixture

from src.dataclasses import RestrictionEnzyme
from src.restriction_enzyme_marks import RestrictionEnzymePresence


class TestRestrictionEnzymePresence:
    @fixture
    def ecori(self):
        return RestrictionEnzyme(
            start_at_fraction_genome_length=0.06,  # actually at 3.8% (not 6%)
            name="EcoRI",
            sequence="GAATTC",
        )

    def test_presence_within_tolerance(self, sars_cov_2_genome, ecori, tolerance=0.05):
        actual = RestrictionEnzymePresence()(sars_cov_2_genome, ecori, tolerance)

        assert True == actual

    def test_absence_within_tolerance(self, sars_cov_2_genome, ecori, tolerance=0.025):
        actual = RestrictionEnzymePresence()(sars_cov_2_genome, ecori, tolerance)

        assert False == actual
