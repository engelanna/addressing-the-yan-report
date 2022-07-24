def sequence_sought_to_enzyme_name(sequence):
    return {
        "GAATTC": "EcoRI",
        "GGTNACC": "BstEII",
        "GCCNNNNNGGC": "BglI",
        "CCANNNNNNTGG": "BstXI",
    }[sequence]
