import time

def run():

    manifest = {
        "securityContext": {
            "runAsNonRoot": False
        }
    }

    start = time.perf_counter()

    violation = manifest["securityContext"]["runAsNonRoot"] == False

    latency = time.perf_counter() - start

    print("Baseline: Policy Validation Only")
    print("Policy rule checked: runAsNonRoot")
    print("Violation detected:", violation)
    print("Auto repair available:", False)
    print("Latency:", round(latency,4))