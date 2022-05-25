from pytest import raises
from src.loaders import SoleSequenceFromFastaFile
from scripts.config_the_analysis import THE_CONFIG


class TestSoleSequenceFromFastaFile:
    def test_length_of_the_only_sequence(
        self,
        file_path=THE_CONFIG.genome_under_test.fasta_file_path,
        expected_length=29903,
    ):
        actual_length = len(SoleSequenceFromFastaFile()(file_path))

        assert expected_length == actual_length

    def test_prohibit_multiple_fasta_sequences(
        self, file_path="assets/fasta/illegal.fasta"
    ):
        with raises(AssertionError, match="Only 1 sequence allowed in the FASTA file"):
            SoleSequenceFromFastaFile()(file_path)
