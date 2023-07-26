from random_coding_challenge.challenge_04 import INPUT_TEXT, regex_extract, unique

# write a function regex_extract, which has two arguments: string, and type
# type can be one of the following:
#  - "email"
#  - "domain_name"
#  - "username"
# The function should use Regular Expressions to extract and return a list of
# the (unique) full email addresses, domain names (the bit after the @ and before
# the .), or usernames (the bit before the @) from the string, depending on which type is chosen.


def test_emails():
    emails = regex_extract(INPUT_TEXT, "email")
    assert isinstance(emails, list)
    assert len(emails) == 5


def test_domain_names():
    domain_names = regex_extract(INPUT_TEXT, "domain_name")
    assert isinstance(domain_names, list)
    assert len(domain_names) == 3


def test_usernames():
    usernames = regex_extract(INPUT_TEXT, "username")
    assert isinstance(usernames, list)
    assert len(usernames) == 5


def test_unique():
    going_in = [2, 4, 5, 5, 5, 5, 5, 3, 1, 4, 5, 6, 3, 99]
    expected_out = [1, 2, 3, 4, 5, 6, 99]
    assert unique(going_in) == expected_out
