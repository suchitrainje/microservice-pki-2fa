import base64
import binascii
import pyotp


def hex_to_base32(hex_seed: str) -> str:
    """
    Convert 64-char hex seed to Base32 string
    """
    
    seed_bytes = binascii.unhexlify(hex_seed)

   
    return base64.b32encode(seed_bytes).decode('utf-8')


def generate_totp_code(hex_seed: str) -> str:
    """
    Generate current TOTP code (6 digits)
    """
    b32 = hex_to_base32(hex_seed)
    totp = pyotp.TOTP(b32)  
    return totp.now()


def verify_totp_code(hex_seed: str, code: str, valid_window: int = 1) -> bool:
    """
    Verify TOTP code from user
    """
    b32 = hex_to_base32(hex_seed)
    totp = pyotp.TOTP(b32)
    return totp.verify(code, valid_window=valid_window)
