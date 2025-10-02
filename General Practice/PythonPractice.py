# crack_md5.py
import hashlib

target = "ca5bcaa95a6e7c55953aaf08d2b119fa"

def md5(s):
    return hashlib.md5(s.encode()).hexdigest()

# try plain digits up to 6
for n in range(0, 10**6):
    s = str(n)
    if md5(s) == target:
        print("FOUND (digits):", s)
        raise SystemExit

# try fixed 4-digit (0000-9999)
for n in range(10000):
    s = f"{n:04d}"
    if md5(s) == target:
        print("FOUND (4-digit):", s)
        raise SystemExit

# try TECH-FLAG-#### pattern
prefix = "TECH-FLAG-"
for n in range(10000):
    s = f"{prefix}{n:04d}"
    if md5(s) == target:
        print("FOUND (TECH-FLAG-####):", s)
        raise SystemExit

print("No match found in these small search spaces.")
