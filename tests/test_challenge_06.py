import pytest
import numpy as np
from random_coding_challenge.challenge_06 import calculate_premiums

# Example risk matrix
risk_matrix = [
    [300, 800],
    [500, 200],
    [900, 700],
]

# Example rate matrix
rate_matrix = [
    [0.1, 0.15, 0.2],
    [0.08, 0.12, 0.16],
]

# Use numpy to calculate the expected result
expected = np.dot(risk_matrix, rate_matrix).tolist()


def test_matrix_multiply_solution():
    """
    Check that calculate_premiums() returns the same result as numpy.dot().
    (which calculates the dot product of two matrices)
    """
    actual = calculate_premiums(risk_matrix, rate_matrix)
    assert len(actual) == len(expected)
    assert len(actual[0]) == len(expected[0])
    assert actual == expected


class TestMatrixMultiplyErrors:
    non_rectangular_risk_matrix = [
        [300, 800],
        [500, 200],
        [900, 700, 100],
    ]

    non_rectangular_rate_matrix = [
        [0.1, 0.15, 0.2],
        [0.08, 0.12, 0.16],
        [0.08, 0.12, 0.16, 0.2],
    ]

    incompatible_dimensions_rate_matrix = [
        [0.1, 0.15, 0.2],
        [0.08, 0.12, 0.16],
        [0.08, 0.12, 0.16],
    ]

    def test_matrix_multiply_error_non_rect(self):
        """
        Checks that calculate_premiums() returns the correct error messages
        when one or both of the matrices are not rectangular (
        i.e. the rows are not of equal length)
        """
        with pytest.raises(ValueError):
            calculate_premiums(self.non_rectangular_risk_matrix, rate_matrix)

        with pytest.raises(ValueError):
            calculate_premiums(risk_matrix, self.non_rectangular_rate_matrix)

    def test_matrix_multiply_error_incompatible_dimensions(self):
        """
        Checks that calculate_premiums() returns the correct error message
        when the dimensions of the matrices are incompatible for matrix
        multiplication.
        """
        with pytest.raises(ValueError):
            calculate_premiums(risk_matrix, self.incompatible_dimensions_rate_matrix)
