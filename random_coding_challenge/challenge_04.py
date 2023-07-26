import re
from typing import Iterable

INPUT_TEXT = """
In the bustling heart of BigData Corp., a team of actuaries sat hunched over their monitors, furrowed brows illuminated by Python code. Led by fearless Maria, a veteran actuary at maria.johansson@bigdatacorp.com, they were embracing the new language of data.

"Python isn't a beast," she would often say to calm the team, emailing them motivational snippets at workmail@teamactuary.com. John, the youngest, a wiz-kid at the actuarial tables, however, struggled. Python syntax was a different animal. He missed his semi-colons and static typing, venting to his friend at john-doe@old-school-math.com.

Then, a breakthrough occurred. Sofia, a bright newcomer with a knack for languages, found an ingenious solution. She started distributing "Python snippets of the day" at sofia.rodriguez@bigdatacorp.com. Simple, everyday codes - a warm-up for the team.

Day by day, the actuaries wrestled with Python, practicing Sofia's snippets. And with time, they were no longer just actuaries - they became data wranglers. Python was their new power tool.

One day, John, the resistant one, surprised everyone by writing an advanced data processing script. The email he sent from triumph@teamactuary.com read, "Python is no more a beast. Python is our friend."

And thus, BigData Corp.'s team of actuaries conquered Python, one email at a time.
"""


def unique(things: Iterable) -> list:
    """
    Take an iterable and return a list of unique items.

    Args:
        things (Iterable): Something iterable which may contain duplicates.

    Returns:
        list: A list of unique items from the iterable
    """
    return list(set(things))


def regex_extract(string: str, match_type: str) -> list[str]:
    """
    Extracts all emails, domain names, or usernames from a string.

    Args:
        string (str): The input string.
        match_type (str): What to extract from the string. Can be one of:
          - "email"
          - "domain_name"
          - "username"

    Returns:
        list[str]: A list of unique items extracted from the string.
    """
    regex_pattern = r"(?P<email>(?P<username>\S+)@(?P<domain_name>\S+)\.\S+\b)"
    matches = re.finditer(regex_pattern, string)

    return unique(match[match_type] for match in matches)


if __name__ == "__main__":
    print(regex_extract(INPUT_TEXT, "email"))
    print(regex_extract(INPUT_TEXT, "domain_name"))
