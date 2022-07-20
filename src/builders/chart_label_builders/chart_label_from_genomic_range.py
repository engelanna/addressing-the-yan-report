class ChartLabelFromGenomicRange:
    def __call__(
        self, text_label: str, position: int, width: int, should_print_range=True
    ):
        return (
            f"{text_label}: {position}-{position+width}"
            if should_print_range
            else text_label
        )
