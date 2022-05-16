from genome_browser import (
    Feature,
    GenomeDiagram,
)


class BuildGenomeDiagram:
    def __init__(self, genomic_ranges: list, genome_length: int = 29903):
        self.diagram = GenomeDiagram()

    def __call__(self, genomic_ranges: list):
        track = Feature("Random Intervals", height_ratio=0.4)

        # Feature must follow iterable as (position, width, strand, color)
        [track.add_feature(grange) for grange in genomic_ranges]

        self.diagram.add_track(track)

        # Annotate the figure with interval specific metadata. Will always appear in lower-right
        self.diagram.annotation = "{}:{:,}-{:,}".format("chr3", 20000, 812383)

    def draw(self):
        diagram_drawing_result_tuple = self.diagram.draw()

        self.fig = diagram_drawing_result_tuple[0]
        self.axes = diagram_drawing_result_tuple[1]
