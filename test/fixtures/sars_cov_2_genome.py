from pytest import fixture

from src.loaders import SoleSequenceFromFastaFile
from src.constants.analyses_config import ANALYSES_CONFIG


@fixture
def sars_cov_2_genome():
    return SoleSequenceFromFastaFile()(
        file_path=ANALYSES_CONFIG.genome_under_test.fasta_file_path
    )
