import os
from datetime import datetime

def run():

    log_folder = "audit_logs"
    os.makedirs(log_folder, exist_ok=True)

    log_file = os.path.join(log_folder, "pipeline_audit.log")

    steps = [
        "Manifest Generated",
        "Policy Verification Passed",
        "Security Repair Applied",
        "Deployment Approved"
    ]

    with open(log_file, "w") as f:
        for step in steps:
            entry = f"{datetime.now()} | {step}"
            f.write(entry + "\n")

    print("Governance: Audit Log Test")
    print("Total events logged:", len(steps))
    print("Audit log file:", log_file)