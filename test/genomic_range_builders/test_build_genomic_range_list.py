from src.genomic_range_builders import BuildGenomicRangeList
from scripts.config_the_analyses import THE_CONFIG


class TestBuildGenomicRangeList:
    def test_building_from_locations_in_patent(
        self,
        expected_genomic_ranges_from_patent,
        sars_cov_2_genome,
        genome_length_tolerance=0.05,
    ):
        actual_output = BuildGenomicRangeList().from_locations_in_patent(
            sars_cov_2_genome, genome_length_tolerance
        )

        assert expected_genomic_ranges_from_patent == actual_output

    def test_building_from_sars_cov_2_bed_file(
        self,
        expected_genomic_ranges_from_sars_cov_2_bed_file,
        bed_file_path=THE_CONFIG.sars_cov_2_structure_diagram.genes_bed_file,
    ):
        actual_output = BuildGenomicRangeList().from_sars_cov_2_bed_file(bed_file_path)

        assert expected_genomic_ranges_from_sars_cov_2_bed_file == actual_output
