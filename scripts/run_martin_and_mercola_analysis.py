from dataclasses import astuple
from matplotlib import pyplot as plt
from ostruct import OpenStruct

from .config_the_analyses import THE_CONFIG
from src.genome_browser_overrides import (
    DiagramRow,
    OverridenGenomeDiagram,
)
from src.genomic_range_builders import BuildGenomicRangeList
from src.loaders import SoleSequenceFromFastaFile
from src.restriction_enzyme_marks import RunBatteryOfRangeTests


sars_cov_2_structure_row = DiagramRow(
    THE_CONFIG.sars_cov_2_structure_diagram.title, height_ratio=0.4
)
[
    sars_cov_2_structure_row.add_feature(astuple(genomic_range))
    for genomic_range in BuildGenomicRangeList().from_sars_cov_2_bed_file(
        THE_CONFIG.sars_cov_2_structure_diagram.genes_bed_file
    )
]

restriction_enzymes_row = DiagramRow(
    f"Restriction enzymes",
    height_ratio=0.4,
    drawing_config=OpenStruct(fill_polygons=True, annotation_color="black"),
)
[
    restriction_enzymes_row.add_feature(astuple(genomic_range))
    for genomic_range in RunBatteryOfRangeTests()(
        genome=SoleSequenceFromFastaFile()(
            THE_CONFIG.genome_under_test.fasta_file_path
        ),
        mismatches_allowed=1,
    )
]


diagram = OverridenGenomeDiagram()
diagram.add_track(sars_cov_2_structure_row)
diagram.add_track(restriction_enzymes_row)

# Annotate the figure with interval specific metadata. Will always appear in lower-right
diagram.annotation = "{}:{:,}-{:,}".format("chr3", 20000, 812383)
fig, axes = diagram.draw()
plt.show()
