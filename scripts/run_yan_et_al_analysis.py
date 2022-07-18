from dataclasses import astuple
from matplotlib import pyplot as plt

from src.constants import ANALYSES_CONFIG, COLORS
from src.genome_browser_overrides import (
    DiagramRow,
    OverridenGenomeDiagram,
)
from src.genomic_range_builders import BuildGenomicRangeList
from src.loaders import SoleSequenceFromFastaFile
from src.matchers import NonoverlappingOccurrencesOfSequenceInGenome


genome = SoleSequenceFromFastaFile()(
    ANALYSES_CONFIG.common.sars_cov_2_genome_fasta_path
)


sars_cov_2_genetic_structure_row = DiagramRow(
    ANALYSES_CONFIG.yan_et_al.diagram_title,
    drawing_config={
        "annotation_color": COLORS.structure_annotation,
        "fill_polygons": True,
    },
)
[
    sars_cov_2_genetic_structure_row.add_feature(astuple(genomic_range))
    for genomic_range in BuildGenomicRangeList().from_sars_cov_2_bed_file(
        ANALYSES_CONFIG.common.sars_cov_2_gene_ranges_bed_file_path
    )
]


restriction_enzymes_row = DiagramRow(drawing_config={"fill_polygons": True})
[
    restriction_enzymes_row.add_feature(astuple(genomic_range))
    for genomic_range in BuildGenomicRangeList().from_search_results(
        genome,
        NonoverlappingOccurrencesOfSequenceInGenome(genome)("GAATTC")
        + NonoverlappingOccurrencesOfSequenceInGenome(genome)("GGTNACC"),
    )
]

diagram = OverridenGenomeDiagram()
diagram.add_track(sars_cov_2_genetic_structure_row)
diagram.add_track(restriction_enzymes_row)

_fig, _axes = diagram.draw()

plt.show()
