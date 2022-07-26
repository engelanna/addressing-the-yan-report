from ostruct import OpenStruct

COLORS = OpenStruct(
    hit="#6495ed",  # cornflower blue
    hit_alternate="limegreen",
    miss="white",
    structure="lightgrey",
    structure_annotation="black",
)

COLOR_FROM_RESTRICTION_ENZYME_NAME = lambda sequence: {
    "EcoRI": COLORS.hit,
    "BstEII": COLORS.hit_alternate,
    "BglI": COLORS.hit,
    "BstXI": COLORS.hit_alternate,
}.get(sequence, COLORS.structure_annotation)

sequence_sought_to_color = lambda sequence: {
    "GAATTC": COLORS.hit,
    "GGTNACC": COLORS.hit_alternate,
    "GGTCACC": COLORS.hit_alternate,
    "GGTGACC": COLORS.hit_alternate,
    "GGTTACC": COLORS.hit_alternate,
}.get(sequence, COLORS.miss)
