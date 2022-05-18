from matplotlib import pyplot as plt
import genome_browser as gb

from .config_the_analysis import THE_CONFIG
from src.genomic_ranges import BuildGenomicRangeList
from src.diagram import LabeledFeature

genome_length = 29903

g = gb.GenomeDiagram()


# Plot 9 random interval features (random start, length, orientation, and color).
track = LabeledFeature("Random Intervals", height_ratio=0.4)

for genomic_range in BuildGenomicRangeList().from_bed_file(
    THE_CONFIG.input_bed_file_path
):
    # Feature must follow iterable as (position, width, strand, color)
    track.add_feature(genomic_range)

g.add_track(track)

# Annotate the figure with interval specific metadata. Will always appear in lower-right
g.annotation = "{}:{:,}-{:,}".format("chr3", 20000, 812383)

fig, axes = g.draw()
plt.show()
