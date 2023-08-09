import pandas as pd
from random_coding_challenge.challenge_05 import Interpolator
import pytest

table = pd.DataFrame({"horse": [10, 20, 30], "bagels": [1000, 4000, 9000]})
curve = Interpolator(table)


def test_linear():
    assert curve.linear_interpolate(15) == 2500


@pytest.mark.filterwarnings("ignore:covariance")
def test_smart():
    assert curve.smart_interpolate(15) == pytest.approx(2250, abs=0.00001)
