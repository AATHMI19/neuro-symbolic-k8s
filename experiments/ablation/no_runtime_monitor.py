import time

def run():

    deployed_manifest = {"runAsNonRoot": True}
    runtime_manifest = {"runAsNonRoot": False}

    start = time.perf_counter()

    drift_detected = False

    time.sleep(0.01)

    latency = time.perf_counter() - start

    print("Ablation: No Runtime Monitoring")
    print("Runtime drift detected:", drift_detected)
    print("System state: Drift ignored")
    print("Latency:", round(latency,4))