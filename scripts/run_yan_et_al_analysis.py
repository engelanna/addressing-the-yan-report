from dataclasses import astuple
from matplotlib import pyplot as plt

from src.constants.analyses_config import ANALYSES_CONFIG
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

# Plot SARS-CoV-2
track = DiagramRow(
    ANALYSES_CONFIG.yan_et_al.diagram_title,
    height_ratio=0.4,
    drawing_config={"padding": 0},
)

[
    track.add_feature(astuple(genomic_range))
    for genomic_range in BuildGenomicRangeList().from_sars_cov_2_bed_file(
        ANALYSES_CONFIG.common.sars_cov_2_gene_ranges_bed_file_path
    )
]
[
    track.add_feature(astuple(genomic_range))
    for genomic_range in BuildGenomicRangeList().from_search_results(
        genome,
        NonoverlappingOccurrencesOfSequenceInGenome(genome)("GAATTC")
        + NonoverlappingOccurrencesOfSequenceInGenome(genome)("GGTNACC"),
    )
]


diagram = OverridenGenomeDiagram()
diagram.add_track(track)
fig, axes = diagram.draw()
plt.show()
