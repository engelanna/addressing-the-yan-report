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
track = OverriddenFeature(f"{THE_CONFIG.subject_name} structure", height_ratio=0.4)
for genomic_range in BuildGenomicRangeList().from_sars_cov_2_bed_file(
    THE_CONFIG.input_bed_file_path
):
    track.add_feature(astuple(genomic_range))
g.add_track(track)

# Annotate the figure with interval specific metadata. Will always appear in lower-right
g.annotation = "{}:{:,}-{:,}".format("chr3", 20000, 812383)

fig, axes = g.draw()
plt.show()
