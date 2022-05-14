from collections import defaultdict


class FastaDictFromFile:
    def __init__(self, file_path):
        self.file_path = file_path
        self.entries = defaultdict(lambda: "")

    def __call__(self):
        if not self.entries:
            self._load_entries()

        return self.entries

    def _load_entries(self):
        for line in open(self.file_path, "r"):
            if line.startswith(">"):
                current_header = line.rstrip()
            else:
                self.entries[current_header] += line.rstrip()
