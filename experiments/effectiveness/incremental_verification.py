import time

def run():

    policies = ["runAsNonRoot", "noPrivileged", "resourceLimits"]

    start = time.perf_counter()

    changed_policy = "runAsNonRoot"

    verified = []

    for p in policies:
        if p == changed_policy:
            time.sleep(0.01)
            verified.append(p)

    latency = time.perf_counter() - start

    print("Effectiveness: Incremental Verification")
    print("Policies total:", len(policies))
    print("Policies verified:", len(verified))
    print("Latency:", round(latency,4))