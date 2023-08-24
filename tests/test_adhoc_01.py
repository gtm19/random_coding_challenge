import pandas as pd
import pytest

from .data import RollingMultiply, RateChange

from random_coding_challenge.adhoc_01 import (
    cum_index_v1,
    cum_index_v2,
    rolling_multiply,
)


@pytest.mark.parametrize("dictionary", RateChange.data)
def test_cum_index_v1(dictionary):
    actual = cum_index_v1(dictionary["input"]["rate_change"])
    assert pytest.approx(dictionary["expected"], abs=0.001) == actual


@pytest.mark.parametrize("dictionary", RateChange.data)
def test_cum_index_v2(dictionary):
    actual = cum_index_v2(dictionary["input"]["rate_change"])
    assert pytest.approx(dictionary["expected"], abs=0.001) == actual


# rolling multiply tests
@pytest.mark.parametrize("dictionary", RollingMultiply.data)
def test_rolling_multiply(dictionary):
    actual = rolling_multiply(
        dictionary["x1"], dictionary["x2"], dictionary.get("truncate", False)
    )
    assert pytest.approx(dictionary["expected"], abs=0.001) == actual
