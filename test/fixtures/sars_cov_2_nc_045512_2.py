from pytest import fixture

from src.loaders import FastaDictFromFile


@fixture
def sars_cov_2_nc_045512_2():
    return FastaDictFromFile("assets/fasta/sars_cov_2_nc_045512.2.fasta")()
