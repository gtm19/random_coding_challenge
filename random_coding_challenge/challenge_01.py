# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


def challenge_01(number: int) -> int:
    """
    Calculates the sum of all multiples of 3 and 5 less than a given number

    Args:
        number (int): The given number

    Returns:
        int: The sum of all multiples of 3 and 5 less than `number`
    """
    threes = range(3, number, 3)
    fives = range(5, number, 5)

    # elements of a set are unique, so this ensures that
    # multiples of 3 _and_ 5 are not double counted
    without_dupes = set(list(threes) + list(fives))
    return sum(without_dupes)


if __name__ == "__main__":
    NUMBER = 1000
    print(f"The answer for challenge 1 where {NUMBER=} is:")
    print(f"{challenge_01(NUMBER):,}")
