from pytest import fixture

from src.genomic_ranges import BuildGenomicRangeList


class TestBuildGenomicRangeList:
    @fixture
    def expected_output_for_locations_from_patent(self):
        return [
            (6364, 1495, None, "#E74C3C"),
            (10094, 1495, None, "#E74C3C"),
            (11610, 1495, None, "#E74C3C"),
            (17555, 1495, None, "#E74C3C"),
            (20470, 1495, None, "#E74C3C"),
            (22685, 1495, None, "#E74C3C"),
            (23760, 1495, None, "#E74C3C"),
            (23760, 1495, None, "#E74C3C"),
            (24791, 1495, None, "#E74C3C"),
            (24992, 1495, None, "#E74C3C"),
            (25506, 1495, None, "#E74C3C"),
            (26201, 1495, None, "#E74C3C"),
            (26939, 1495, None, "#E74C3C"),
            (27006, 1495, None, "#E74C3C"),
            (27118, 1495, None, "#E74C3C"),
            (28461, 1495, None, "#E74C3C"),
            (28618, 1495, None, "#E74C3C"),
            (29139, 1495, None, "#E74C3C"),
            (29147, 1495, None, "#E74C3C"),
        ]

    def test_building_from_locations_in_patent(
        self,
        expected_output_for_locations_from_patent,
        len_genome=29903,
        genome_length_tolerance=0.05,
    ):
        actual_output = BuildGenomicRangeList().from_locations_in_patent(
            len_genome, genome_length_tolerance
        )

        assert expected_output_for_locations_from_patent == actual_output

    @fixture
    def expected_output_from_sars_cov_2_bed_file(self):
        return [
            (0, 265, "+", "#E74C3C"),
            (265, 21290, "+", "#E74C3C"),
            (21562, 3822, "+", "#E74C3C"),
            (25392, 828, "+", "#E74C3C"),
            (26244, 228, "+", "#E74C3C"),
            (26522, 669, "+", "#E74C3C"),
            (27201, 186, "+", "#E74C3C"),
            (27393, 366, "+", "#E74C3C"),
            (27755, 132, "+", "#E74C3C"),
            (27893, 366, "+", "#E74C3C"),
            (28273, 1260, "+", "#E74C3C"),
            (29557, 117, "+", "#E74C3C"),
            (29674, 229, "+", "#E74C3C"),
        ]

    def test_building_from_sars_cov_2_bed_file(
        self,
        expected_output_from_sars_cov_2_bed_file,
        bed_file_path="assets/bed/genes_sars_cov_2_nc_045512.2.bed",
    ):
        actual_output = BuildGenomicRangeList().from_bed_file(bed_file_path)

        assert expected_output_from_sars_cov_2_bed_file == actual_output
