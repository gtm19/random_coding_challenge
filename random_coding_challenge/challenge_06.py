"""
You're working for an insurance company that needs to calculate premium amounts for different policyholders
based on their risk factors. Write a function called calculate_premiums that takes two matrices as input:
a risk matrix and a rate matrix. The risk matrix represents the risk factors of policyholders, and the
rate matrix represents the rates assigned to different risk categories.

In Python, these matrices are represented as a list of lists.

The risk matrix has dimensions rows(P) x cols(R), where P is the number of policyholders and R is the
number of risk factors.
The rate matrix has dimensions rows(R) x cols(C), where C is the number of rate categories.

Your function should calculate the premium amounts for each policyholder based on the risk factors and
the corresponding rates. The value in row i and column j of the result matrix should be calculated by
multiplying the elements of row i in the risk matrix with the elements of column j in the rate matrix
and then summing the products.

For example, if the risk matrix is:

[
    [300, 800],
    [500, 200],
    [900, 700],
]

And the rate matrix is:

[
    [0.1, 0.15, 0.2],
    [0.08, 0.12, 0.16],
]

The function should return the premium matrix:

[
    [94.0, 141.0, 188.0],
    [66.0, 99.0, 132.0],
    [146.0, 219.0, 292.0]
]

In addition, if either of the matrices is not rectangular (i.e. rows are not all the same length),
or their dimensions are not compatible for multiplication (i.e. the number of columns of the risk
matrix does not match the number of rows of the rate matrix), then the function should raise a
ValueError.

❗IMPORTANT❗: your solution CANNOT use the following:
    - nested `for`, `while`, or any other kinds of loops - you are better than this!
    - any imported functions/classes from numpy

Jack has proposed that the forfeit for ignoring this directive is that you will have to live code
the entirity of the 2023 Advent of Code dressed as the Grinch, and broadcast from the company 
LinkedIn account.

The tests have already been written for you (see `tests/test_challenge_06.py`), you just need to
write the functions. You can run `pytest -k challenge_06` in the terminal to see if your tests
pass.
"""


def calculate_premiums(risk_matrix: list, rate_matrix: list) -> list:
    if any(len(row) != len(risk_matrix[0]) for row in risk_matrix):
        raise ValueError("Risk matrix rows are not of equal length.")
    if any(len(row) != len(rate_matrix[0]) for row in rate_matrix):
        raise ValueError("Rate matrix rows are not of equal length.")
    if len(risk_matrix[0]) != len(rate_matrix):
        raise ValueError("Matrix dimensions are incompatible for premium calculation.")

    return [
        [
            sum(risk * rate for risk, rate in zip(risk_row, rate_col))
            for rate_col in zip(*rate_matrix)
        ]
        for risk_row in risk_matrix
    ]
