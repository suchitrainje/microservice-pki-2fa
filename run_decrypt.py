from decrypt_seed import decrypt_seed, load_private_key

private_key = load_private_key("student_private.pem")

with open("encrypted_seed.txt", "r") as f:
    encrypted_seed_b64 = f.read().strip()

seed = decrypt_seed(encrypted_seed_b64, private_key)

print("Decrypted Seed:", seed)

with open("seed.txt", "w") as f:
    f.write(seed)
