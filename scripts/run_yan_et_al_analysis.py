from dataclasses import astuple
from matplotlib import pyplot as plt

from src.constants import ANALYSES_CONFIG
from src.genome_browser_overrides import (
    DiagramRow,
    OverridenGenomeDiagram,
)
from src.builders.genomic_range_builders import BuildGenomicRangeList
from src.loaders import SoleSequenceFromFastaFile
from src.matchers import NonoverlappingOccurrencesOfSequenceInGenome


genome = SoleSequenceFromFastaFile()(
    ANALYSES_CONFIG.yan_et_al.sars_cov_2_genome_fasta_path
)


sars_cov_2_genetic_structure_row = DiagramRow()
[
    sars_cov_2_genetic_structure_row.add_feature(astuple(genomic_range))
    for genomic_range in BuildGenomicRangeList().from_bed_file(
        ANALYSES_CONFIG.yan_et_al.sars_cov_2_gene_ranges_bed_file_path
    )
]


restriction_enzymes_row = DiagramRow()
[
    restriction_enzymes_row.add_feature(astuple(genomic_range))
    for genomic_range in BuildGenomicRangeList().from_search_results(
        genome,
        NonoverlappingOccurrencesOfSequenceInGenome(genome)("GAATTC")
        + NonoverlappingOccurrencesOfSequenceInGenome(genome)("GGTNACC"),
    )
]

diagram = OverridenGenomeDiagram(ANALYSES_CONFIG.yan_et_al.diagram_title)
diagram.add_track(sars_cov_2_genetic_structure_row)
diagram.add_track(restriction_enzymes_row)

_fig, _axes = diagram.draw()
plt.show()
