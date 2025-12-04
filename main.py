from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes
import base64

app = FastAPI()

# Load private key once at startup
with open("private.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
    )

@app.post("/decrypt-seed", response_class=PlainTextResponse)
def decrypt_seed(encrypted_seed: str):
    # Base64 decode from query string
    decoded = base64.b64decode(encrypted_seed)

    # Decrypt RSA
    seed = private_key.decrypt(
        decoded,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Convert bytes → text
    return seed.decode()
