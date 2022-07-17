from ostruct import OpenStruct

ANALYSES_CONFIG = OpenStruct(
    common=OpenStruct(
        sars_cov_2_gene_ranges_bed_file_path="assets/bed/sars_cov_2_genes_for_diagram.bed",
        sars_cov_2_genome_fasta_path="assets/fasta/MN908947.1.fasta",
    ),
    martin_and_mercola=OpenStruct(
        diagram_title="M&M TITLE SARS-CoV-2 (accession MN908947.1) genes",
    ),
    yan_et_al=OpenStruct(
        diagram_title="YAN TITLE SARS-CoV-2 (accession MN908947.1) genes",
    ),
)
