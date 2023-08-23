import pandas as pd
import pytest

from random_coding_challenge.adhoc_01 import cum_index_v1, cum_index_v2, EXAMPLE_DATA

input_2 = (
    pd.DataFrame(
        {
            "year": range(2016, 2024),
            "rate_change": [
                0.02,
                0.01,
                0.04,
                -0.1,
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

data = [
    {
        "input": EXAMPLE_DATA,
        "expected": pd.Series(
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
        ),
    },
    {
        "input": input_2,
        "expected": pd.Series(
            [
                1.11585,
                1.10481,
                1.06231,
                1.18035,
                1.10313,
                1.08150,
                1.05000,
                1.00000,
            ]
        ),
    },
]


@pytest.mark.parametrize("dictionary", data)
def test_cum_index_v1(dictionary):
    actual = cum_index_v1(dictionary["input"]["rate_change"])
    assert pytest.approx(actual, abs=0.001) == dictionary["expected"]


@pytest.mark.parametrize("dictionary", data)
def test_cum_index_v2(dictionary):
    actual = cum_index_v2(dictionary["input"]["rate_change"])
    assert pytest.approx(actual, abs=0.001) == dictionary["expected"]
