import json
import jwt
import uuid
from datetime import datetime
from jwcrypto import jwk

# Creazione di una coppia di chiavi RSA
key = jwk.JWK.generate(
    kty='RSA',
    size=2048,
    alg='RS256',
    use='sig',
    kid='prod_env'
)

# Estrazione della chiave pubblica
public_key = key.export_public()
# Estrazione della chiave privata
private_key = key.export_private()

with open("private_key.json", "w") as f:
    f.write(json.dumps(json.loads(private_key), indent=4))

with open("public_key.json", "w") as f:
    f.write(json.dumps(json.loads(public_key), indent=4))


with open("private_key.json", "r") as f:
    pri_key = json.load(f)

with open("public_key.json", "r") as f:
    jwks = json.load(f)

# Dal file della chiave privata prendo la chiave privata da usare per le firme.
k = jwt.algorithms.RSAAlgorithm.from_jwk(pri_key)

headers = {
    'alg': pri_key['alg'],
    'typ': 'JWT',
    'kid': pri_key['kid']
}

payload = {
    'userid': str(uuid.uuid4()),
    'username':'username',
    'exp': int(datetime.now().timestamp()) + 3600
}

token = jwt.encode(payload, k, "RS256", headers)

p = jwt.algorithms.RSAAlgorithm.from_jwk(jwks)

payload_decoded = jwt.decode(token, p, ["RS256"])

print(f"jwt token: {token}")