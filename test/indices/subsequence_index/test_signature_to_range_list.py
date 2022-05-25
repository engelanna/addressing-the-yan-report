from pytest import fixture

from src.indices import SignatureToRangeList


class TestSignatureToRangeList:
    @fixture
    def subject(self):
        return SignatureToRangeList()

    def test_multiple_spaces(self, subject, signature="xx____x"):
        assert [range(0, 2), range(6, 7)] == subject(signature)

    def test_middle_range(self, subject, signature="xx_xx_xx"):
        assert [range(0, 2), range(3, 5), range(7, 8)] == subject(signature)

    def test_drops_prefix_and_suffix(self, subject, signature="__x_x_"):
        assert [range(0, 1), range(2, 3)] == subject(signature)
