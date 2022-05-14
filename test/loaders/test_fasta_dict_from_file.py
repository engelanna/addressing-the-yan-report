class TestFastaDictFromFile:
    def test_only_one_entry(self, sars_cov_2_nc_045512_2):
        expected = 1
        actual = len(sars_cov_2_nc_045512_2.keys())

        assert expected == actual

    def test_length_of_the_only_sequence(self, sars_cov_2_nc_045512_2):
        expected = 29903
        actual = len(list(sars_cov_2_nc_045512_2.values())[0])

        assert expected == actual
