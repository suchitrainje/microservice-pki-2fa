from decrypt_seed import decrypt_seed, load_private_key
from totp import generate_totp_code, verify_totp_code

private_key = load_private_key("student_private.pem")

with open("encrypted_seed.txt", "r") as f:
    encrypted_seed = f.read().strip()


seed = decrypt_seed(encrypted_seed, private_key)
print("Seed:", seed)

code = generate_totp_code(seed)
print("Current 2FA Code:", code)

print("Verify:", verify_totp_code(seed, code))
