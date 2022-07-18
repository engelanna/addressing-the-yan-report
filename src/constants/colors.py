from ostruct import OpenStruct

COLORS = OpenStruct(
    hit="limegreen",
    miss="lightgrey",
    structure="orange",
    structure_annotation="#6495ED",
)

COLOR_FROM_RESTRICTION_ENZYME_SEQUENCE = lambda sequence: {
    "GAATTC": COLORS.hit,
}.get(sequence, COLORS.miss)
