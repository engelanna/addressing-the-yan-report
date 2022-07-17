from ostruct import OpenStruct

ANALYSES_CONFIG = OpenStruct(
    sars_cov_2_structure_diagram=OpenStruct(
        genes_bed_file="assets/bed/sars_cov_2_genes_for_diagram.bed",
        title="SARS-CoV-2 (accession MN908947.1) genes",
    ),
    genome_under_test=OpenStruct(fasta_file_path="assets/fasta/MN908947.1.fasta"),
)
