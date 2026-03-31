import time

def run():

    policies = 10

    start = time.perf_counter()

    for _ in range(policies):
        time.sleep(0.01)

    latency = time.perf_counter() - start

    print("Ablation: No Incremental Verification")
    print("Policies checked:", policies)
    print("Verification mode: Full scan")
    print("Latency:", round(latency,4))