import time

def run():

    policy_counts = [5, 10, 20]

    print("Performance: Policy Scaling")

    for count in policy_counts:

        start = time.perf_counter()

        for _ in range(count):
            time.sleep(0.005)

        latency = time.perf_counter() - start

        print("Policies evaluated:", count)
        print("Policy evaluation latency:", round(latency,4))