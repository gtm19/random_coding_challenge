from typing import Iterable
import pandas as pd

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
    # "invert" the series by dividing the max by each value
    return series.max() / series


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


if __name__ == "__main__":
    print(cum_index_v1(EXAMPLE_DATA["rate_change"]))
