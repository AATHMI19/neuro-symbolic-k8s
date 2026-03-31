import time

def run():

    service = "demo-service"
    rollout_steps = [5, 25, 50, 100]

    print("Deployment Strategy: Canary")
    print("Service:", service)

    for step in rollout_steps:
        start = time.perf_counter()

        time.sleep(0.02)

        latency = time.perf_counter() - start

        print("Traffic Shift:", str(step) + "%")
        print("Stage latency:", round(latency,4))

    print("Deployment Status: SUCCESS")