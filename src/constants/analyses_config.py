from ostruct import OpenStruct

ANALYSES_CONFIG = OpenStruct(
    yan_et_al=OpenStruct(
        diagram_title=(
            "Sequences identical to EcoRI or BstEII in the SARS-CoV-2 genome (accession MN908947.1)"
        ),
        sars_cov_2_gene_ranges_bed_file_path="assets/bed/sars_cov_2_genes_for_diagram.bed",
        sars_cov_2_genome_fasta_path="assets/fasta/sars_cov_2_MN908947.1.fasta",
    ),
)
