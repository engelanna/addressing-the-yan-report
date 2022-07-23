from ostruct import OpenStruct

_common_annotation = "ORF = Open Reading Frame (region between start & end sites of RNA>protein translation"

ANALYSES_CONFIG = OpenStruct(
    martin_and_mercola=OpenStruct(
        diagram_title="SARS-CoV-1 (accession MN908947.1) genes",
        sars_cov_1_gene_ranges_bed_file_path="assets/bed/sars_cov_1_genes_for_diagram bed",
        sars_cov_1_genome_fasta_path="assets/fasta/sars_cov_1_NC_004718.3.fasta",
        diagram_annotation=_common_annotation,
    ),
    yan_et_al=OpenStruct(
        diagram_title=(
            "Sequences identical to EcoRI or BstEII in the SARS-CoV-2 genome (accession MN908947.1)"
        ),
        sars_cov_2_gene_ranges_bed_file_path="assets/bed/sars_cov_2_genes_for_diagram.bed",
        sars_cov_2_genome_fasta_path="assets/fasta/sars_cov_2_MN908947.1.fasta",
        diagram_annotation=_common_annotation,
    ),
)
