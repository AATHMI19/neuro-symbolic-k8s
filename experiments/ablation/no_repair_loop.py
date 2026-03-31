import time

def run():

    manifest = {
        "securityContext": {
            "runAsNonRoot": False
        }
    }

    start = time.perf_counter()

    violation_detected = manifest["securityContext"]["runAsNonRoot"] == False

    time.sleep(0.01)

    latency = time.perf_counter() - start

    print("Ablation: No Repair Loop")
    print("Violation detected:", violation_detected)
    print("Repair applied:", False)
    print("Latency:", round(latency,4))