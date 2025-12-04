#!/usr/bin/env python3

import os
import sys
import base64
import time
from datetime import datetime, timezone

import pyotp

SEED_FILE_PATH = "/data/seed.txt"

def read_hex_seed():
    try:
        with open(SEED_FILE_PATH, "r") as f:
            hex_seed = f.read().strip()
            return hex_seed
    except FileNotFoundError:
        return None

def hex_to_base32(hex_seed: str) -> str:
        raw = bytes.fromhex(hex_seed)
        return base64.b32encode(raw).decode("utf-8")

def generate_totp(hex_seed: str) -> str:
        seed_b32 = hex_to_base32(hex_seed)
        totp = pyotp.TOTP(seed_b32)
        return totp.now()

def log_code():
        hex_seed = read_hex_seed()
        if not hex_seed:
            print("Seed not found")
            return

        code = generate_totp(hex_seed)
        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
        print(f"{timestamp} - 2FA Code: {code}")

if __name__ == "__main__":
        log_code()
