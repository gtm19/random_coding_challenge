import pandas as pd
import pytest

from random_coding_challenge.adhoc_01 import cum_index_v1, cum_index_v2, EXAMPLE_DATA

expected = pd.Series(
    [
        1.277,
        1.264,
        1.216,
        1.180,
        1.103,
        1.082,
        1.050,
        1.000,
    ]
)


def test_cum_index_v1():
    actual = cum_index_v1(EXAMPLE_DATA["rate_change"])
    assert pytest.approx(actual, abs=0.001) == expected


def test_cum_index_v2():
    actual = cum_index_v2(EXAMPLE_DATA["rate_change"])
    assert pytest.approx(actual, abs=0.001) == expected
