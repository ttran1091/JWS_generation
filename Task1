import jwt
import datetime
import hashlib

# Provided credentials
username = "jws-test"
entity = "apex"
shared_secret = "1234567890"

# Create the payload
payload = {
    "username": username,
    "entity": entity,
    "datetime": datetime.datetime.utcnow().isoformat()
}

# Create the header
header = {
    "alg": "HS512"
}

# Create the JWS
jws = jwt.encode(payload, shared_secret.encode("utf-8"), algorithm="HS512", headers=header)

print("Generated JWS:", jws)