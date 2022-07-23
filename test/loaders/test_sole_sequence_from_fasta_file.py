from pytest import raises
from src.loaders import SoleSequenceFromFastaFile
from src.constants.analyses_config import ANALYSES_CONFIG


class TestSoleSequenceFromFastaFile:
    def test_length_of_the_only_sequence(
        self,
        file_path=ANALYSES_CONFIG.yan_et_al.sars_cov_2_genome_fasta_path,
        expected_length=30473,
    ):
        actual_length = len(SoleSequenceFromFastaFile()(file_path))

        assert expected_length == actual_length

    def test_prohibit_multiple_fasta_sequences(
        self, file_path="assets/fasta/illegal.fasta"
    ):
        with raises(AssertionError, match="Only 1 sequence allowed in the FASTA file"):
            SoleSequenceFromFastaFile()(file_path)
