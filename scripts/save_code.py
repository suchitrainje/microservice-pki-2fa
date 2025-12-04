from totp import generate_totp
import time

code = generate_totp()
timestamp = int(time.time())

with open("/cron/last_code.txt", "w") as f:
    f.write(f"{timestamp},{code}\n")
