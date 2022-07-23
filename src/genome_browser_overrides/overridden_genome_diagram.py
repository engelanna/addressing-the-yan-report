from genome_browser import (
    # ASPECT,
    ax_off,
    cleanup_chart_junk,
    GenomeDiagram,
    # HSPACE,
)
from matplotlib import pyplot as plt
import numpy as np

ASPECT = 2.8
HSPACE = 0.0


class OverridenGenomeDiagram(GenomeDiagram):
    """
    Formats the xticks as 1k, 2k, ...
    """

    def draw(self):
        # Construct a one-column figure with rows that follow the height_ratios
        # defined in each of the tracks defined. At the moment only a generic
        # horizontal space parameter (HSPACE) is supplied, but spacing can be
        # tweaked post-draw.
        fig, axes = plt.subplots(
            nrows=len(self.tracks),
            ncols=1,
            figsize=(20, len(self.tracks) * 0.75 * ASPECT),
            gridspec_kw={
                "height_ratios": self.height_ratios,
                "hspace": HSPACE,
                "wspace": 0.0,
            },
        )

        # If this figure has a name, make it the title.
        if self.name is not None:
            fig.suptitle(self.name, x=0.5, y=0.94, fontsize=10, weight="bold")

        # If we are only plotting one track then put it in an iterable for zip.
        if len(self.tracks) == 1:
            axes = np.array([axes])

        for i, (ax, track) in enumerate(zip(axes.flatten(), self.tracks)):
            if track._empty is True:
                ax.axis("off")
                continue

            # Cleanup each track before plotting.
            ax = track._plot(cleanup_chart_junk(ax))

            # Set each ax to the limits of the greatest data range.
            ax.set_xlim(*self.xlim)

            # If this is not the last ax then turn off the x-axis. If not,
            # plot xticks at the step interval defined.
            if i != len(self.tracks) - 1:
                ax = ax_off(ax, axis="x")
            else:
                ax.spines["bottom"].set_visible(True)
                # Set the positions every step size after the 0-defined min.
                ax.set_xticks(range(*map(int, ax.get_xlim()), track.step))
                # Set the labels as numbers increasing by step, after 0.
                ax.set_xticklabels(
                    range(0, int(abs(np.subtract(*ax.get_xlim()))), track.step),
                    rotation=90,
                )
                ax.xaxis.set_major_formatter(lambda x, _pos: f"{x // 1000}k")
                # Figure annotations will be applied to the last ax in offset
                # coordinates in a lightgray text. Clipping is ignored as the
                # text clearly cips with the axes outboard frame.
                if self.annotation is not None:
                    ax.annotate(
                        xy=(1, 0),
                        xycoords="axes fraction",
                        text=self.annotation,
                        xytext=(0, -60),
                        textcoords="offset points",
                        va="bottom",
                        ha="right",
                        color="0.6",
                        clip_on=False,
                    )
        return fig, axes
