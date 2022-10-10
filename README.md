# JSON Web Ket Set (JWKS)
Python methods to generate a RSA key pair and to create and validate JWT tokens.

If you like the idea or you find usefull this repo in your work, please leave a ⭐ to support this personal project.

## Documentation
Documentation goes here.

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

## Example of JWT token


Riferimenti al sito jwt.io
