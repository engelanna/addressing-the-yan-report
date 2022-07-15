from ostruct import OpenStruct

SARS_COV_2_ACCESSION = "MN908947.1"

THE_CONFIG = OpenStruct(
    sars_cov_2_structure_diagram=OpenStruct(
        genes_bed_file="assets/bed/sars_cov_2_genes_for_diagram.bed",
        title=f"SARS-CoV-2 (accession {SARS_COV_2_ACCESSION}) genetic structure",
    ),
    genome_under_test=OpenStruct(
        fasta_file_path=f"assets/fasta/{SARS_COV_2_ACCESSION}.fasta"
    ),
)
