import os
from random_coding_challenge.challenge_02 import challenge_02

test_file_path = os.path.join("random_coding_challenge", "data", "002_test.txt")


def test_002_file_exists():
    assert os.path.exists(test_file_path)


def test_002_numbers():
    assert challenge_02(test_file_path) == 24_000
