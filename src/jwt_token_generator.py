import jwt
import uuid
from datetime import datetime

def create_token(private_key: str, issuer: str = None, username: str = None, email: str = None) -> str:

    headers = {
        'alg': private_key['alg'],
        'typ': 'JWT',
        'kid': private_key['kid']
    }

    payload = {
        'uid': str(uuid.uuid4()),
        'iss': issuer,
        'aud': None,
        'sub': username,
        'email': email,
        'nbf': int(datetime.now().timestamp()),
        'iat': int(datetime.now().timestamp()),
        'exp': int(datetime.now().timestamp()) + 3600,
        'jti': str(uuid.uuid4())
    }

    jwy_token = jwt.encode(
        payload,
        key=jwt.algorithms.RSAAlgorithm.from_jwk(private_key),
        algorithm="RS256",
        headers=headers
    )

    return jwy_token

def validate_token(jwt_token: str, public_key: str) -> dict:

    payload = jwt.decode(
        jwt=jwt_token, 
        key=jwt.algorithms.RSAAlgorithm.from_jwk(public_key),
        algorithms=["RS256"]
    )

    return payload