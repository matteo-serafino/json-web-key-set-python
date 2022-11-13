# JSON Web Ket Set (JWKS)
Python methods to generate a RSA key pair and to create and validate JWT tokens.

If you like the idea or you find usefull this repo in your work, please leave a ⭐ to support this personal project.

## RSA Key Generation
```python
from rsa_key_generator import generate_key_pair

private_key, public_key = generate_key_pair(kid=str(uuid.uuid4()), save=True)
```
The save parameter set to true will save the private and the public key into two separate json files. 

## Example: Private and Public key pair
**Private Key**
```json
{
    "alg": "RS256",
    "d": "CJRQyEiep3HXYwRsJNtR1jWqUnt72D43CKJSwwc-VhMoVJbvqm2VPix3hhF9oTZkjJ7ExJ--I_FfolgCqyUHWpzD14LyghLo2yWBIJLZOUKRojzf_D8Lcg0N8hpAaIV8F7v5iQgDHGf7H_5KlXnI9ZNarNSQ7Rh1e_nFOwh4HjO_CvCM23t2jJ8ThfhY1ITG7dIF8O2zi61ppoDHaNmHhTvLcTdRMc6nqjhvLgQ9ovmWPe4p1bkO1DmFNkT-XgU8RhHLRVdI7aW3Wpm6PQi7uaBH590C9m7gd3zYLZaEWjayIc-ZRfJSYIug3ZkpWYlS2t26N4xKo_na3dbPhPJYhQ",
    "dp": "gH2VTWX1Oszul7SYJZzf9ihdU0P03GxqoKM3OBbS7-tKicXnAARUrVp2oA51Cuqa_99XW0pw07RJaG3pLHOJ1zSq0x-7BWgwzsYBO1yt-ypGfCXlgu03T_ULmZHjrEvQ8QCjD_tLnDiRtY9RFYw6KLAUwFoj2RGvdRAVqfo-6-U",
    "dq": "pvGPfjkIKLeNrJWq4rIhWZ7o5QhQ_hI8Vmcnq5e00ZWVn6GI9OrbXI-mJLbG6NVZBp6nYWJVCV0DdwKQLixlRN_qBxEPp7OcyusLumGi0XBRUyNpbrVSQ6KJ22MqPo11pKUS37Ia7TjIUOmTzSUQATH6enYecAiEgMNLl6_VynM",
    "e": "AQAB",
    "kid": "d813b2b6-94ff-4ad4-a884-38ee6922af71",
    "kty": "RSA",
    "n": "0--IymNJcEVdAdCjAZax4_fyHnk6i7rXEl5QOIvbEsSAgZ4t3ru_IddxbsbxTd-OCoxv4ANaxWGD4XkyxWYK9zsAglgBQagWMvvgjOEy3PPU2Slq7XnXxWErcAyX9P1Cy5wnd4NXwP9457k6jLmBJPzXAfQC3LhcSmv_Tjpkzhs4vdLgoESskfQR4q-H9IoBErTu_NDIBd86CKoC6DtTJwAqK3alSQvg41R-C924iyuNU30tathPh16PNA6k6nEpva93L19Fgfw4aqG8kQgtAhi0L51PbTpC6VaOivHUNxZ6MtbMPw39rfhS6yXg-JqgKyWpmmVtqtLQmwZSR7w7QQ",
    "p": "5XblIsbGQlduYF9tvuFqNSiGr_CnbFgOfT5SQSQO8o1ZFtBqhVFim8diQGieHEODAoqlkcQevJRCOEbGNus97EMJx1iRBaUbKCF78U7oBBNgYaMCa10PQeV9GGl0ql_wzGAu_mJULmeXSxTSCP56Kuc3xJ0gJzcLDhL3J7Ems_s",
    "q": "7HG3DH1Pg_wHqFddTkAINWwRIMC8wYpn6asiNftHEhOXYNb4NRZ1Hgp4nnmFsu9w2AbZXhlGNbVqv1qwGZATqHZMZYZ39RYJyMCyTjlxn-AmFPjIjLFUUDOuQ59Y4yLLU6XocoaYZC3FuzLc96gKnM9OxFj84tgWOaKgWyX87PM",
    "qi": "LDoB2LAFKvhdB_CeAZVDxm-TAgwK7v_LH4DndYvcfgs-3YldeJ7mMshVzT_Wc6t065f4M805Bum8v03eUNMw51HVcDNsrl1gszEafYe3g9_fSbrIc8LpQHyw26rxmNkFKKmUD8i6i-ouSL0gIEyyzNYDUkYxZgX_NVRBD_v54FM",
    "use": "sig"
}
```

