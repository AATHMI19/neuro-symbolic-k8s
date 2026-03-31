import time

def run():

    sizes = [1, 5, 10]

    print("Performance: Latency vs Manifest Size")

    for size in sizes:

        start = time.perf_counter()

        # simulate verification workload
        for _ in range(size):
            time.sleep(0.01)

        latency = time.perf_counter() - start

        print("Containers:", size)
        print("Verification latency:", round(latency,4))