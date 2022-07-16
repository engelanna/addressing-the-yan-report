from dataclasses import astuple
from matplotlib import pyplot as plt

from .config_the_analyses import THE_CONFIG
from src.genome_browser_overrides import (
    OverridenGenomeDiagram,
    GeneticStructureRow,
    NoRestrictionEnzymeCheckRow,
)
from src.genomic_range_builders import BuildGenomicRangeList
from src.loaders import SoleSequenceFromFastaFile
from src.matchers import NonoverlappingOccurrencesOfSequenceInGenome

genome = SoleSequenceFromFastaFile()(THE_CONFIG.genome_under_test.fasta_file_path)

# Plot SARS-CoV-2
track = NoRestrictionEnzymeCheckRow(
    THE_CONFIG.sars_cov_2_structure_diagram.title, height_ratio=0.4
)

[
    track.add_feature(astuple(genomic_range))
    for genomic_range in BuildGenomicRangeList().from_sars_cov_2_bed_file(
        THE_CONFIG.sars_cov_2_structure_diagram.genes_bed_file
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
