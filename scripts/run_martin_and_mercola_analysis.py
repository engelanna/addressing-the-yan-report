from dataclasses import astuple
from matplotlib import pyplot as plt

from src.constants.analyses_config import ANALYSES_CONFIG
from src.genome_browser_overrides import (
    DiagramRow,
    OverridenGenomeDiagram,
)
from src.builders.genomic_range_builders import BuildGenomicRangeList
from src.loaders import SoleSequenceFromFastaFile
from src.restriction_enzyme_marks import RunBatteryOfRangeTests


sars_cov_2_structure_row = DiagramRow(
    ANALYSES_CONFIG.martin_and_mercola.diagram_title, height_ratio=0.4
)
[
    sars_cov_2_structure_row.add_feature(astuple(genomic_range))
    for genomic_range in BuildGenomicRangeList().from_sars_cov_2_bed_file(
        ANALYSES_CONFIG.common.sars_cov_2_gene_ranges_bed_file_path
    )
]

restriction_enzymes_row = DiagramRow(
    f"Restriction enzymes",
    height_ratio=0.4,
    drawing_config={"fill_polygons": True, "annotation_color": "black"},
)
[
    restriction_enzymes_row.add_feature(astuple(genomic_range))
    for genomic_range in RunBatteryOfRangeTests()(
        genome=SoleSequenceFromFastaFile()(
            ANALYSES_CONFIG.common.sars_cov_2_genome_fasta_path
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