**Public Key**
```json
{
    "alg": "RS256",
    "e": "AQAB",
    "kid": "d813b2b6-94ff-4ad4-a884-38ee6922af71",
    "kty": "RSA",
    "n": "0--IymNJcEVdAdCjAZax4_fyHnk6i7rXEl5QOIvbEsSAgZ4t3ru_IddxbsbxTd-OCoxv4ANaxWGD4XkyxWYK9zsAglgBQagWMvvgjOEy3PPU2Slq7XnXxWErcAyX9P1Cy5wnd4NXwP9457k6jLmBJPzXAfQC3LhcSmv_Tjpkzhs4vdLgoESskfQR4q-H9IoBErTu_NDIBd86CKoC6DtTJwAqK3alSQvg41R-C924iyuNU30tathPh16PNA6k6nEpva93L19Fgfw4aqG8kQgtAhi0L51PbTpC6VaOivHUNxZ6MtbMPw39rfhS6yXg-JqgKyWpmmVtqtLQmwZSR7w7QQ",
    "use": "sig"
}
```
## JWT Token Generation
```python
from jwt_token_generator import create_token

jwt_token = create_token(private_key=private_key, issuer="https://example.com", username="username", email="user.name@example.com")
```

## JWT Token Validation
```python
from jwt_token_generator import validate_token

is_valid, payload, exception = validate_token(jwt_token=jwt_token, public_key=public_key)
```

## Example: JWT token
```python
"eyJhbGciOiJSUzI1NiIsImtpZCI6ImQ4MTNiMmI2LTk0ZmYtNGFkNC1hODg0LTM4ZWU2OTIyYWY3MSIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiJmYTZjYzFkMC1kNDZkLTQwZDAtYTJlMy1lY2Y2MzkwOTYzYjYiLCJpc3MiOiJodHRwczovL2V4YW1wbGUuY29tIiwiYXVkIjpudWxsLCJzdWIiOiJ1c2VybmFtZSIsImVtYWlsIjoidXNlci5uYW1lQGV4YW1wbGUuY29tIiwibmJmIjoxNjY3MDczMzE3LCJpYXQiOjE2NjcwNzMzMTcsImV4cCI6MTY2NzA3NjkxNywianRpIjoiZjkwOTg1OWQtMjZhMy00Nzg5LTg1M2MtOWViNjQwYmNiZDU5In0.oE1rwzIg_JsB50N9WFMZQ_ZLgmuzv2qdqEoj92A4VYGZ_Ljgiv5vAg4gUjWVWrfcvukwgSiWdlam_OmEdaSqhnZMiFShTi8d6tPbnvqQr9oKlHoEx4a10musiwb-BmPaCx7Mw1zwOEI-UcPJTz4apCespTl9G3gV8lqw4-PfTA_uH8iIOgF7-IbM0CPITLkt2bd_ztI4BooXBwN2NNhk4ui3StXNplgdFULK73hH9HNvMNhD0nmJHYQdS95YdhdHCHHkoz9Kgx7MyrnJIgDSnxsxHd71itpNodi4GvCCv6BniWRtUOAeSNP3LhEz4vUIJB7K8cN4wwe21rejjYuILw"
```

### JWT Token Header (decoded)
```json
{
  "alg": "RS256",
  "kid": "d813b2b6-94ff-4ad4-a884-38ee6922af71",
  "typ": "JWT"
}
```

### JWT Token Body (decoded)
```json
{
  "uid": "fa6cc1d0-d46d-40d0-a2e3-ecf6390963b6",
  "iss": "https://example.com",
  "aud": null,
  "sub": "username",
  "email": "user.name@example.com",
  "nbf": 1667073317,
  "iat": 1667073317,
  "exp": 1667076917,
  "jti": "f909859d-26a3-4789-853c-9eb640bcbd59"
}
```

### Standard Claims [1]

* `iss` (issuer): Issuer of the JWT;
* `sub` (subject): Subject of the JWT (the user);
* `aud` (audience): Recipient for which the JWT is intended;
* `exp` (expiration time): Time after which the JWT expires;
* `nbf` (not before time): Time before which the JWT must not be accepted for processing;
* `iat` (issued at time): Time at which the JWT was issued; can be used to determine age of the JWT;
* `jti` (JWT ID): Unique identifier; can be used to prevent the JWT from being replayed (allows a token to be used only once);

## References
[1] [Auth0 Docs Tokens](https://auth0.com/docs/secure/tokens/json-web-tokens/json-web-token-claims)

[2] [jwt.io](https://jwt.io/)