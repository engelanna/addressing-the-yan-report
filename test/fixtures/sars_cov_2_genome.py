from pytest import fixture

from src.loaders import SoleSequenceFromFastaFile
from src.constants.analyses_config import ANALYSES_CONFIG


@fixture
def sars_cov_2_genome():
    return SoleSequenceFromFastaFile()(
        file_path=ANALYSES_CONFIG.common.sars_cov_2_genome_fasta_path
    )
