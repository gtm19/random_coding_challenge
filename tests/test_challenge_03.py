import inspect
import pytest
from random_coding_challenge.challenge_03 import get_beer, get_url


def test_arg():
    """
    The get_beer function should have one argument, id, which is optional
    and defaults to None
    """
    params = inspect.signature(get_beer).parameters
    assert len(params) == 1
    assert "id" in params
    assert params["id"].default is None


def test_get_url():
    """
    The get_url function should have one argument, id, which is optional
    and defaults to None. It should return the url for the punkapi
    unless id is not None or an int, in which case it should raise a
    TypeError
    """
    assert get_url(12) == "https://api.punkapi.com/v2/beers/12"
    assert get_url() == "https://api.punkapi.com/v2/beers/random"
    with pytest.raises(TypeError):
        get_url("cheese")


@pytest.mark.parametrize("id", (42, None), ids=("specific", "random"))
def test_get_beer(id):
    """
    Test the get_beer function works. It should return a dict with the
    keys "name" and "abv".
    """
    beer = get_beer(id)
    assert isinstance(beer, dict)
    assert len(beer) == 2
    assert "name" in beer
    assert "abv" in beer


def test_get_beer_errors():
    """
    Test the get_beer function raises errors if the id is not an int or
    None, or if the id is not found.
    """
    with pytest.raises(TypeError):
        get_beer("cheese")
    with pytest.raises(RuntimeError):
        get_beer(1928172981739817)
