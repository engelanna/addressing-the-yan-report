from pytest import fixture

from src.loaders import SoleSequenceFromFastaFile
from scripts.config_the_analyses import THE_CONFIG


@fixture
def sars_cov_2_genome():
    return SoleSequenceFromFastaFile()(
        file_path=THE_CONFIG.genome_under_test.fasta_file_path
    )
