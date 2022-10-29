import json
from jwcrypto import jwk

def generate_key_pair(kid: str = "my-app-prod", save: bool = False) -> tuple:

    key = jwk.JWK.generate(
        kty='RSA',
        size=2048,
        alg='RS256',
        use='sig',
        kid=kid
    )

    public_key = key.export_public()
    
    private_key = key.export_private()

    if save:
        save_key(public_key, private_key, "./keys")

    return public_key, private_key

def save_key(public_key, private_key, dir: str = "./") -> None:

    with open(f"{dir}/private_key.json", "w") as f:
        f.write(json.dumps(json.loads(private_key), indent=4))

    with open(f"{dir}/public_key.json", "w") as f:
        f.write(json.dumps(json.loads(public_key), indent=4))

    return None