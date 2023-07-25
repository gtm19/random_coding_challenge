import pytest

from random_coding_challenge.challenge_04 import INPUT_STRING, regex_extract


def test_email():
    emails = regex_extract(INPUT_STRING, "email")
    assert set(emails) == set(
        [
            "triumph@teamactuary.com",
            "john-doe@old-school-math.com",
            "maria.johansson@bigdatacorp.com",
            "sofia.rodriguez@bigdatacorp.com",
            "workmail@teamactuary.com",
        ]
    )


def test_domain():
    domain_names = regex_extract(INPUT_STRING, "domain_name")
    assert set(domain_names) == set(["teamactuary", "bigdatacorp", "old-school-math"])


def test_user_name():
    usernames = regex_extract(INPUT_STRING, "username")
    assert set(usernames) == set(
        [
            "workmail",
            "triumph",
            "maria.johansson",
            "sofia.rodriguez",
            "john-doe",
        ]
    )


def test_error():
    with pytest.raises(ValueError):
        regex_extract(INPUT_STRING, "banana")
