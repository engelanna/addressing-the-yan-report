class SoleSequenceFromFastaFile:
    def __call__(self, file_path: str):
        the_sequence = str()

        for line in open(file_path, "r"):
            if not line.startswith(">"):
                the_sequence += line.rstrip()

        return the_sequence
