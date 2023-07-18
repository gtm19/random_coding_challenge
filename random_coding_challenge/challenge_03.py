import requests


def get_beer(id: int | None = None) -> dict:
    """
    Get a beer from the punkapi. If id is None, a random beer is returned.

    Args:
        id (int, optional): The id. Defaults to None.


    Returns:
        dict: A dict with the keys "name" and "abv"
    """
    url = get_url(id)

    response = requests.get(url)
    response_data = response.json()

    if response.status_code == 404:
        raise RuntimeError(response_data["message"])

    # if it doesn't error, a list of dicts is returned
    # so we need the first element
    response_data = response_data[0]

    return {k: v for k, v in response_data.items() if k in ["name", "abv"]}


def get_url(id: int | None = None) -> str:
    """
    Get the url for the punkapi. If id is None, the random url is returned.

    Args:
        id (int, optional): The id of the beer. Defaults to None.

    Returns:
        str: The url
    """
    if id is not None and not isinstance(id, int):
        raise TypeError(f"id must be of type int or None, not {type(id).__name__}")
    if id is None:
        return "https://api.punkapi.com/v2/beers/random"
    return f"https://api.punkapi.com/v2/beers/{id}"


if __name__ == "__main__":
    while True:
        id = input(
            "Input the id of a beer, or press Enter for a random beer\n> "
        ).strip()
        try:
            id = int(id)
        except ValueError:
            id = None
        beer = get_beer(id)
        print(
            f"The beer with {id=} is called {beer['name']} and has an ABV of {beer['abv']}%"
        )
