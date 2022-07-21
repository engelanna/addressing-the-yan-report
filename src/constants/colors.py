from ostruct import OpenStruct

COLORS = OpenStruct(
    hit="limegreen",
    hit_alternate="red",
    miss="slategrey",
    structure="darkorange",
    structure_annotation="blue",
)

COLOR_FROM_RESTRICTION_ENZYME_NAME = lambda sequence: {
    "EcoRI": COLORS.hit,
    "BstEII": COLORS.hit_alternate,
}.get(sequence, COLORS.structure_annotation)

COLOR_FROM_RESTRICTION_ENZYME_SEQUENCE = lambda sequence: {
    "GAATTC": COLORS.hit,
    "GGTAACC": COLORS.hit_alternate,
    "GGTCACC": COLORS.hit_alternate,
    "GGTGACC": COLORS.hit_alternate,
    "GGTTACC": COLORS.hit_alternate,
}.get(sequence, COLORS.miss)
