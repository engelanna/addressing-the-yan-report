from dataclasses import astuple
from matplotlib import pyplot as plt

from src.constants.analyses_config import ANALYSES_CONFIG
from src.genome_browser_overrides import (
    DiagramRow,
    OverridenGenomeDiagram,
)
from src.builders.genomic_range_builders import BuildGenomicRangeList
from src.loaders import SoleSequenceFromFastaFile
from src.matchers import NonoverlappingOccurrencesOfSequenceInGenome
from src.restriction_enzyme_marks import RunBatteryOfRangeTests


genome = SoleSequenceFromFastaFile()(
    ANALYSES_CONFIG.martin_and_mercola.sars_cov_1_genome_fasta_path
)

sars_cov_1_structure_row = DiagramRow()
[
    sars_cov_1_structure_row.add_feature(astuple(genomic_range))
    for genomic_range in BuildGenomicRangeList().from_bed_file(
        ANALYSES_CONFIG.martin_and_mercola.sars_cov_1_gene_ranges_bed_file_path
    )
]

restriction_enzymes_row = DiagramRow()
[
    restriction_enzymes_row.add_feature(astuple(genomic_range))
    for genomic_range in BuildGenomicRangeList().from_search_results(
        genome,
        NonoverlappingOccurrencesOfSequenceInGenome(genome)("GCCNNNNNGGC")
        + NonoverlappingOccurrencesOfSequenceInGenome(genome)("CCANNNNNNTGG"),
    )
]

diagram = OverridenGenomeDiagram(ANALYSES_CONFIG.martin_and_mercola.diagram_title)
diagram.add_track(sars_cov_1_structure_row)
diagram.add_track(restriction_enzymes_row)

diagram.annotation = ANALYSES_CONFIG.martin_and_mercola.diagram_annotation
_fig, _axes = diagram.draw()
plt.show()
