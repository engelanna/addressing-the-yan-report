from dataclasses import astuple
from matplotlib import pyplot as plt

from .config_the_analysis import THE_CONFIG
from src.genomic_range_builders import BuildGenomicRangeList
from src.genome_browser_overrides import (
    OverridenGenomeDiagram,
    OverriddenFeature,
)

genome_length = 29903
g = OverridenGenomeDiagram()

# Plot SARS-CoV-2
track = OverriddenFeature(
    THE_CONFIG.sars_cov_2_structure_diagram.title, height_ratio=0.4
)
for genomic_range in BuildGenomicRangeList().from_sars_cov_2_bed_file(
    THE_CONFIG.sars_cov_2_structure_diagram.genes_bed_file
):
    track.add_feature(astuple(genomic_range))
g.add_track(track)

# Plot locations from patent
track = OverriddenFeature(f"Restriction enzymes", height_ratio=0.4)
for genomic_range in BuildGenomicRangeList().from_locations_in_patent(
    genome_length=genome_length, tolerance_as_fraction_of_genome_length=0.05
):
    track.add_feature(astuple(genomic_range))
g.add_track(track)


# Annotate the figure with interval specific metadata. Will always appear in lower-right
g.annotation = "{}:{:,}-{:,}".format("chr3", 20000, 812383)

fig, axes = g.draw()
plt.show()
