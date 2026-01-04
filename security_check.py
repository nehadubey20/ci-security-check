import sys

# Simulated insecure code
code = """
API_KEY = "12345-SECRET-KEY"
password = "admin123"
"""

secrets = ["API_KEY", "password", "SECRET"]

for secret in secrets:
    if secret in code:
        print(f"[SECURITY ISSUE] Hardcoded secret found: {secret}")
        sys.exit(1)

print("No security issues found.")
