import time

def run():

    manifest = {"runAsNonRoot": False}

    start = time.perf_counter()

    iterations = 0

    while manifest["runAsNonRoot"] == False:
        manifest["runAsNonRoot"] = True
        iterations += 1

    latency = time.perf_counter() - start

    print("Effectiveness: Repair Convergence")
    print("Repair iterations:", iterations)
    print("Final configuration:", manifest)
    print("Latency:", round(latency,4))