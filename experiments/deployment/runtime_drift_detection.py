import time

def run():

    verified_config = {"runAsNonRoot": True}
    runtime_config = {"runAsNonRoot": False}

    start = time.perf_counter()

    drift_detected = verified_config != runtime_config

    time.sleep(0.01)

    latency = time.perf_counter() - start

    print("Runtime Drift Detection")
    print("Expected config:", verified_config)
    print("Runtime config:", runtime_config)
    print("Drift detected:", drift_detected)
    print("Detection latency:", round(latency,4))