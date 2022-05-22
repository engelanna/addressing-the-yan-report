from ostruct import OpenStruct


THE_CONFIG = OpenStruct(
    sars_cov_2_structure_diagram=OpenStruct(
        genes_bed_file="assets/bed/sars_cov_2_genes_for_diagram.bed",
        title="SARS-CoV-2 NC_045512 genetic structure",
    ),
    sars_cov_2_genome=OpenStruct(fasta_file_path="assets/fasta/NC_045512.2.fasta"),
)
