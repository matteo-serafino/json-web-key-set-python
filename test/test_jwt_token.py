import json
import unittest
from src.jwt_token_generator import (
    create_token,
    validate_token
)

class TestJwtTokenGenerator(unittest.TestCase):
    def setUp(self) -> None:
        return None

    def test_create_token(self):

        with open("./keys/private_key.json", "r") as f:
            private_key = json.load(f)

        try:
            jwt_token = create_token(
                private_key=private_key,
                issuer="https://example.com",
                username="username",
                email="user.name@example.com"
            )

            print(f"Your JWT token:\n{jwt_token}")
        
            assert True
        
        except Exception as ex:
            print(f"Exception: {ex}")

            assert False

    def test_validate_token(self):

        with open("./keys/private_key.json", "r") as f:
            private_key = json.load(f)

        with open("./keys/public_key.json", "r") as f:
            public_key = json.load(f)

        jwt_token = create_token(
                private_key=private_key,
                issuer="https://example.com",
                username="username",
                email="user.name@example.com"
            )

        try:
            is_valid, payload, exception = validate_token(jwt_token=jwt_token, public_key=public_key)

            print(f"JWT token payload:\n{payload}")

            print(f"Exception:\n{exception}")

            assert is_valid

        except Exception as ex:

            print(f"Exception: {ex}")

            assert False