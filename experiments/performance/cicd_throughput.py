import time

def run():

    deployments = 10

    print("Performance: CI/CD Throughput Test")

    start = time.perf_counter()

    for i in range(deployments):
        time.sleep(0.02)

    total_time = time.perf_counter() - start

    throughput = deployments / total_time

    print("Deployments processed:", deployments)
    print("Total time:", round(total_time,3))
    print("Throughput (deployments/sec):", round(throughput,2))