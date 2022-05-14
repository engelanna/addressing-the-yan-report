from pytest import fixture

from src.chart import GenerateRangesForChart


class TestGenerateRangesForChart:
    @fixture
    def expected(self):
        return [
            (6364, 1495, "+", "#E74C3C"),
            (10094, 1495, "+", "#E74C3C"),
            (11610, 1495, "+", "#E74C3C"),
            (17555, 1495, "+", "#E74C3C"),
            (20470, 1495, "+", "#E74C3C"),
            (22685, 1495, "+", "#E74C3C"),
            (23760, 1495, "+", "#E74C3C"),
            (23760, 1495, "+", "#E74C3C"),
            (24791, 1495, "+", "#E74C3C"),
            (24992, 1495, "+", "#E74C3C"),
            (25506, 1495, "+", "#E74C3C"),
            (26201, 1495, "+", "#E74C3C"),
            (26939, 1495, "+", "#E74C3C"),
            (27006, 1495, "+", "#E74C3C"),
            (27118, 1495, "+", "#E74C3C"),
            (28461, 1495, "+", "#E74C3C"),
            (28618, 1495, "+", "#E74C3C"),
            (29139, 1495, "+", "#E74C3C"),
            (29147, 1495, "+", "#E74C3C"),
        ]

    def test(self, expected, len_genome=29903, genome_length_tolerance=0.05):
        actual = GenerateRangesForChart()(len_genome, genome_length_tolerance)

        assert expected == actual
