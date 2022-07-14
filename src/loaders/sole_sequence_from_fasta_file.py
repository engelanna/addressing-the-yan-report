class SoleSequenceFromFastaFile:
    """Accepts a single-entry FASTA file
    => discards the header, returning just the sequence.

    Raises AssertionError when the FASTA file is multi-sequence.
    """

    def __call__(self, file_path: str):

        the_sequence = ""
        header_already_encountered = False

        for line in open(file_path, "r"):
            if line.startswith(">") and header_already_encountered:
                raise AssertionError("Only 1 sequence allowed in the FASTA file")
            elif line.startswith(">"):
                header_already_encountered = True
            else:
                the_sequence += line.rstrip()

        return the_sequence
