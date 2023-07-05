from random_coding_challenge.challenge_01 import challenge_01


def test_challenge_01():
    # for 10:
    # 3, 5, 6, 9 / sum = 23
    assert challenge_01(10) == 23
    # take 20:
    # 3, 5, 6, 9, 10, 12, 15, 18 / sum = 78
    assert challenge_01(20) == 78
