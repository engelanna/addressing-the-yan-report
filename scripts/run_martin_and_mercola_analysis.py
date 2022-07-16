from dataclasses import astuple
from matplotlib import pyplot as plt

from .config_the_analyses import THE_CONFIG
from src.genome_browser_overrides import (
    OverridenGenomeDiagram,
    GeneticStructureFeature,
    RestrictionEnzymeCheckOutputFeature,
)
from src.genomic_range_builders import BuildGenomicRangeList
from src.loaders import SoleSequenceFromFastaFile
from src.restriction_enzyme_marks import RunBatteryOfRangeTests

diagram = OverridenGenomeDiagram()

# Plot SARS-CoV-2
track = GeneticStructureFeature(
    THE_CONFIG.sars_cov_2_structure_diagram.title, height_ratio=0.4
)
for genomic_range in BuildGenomicRangeList().from_sars_cov_2_bed_file(
    THE_CONFIG.sars_cov_2_structure_diagram.genes_bed_file
):
    track.add_feature(astuple(genomic_range))

diagram.add_track(track)

# Plot locations from patent
genome = SoleSequenceFromFastaFile()(THE_CONFIG.genome_under_test.fasta_file_path)

track = RestrictionEnzymeCheckOutputFeature(f"Restriction enzymes", height_ratio=0.4)
diagram.add_track(track)

for genomic_range in RunBatteryOfRangeTests()(genome, mismatches_allowed=1):
    track.add_feature(astuple(genomic_range))

# Annotate the figure with interval specific metadata. Will always appear in lower-right
diagram.annotation = "{}:{:,}-{:,}".format("chr3", 20000, 812383)

fig, axes = diagram.draw()
plt.show()
