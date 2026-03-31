import time

def run():

    start = time.perf_counter()

    manifest = {
        "apiVersion": "v1",
        "kind": "Pod",
        "metadata": {"name": "demo"},
        "spec": {
            "containers": [
                {
                    "name": "app",
                    "image": "nginx",
                    "securityContext": {"runAsNonRoot": False}
                }
            ]
        }
    }

    violation = manifest["spec"]["containers"][0]["securityContext"]["runAsNonRoot"] == False

    latency = time.perf_counter() - start

    print("Baseline: LLM Only Generation")
    print("Generated manifest:", manifest["metadata"]["name"])
    print("Security violation present:", violation)
    print("Latency:", round(latency,4))