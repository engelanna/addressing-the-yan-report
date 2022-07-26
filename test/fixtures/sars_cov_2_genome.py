from pytest import fixture

from src.loaders import SoleSequenceFromFastaFile
from src.constants.analysis_config import ANALYSIS_CONFIG


@fixture
def sars_cov_2_genome():
    return SoleSequenceFromFastaFile()(
        file_path=ANALYSIS_CONFIG.yan_et_al.sars_cov_2_genome_fasta_path
    )
