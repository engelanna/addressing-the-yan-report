from genome_browser import (
    ALPHA,
    ax_off,
    despine,
    disjoint_bins,
    Feature,
    PADDING,
)
from itertools import chain as chain
from matplotlib import pyplot as plt
import matplotlib.patches as patches
import numpy as np


class OverriddenFeature(Feature):
    """
    Adds text labels to genomic intervals.
    Changes step to 1k.
    """

    def __init__(self, name=None, height_ratio=1):
        Feature.__init__(self, name, height_ratio)
        self.step = 1000

    @property
    def xlim(self):
        """Return a tuple of the smallest and largest break in all features."""
        edges = tuple(chain.from_iterable(self._intervals))
        return min(edges), max(edges) + 100

    def _plot(self, ax=None):
        if ax is None:
            ax = plt.gca()

        # Height of the features is some percent less than one.
        height = 1 / (PADDING + 1)

        # The non-overlapping disjoint intervals are computed using the
        # logic which priortizes first position of interval, then length.
        levels = list(disjoint_bins(self._intervals))

        # pull_back is the distance in units to pull back corners for
        # directional intervals
        pull_back = self.pullback * 0.005 * abs(np.subtract(*self.xlim))

        for (position, width, strand, color, text_label), level in zip(
            self._sorted_features, levels
        ):

            # pull_back is used on either the start or end of the interval
            # depending on the strand, if the pull_back is greater than the
            # width of the interval, then just pull back the entire width.
            start_taper = min(0, width)
            end_taper = min(0, width)

            # The polygon is simply a rectangle with two variable midpoints at
            # the middle of the left and right sides which act as anchors.
            # The four corners can be 'pulled back' (either left or right) to
            # simulate a directional rectangle.
            ax.add_patch(
                patches.Polygon(
                    [
                        [position + start_taper, level],
                        [position, level + height / 2],
                        [position + start_taper, level + height],
                        [position + width - end_taper, level + height],
                        [position + width, level + height / 2],
                        [position + width - end_taper, level],
                    ],
                    closed=True,
                    alpha=ALPHA,
                    fill=False,
                    color="orange",
                )
            )
            plt.text(
                position + width / 2,
                level + height / 2,
                text_label,
                color="blue",
                ha="center",
                va="center_baseline",
                rotation=45,
                rotation_mode="anchor",
            )

        # For features, remove y-axis by default.
        ax = despine(ax_off(ax, axis="y"))

        # Adjust y-limits to include padding, scales with the number of levels.
        ax.set_ylim((0 - PADDING) * (max(levels) + 1) / 2, max(levels) + 1)
        ax.set_xlim(*self.xlim)
        return ax
