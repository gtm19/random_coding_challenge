from random_coding_challenge.challenge_03 import get_beer
import pytest

# Here is the criteria:

# You must define a function: get_beer

# The function should have a single parameter: id, which by default is None

# If the id is None, the function should fetch a random beer from https://api.punkapi.com/v2/beers/random

# if the id is an int, the function should fetch the specific beer relating to the id (e.g. https://api.punkapi.com/v2/beers/42)


# if the id is not None or an int, it should raise an appropriate error
def test_error_on_non_int():
    with pytest.raises(TypeError):
        get_beer("beer")
    with pytest.raises(TypeError):
        get_beer(19.2)


# The function should return a dictionary with the beer's name and abv
def test_return_value():
    info = get_beer(42)
    assert isinstance(info, dict)
    assert len(info) == 2
    assert "name" in info
    assert "abv" in info


def test_random_value():
    info = get_beer()
    assert isinstance(info, dict)
    assert len(info) == 2
    assert "name" in info
    assert "abv" in info


# FOR BONUS POINTS: if the id does not correspond to an actual beer on the API, raise an appropriate error (it will be useful to see what the output is in this scenario: check out https://api.punkapi.com/v2/beers/332987429872947, for example)
def test_error_on_non_beer():
    with pytest.raises(RuntimeError):
        info = get_beer(2943786298372938729837)
