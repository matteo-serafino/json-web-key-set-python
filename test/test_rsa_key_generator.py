import unittest
import uuid
from src.rsa_key_generator import generate_key_pair

class TestRsaKeyGenerator(unittest.TestCase):
    def setUp(self) -> None:
        return None

    def test_key_generator(self):

        try:
            secret_key, public_key = generate_key_pair(
                kid=str(uuid.uuid4()),
                save=True
            )

            print(f"Your secret key:\n{secret_key}")

            print(f"Your public key {public_key}")

            assert True

        except Exception as ex:
            
            print(f"Exception: {ex}")

            assert False