from typing import List


class SignatureToRangeList:
    """Given a signature like "xx____x":

    returns [
        ranges(0,2),
        ranges(6,7)
    ]
    """

    def __call__(self, signature: str):
        interesting_parts_of_signature = signature.strip("_")

        return self._from_signature(interesting_parts_of_signature, 0, [])

    def _from_signature(self, signature: str, range_start: int, range_list: List):
        print(f"Signature: {signature}")
        for i in range(1, len(signature)):

            previous_char = signature[i - 1]
            current_char = signature[i]
            is_final_iteration = i == len(signature) - 1

            if is_final_iteration:
                range_start = i
                range_list.append(range(range_start, i + 1))
            elif previous_char == "x" and current_char == "_":
                range_list.append(range(range_start, i))
            elif previous_char == "_" and current_char == "x":
                range_start = i

        return range_list
