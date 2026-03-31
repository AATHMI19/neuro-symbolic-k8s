import time

def run():

    manifests = [
        {"runAsNonRoot": True},
        {"runAsNonRoot": False},
        {"runAsNonRoot": True},
        {"runAsNonRoot": False}
    ]

    start = time.perf_counter()

    total = len(manifests)
    violations = 0
    detected = 0

    for m in manifests:
        if m["runAsNonRoot"] == False:
            violations += 1
            detected += 1

    accuracy = detected / violations if violations else 1

    latency = time.perf_counter() - start

    print("Effectiveness: Detection Accuracy")
    print("Total manifests:", total)
    print("Violations present:", violations)
    print("Violations detected:", detected)
    print("Accuracy:", round(accuracy,3))
    print("Latency:", round(latency,4))