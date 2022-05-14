from . import FastaDictFromFile


class NcbiVirusLoader:
    def __call__(self):
        entries = FastaDictFromFile("assets/fasta/sars_cov_2_nc_045512.2.fasta")()

        return list(entries.values())[0]
