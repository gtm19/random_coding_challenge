import pandas as pd
import pytest

from random_coding_challenge.adhoc_01 import cum_index_v1, cum_index_v2

data_frame = (
    pd.DataFrame(
        {
            "year": range(2016, 2024),
            "rate_change": [
                0.02,
                0.01,
                0.04,
                0.03,
                0.07,
                0.02,
                0.03,
                0.05,
            ],
        }
    )
    .set_index("year")
    .sort_index()
)

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
    actual = cum_index_v1(data_frame["rate_change"])
    assert pytest.approx(actual, abs=0.001) == expected


def test_cum_index_v2():
    actual = cum_index_v2(data_frame["rate_change"])
    assert pytest.approx(actual, abs=0.001) == expected
