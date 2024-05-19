import hashlib
import base64
import json

def generate_form_hash(form):
    """Generates the form hash for the given form."""
    # Calculate the SHA-256 digest of the form contents
    sha256 = hashlib.sha256()
    sha256.update(form.encode())
    digest = sha256.digest()

    # Base64 encode the digest
    form_hash = base64.b64encode(digest).decode()

    return form_hash

# Load the form from the JSON file
with open('test.json', 'r') as f:
    form = json.load(f)

# Generate the form hash
form_hash = generate_form_hash(json.dumps(form, indent=4))

print(f"Form hash: {form_hash}")