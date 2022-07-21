from pytest import fixture

from src.builders.chart_label_builders import ChartLabelFromGenomicRange


class TestChartLabelFromGenomicRange:
    @fixture
    def text_label(self):
        return "text label"

    @fixture
    def position(self):
        return 1000

    @fixture
    def width(self):
        return 500

    def test_range_printing_mode(self, text_label, position, width):
        actual = ChartLabelFromGenomicRange()(
            text_label, position, width, should_print_range=True
        )
        expected = f"{text_label}: {position}-{position + width}"

        assert expected == actual

    def test_no_range_printing_mode(self, text_label, position, width):
        actual = ChartLabelFromGenomicRange()(
            text_label, position, width, should_print_range=False
        )
        expected = f"{text_label}"

        assert expected == actual
