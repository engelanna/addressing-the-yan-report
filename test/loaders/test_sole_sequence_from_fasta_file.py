from src.loaders import SoleSequenceFromFastaFile


class TestSoleSequenceFromFastaFile:
    def test_length_of_the_only_sequence(self, expected_length=29903):
        actual_length = len(
            SoleSequenceFromFastaFile()("assets/fasta/sars_cov_2_nc_045512.2.fasta")
        )

        assert expected_length == actual_length
