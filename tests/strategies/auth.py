from binascii import hexlify

from hypothesis.strategies import (
    binary,
    booleans,
    characters,
    composite,
    dictionaries,
    fixed_dictionaries,
    integers,
    lists,
    none,
    one_of,
    sampled_from,
    shared,
    text,
    uuids,
)


@composite
def auth_refresh_response(draw):
    return {
        "jwtTokens": {
            "access": draw(text(min_size=1)),
            "refresh": draw(text(min_size=1)),
        },
        "permissions": {"owned": [], "requested": [], "granted": []},
        "access": draw(text(min_size=1)),
        "refresh": draw(text(min_size=1)),
    }


@composite
def auth_refresh_request(draw):
    return {
        "jwtTokens": {
            "access": draw(text(min_size=1)),
            "refresh": draw(text(min_size=1)),
        },
        "accessToken": draw(text(min_size=1)),
        "refreshToken": draw(text(min_size=1)),
    }


@composite
def auth_logout_request(draw):
    return {"global": draw(booleans())}


@composite
def auth_login_request(draw):
    return {
        "password": draw(text(min_size=1)),
        "username": draw(text(min_size=1)),
        "jwtLifetimes": {
            "access": draw(text(min_size=1)),
            "refresh": draw(text(min_size=1)),
        },
        "permissions": draw(lists(text(min_size=1))),
        "ethAddress": draw(text(min_size=1)),
        "userId": draw(text(min_size=1)),
    }
