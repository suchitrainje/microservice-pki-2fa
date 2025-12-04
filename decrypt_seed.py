import base64
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding


def decrypt_seed(encrypted_seed_b64: str, private_key) -> str:
    """
    Decrypt base64-encoded encrypted seed using RSA/OAEP (SHA256)
    """
    
    
    encrypted_seed = base64.b64decode(encrypted_seed_b64)

    
    decrypted_bytes = private_key.decrypt(
        encrypted_seed,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

   
    seed_hex = decrypted_bytes.decode('utf-8')

    
    if len(seed_hex) != 64:
        raise ValueError("Invalid seed – must be 64 characters")

    allowed = "0123456789abcdef"
    if any(c not in allowed for c in seed_hex.lower()):
        raise ValueError("Invalid seed – must be hexadecimal")

    return seed_hex


def load_private_key(path: str):
    """
    Load RSA private key from PEM
    """
    with open(path, 'rb') as f:
        return serialization.load_pem_private_key(
            f.read(),
            password=None
        )
