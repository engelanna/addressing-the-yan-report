from genome_browser import (
    ALPHA,
    ax_off,
    despine,
    disjoint_bins,
    Feature,
)
from itertools import chain as chain
from matplotlib import pyplot as plt
import matplotlib.patches as patches
from ostruct import OpenStruct


class DiagramRow(Feature):
    """
    Adds text labels to genomic intervals.
    Changes step to 1k.
    """

    def __init__(self, name=None, height_ratio=1, drawing_config: dict = None):
        Feature.__init__(self, name, height_ratio)
        self.step = 1000
        self.drawing_config = {
            "fill_polygons": False,
            "annotation_color": "slategrey",
            "padding": 0.3,
            **(drawing_config or {}),
        }

    @property
    def xlim(self):
        """Return a tuple of the smallest and largest break in all features."""
        edges = tuple(chain.from_iterable(self._intervals))
        return min(edges), max(edges) + 100

    def _plot(self, ax=None):
        if ax is None:
            ax = plt.gca()

        # Height of the features is some percent less than one.
        height = 1 / (self.drawing_config["padding"] + 1)

        # The non-overlapping disjoint intervals are computed using the
        # logic which priortizes first position of interval, then length.
        levels = list(disjoint_bins(self._intervals))

        for (position, width, strand, color, text_label), level in zip(
            self._sorted_features, levels
        ):
            # The polygon is simply a rectangle with two variable midpoints at
            # the middle of the left and right sides which act as anchors.
            # The four corners can be 'pulled back' (either left or right) to
            # simulate a directional rectangle.
            ax.add_patch(
                patches.Polygon(
                    [
                        [position, level],
                        [position, level + height / 2],
                        [position, level + height],
                        [position + width, level + height],
                        [position + width, level + height / 2],
                        [position + width, level],
                    ],
                    linewidth=0.5,
                    closed=True,
                    alpha=ALPHA,
                    fill=self.drawing_config["fill_polygons"],
                    color=color,
                )
            )
            ax.annotate(
                text_label,
                [position + width / 2, level + height / 2],
                color=self.drawing_config["annotation_color"],
                ha="center",
                va="center_baseline",
                rotation=45,
                rotation_mode="anchor",
            )

        # For features, remove y-axis by default.
        ax = despine(ax_off(ax, axis="y"))

        # Adjust y-limits to include self.drawing_config["padding, scales with the number of levels.
        ax.set_ylim(
            (0 - self.drawing_config["padding"]) * (max(levels) + 1) / 2,
            max(levels) + 1,
        )
        ax.set_xlim(*self.xlim)
        return ax
