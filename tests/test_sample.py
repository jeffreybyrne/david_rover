import pytest


class TestSample:

    @pytest.mark.parametrize("num1, num2, num3", [(1, 1, 2),
                                                  (544, 99, 643),
                                                  (1000, -100, 900)])
    def test_sample(self, num1, num2, num3):
        assert num1 + num2 == num3
