import numpy as np
import genome_browser as gb

from matplotlib import pyplot as plt
from src.genomic_ranges import BuildGenomicRanges

genome_length = 29903

g = gb.GenomeDiagram()

# Plot a density of random data, interpolated and filled.
track1 = gb.Graph("Random Density")
track1.new_graph(
    x=np.arange(genome_length),
    y=np.abs(np.random.randn(genome_length)),
    fmt="interpolate",
    fill=True,
)

g.add_track(track1)

# Plot 9 random interval features (random start, length, orientation, and color).
track = gb.Feature("Random Intervals", height_ratio=0.4)
for genomic_range in BuildGenomicRanges()(genome_length):
    # Feature must follow iterable as (position, width, strand, color)
    track.add_feature(genomic_range)

g.add_track(track)

# Annotate the figure with interval specific metadata. Will always appear in lower-right
g.annotation = "{}:{:,}-{:,}".format("chr3", 20000, 812383)

fig, axes = g.draw()

plt.show()
