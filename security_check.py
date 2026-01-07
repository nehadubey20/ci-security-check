import sys
import os


HIGH_SEVERITY = ["API_KEY", "SECRET", "TOKEN"]
LOW_SEVERITY = ["PASSWORD"]

files_to_scan = ["app.py"]

issue_found=0

for file in files_to_scan:
    if not os.path.exists(file):
        continue

    with open(file,"r") as f:
        content =f.read()    

    for secret in HIGH_SEVERITY:
        if secret in content:
            print(f"[HIGH] Hardcoded secret found: {secret} in {file}")
            issues_found = True

    for secret in LOW_SEVERITY:
        if secret in content:
            print(f"[LOW] Potential secret found: {secret} in {file}")
        
        

if issues_found:
    print("Security scan failed.")
    sys.exit(1)

print("Security scan passed!!")    
