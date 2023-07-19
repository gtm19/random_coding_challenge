import requests


def get_beer(id=None):
    if id is not None and not isinstance(id, int):
        raise TypeError(f"id must be None or of type int, not {type(id)}")

    if id is None:
        url_suffix = "random"
    else:
        url_suffix = id

    url = f"https://api.punkapi.com/v2/beers/{url_suffix}"

    response = requests.get(url)

    json = response.json()
    if response.status_code == 404:
        raise RuntimeError(json["message"])
    json = json[0]

    # Loopy way 1
    # return_data = {}
    # for key in ["name", "abv"]:
    #     return_data[key] = json[key]
    # return return_data

    # Loopy way 2
    # return_data = {}
    # for key in json:
    #     if key in ["name", "abv"]:
    #         return_data[key] = json[key]
    # return return_data

    # A note about dict.items()
    # say dict is {"name": "beer", "abv": 5.0}
    # then dict.items() is [("name", "beer"), ("abv", 5.0)]

    return {key: value for key, value in json.items() if key in ["name", "abv"]}
