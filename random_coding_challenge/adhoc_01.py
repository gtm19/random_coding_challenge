from typing import Sequence, Iterable
import pandas as pd
import numpy as np

EXAMPLE_DATA = (
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


def cum_index_v1(iterable: Iterable) -> pd.Series:
    series = pd.Series(list(iterable))
    # make first value 0
    series[0] = 0
    # add 1 to each value
    series = series + 1
    # cumulatively multiply
    series = series.cumprod()
    # "invert" the series by dividing the last value by each value
    return series.iat[-1] / series


def cum_index_v2(iterable: Iterable) -> pd.Series:
    values = list(iterable)
    # drop the first value
    values = values[1:]
    # add a 0 to the end and turn into a series
    values.append(0)
    series = pd.Series(values)
    # add 1 to each value
    series = series + 1
    # reverse the series
    series = series[::-1]
    # cumulatively multiply
    series = series.cumprod()
    # reverse the series again and return it
    return series[::-1]


def rolling_multiply(x1: Sequence, x2: Sequence, truncate: bool = False) -> Iterable:
    return_list = np.correlate(x1, x2, "full")[::-1]
    if truncate:
        return return_list[: len(x2)]
    return return_list


if __name__ == "__main__":
    print(cum_index_v1(EXAMPLE_DATA["rate_change"]))
