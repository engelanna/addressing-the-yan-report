from ostruct import OpenStruct


THE_CONFIG = OpenStruct(
    sars_cov_2_structure_diagram=OpenStruct(
        genes_bed_file="assets/bed/sars_cov_2_genes_for_diagram.bed",
        title="SARS-CoV-2 NC_045512 genetic structure",
    ),
    genome_under_test=OpenStruct(fasta_file_path="assets/fasta/MN908947.3.fasta"),
)
