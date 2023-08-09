import pandas as pd
import numpy as np
from scipy import optimize


def relation(x, m, n, c):
    return m * x**n + c


class Interpolator:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def linear_interpolate(self, n):
        # iloc so the functions are agnostic of column names
        x_values = self.data.iloc[:, 0]
        y_values = self.data.iloc[:, 1]
        return np.interp(n, xp=x_values, fp=y_values)

    def smart_interpolate(self, n):
        params, _ = optimize.curve_fit(
            relation, self.data.iloc[:, 0], self.data.iloc[:, 1]
        )
        return relation(n, *params)


if __name__ == "__main__":
    # add something to run here if you wish
    pass
