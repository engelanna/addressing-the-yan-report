from src.builders.genomic_range_builders import BuildGenomicRangeList
from src.constants.analyses_config import ANALYSES_CONFIG


class TestBuildGenomicRangeList:
    def test_building_from_bed_file(
        self,
        expected_genomic_ranges_from_sars_cov_2_bed_file,
        bed_file_path=ANALYSES_CONFIG.yan_et_al.sars_cov_2_gene_ranges_bed_file_path,
    ):
        actual_output = BuildGenomicRangeList().from_bed_file(bed_file_path)

        assert expected_genomic_ranges_from_sars_cov_2_bed_file == actual_output
