from pytest import fixture

from src.loaders import SoleSequenceFromFastaFile


@fixture
def human_chromosome_1():
    return SoleSequenceFromFastaFile()("assets/fasta/chr1.GRCh38.excerpt.fasta")
