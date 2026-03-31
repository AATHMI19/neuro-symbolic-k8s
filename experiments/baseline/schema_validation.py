import time

def run():

    manifest = {
        "apiVersion": "v1",
        "kind": "Pod",
        "metadata": {"name": "demo"}
    }

    start = time.perf_counter()

    required_fields = ["apiVersion", "kind", "metadata"]

    valid = all(field in manifest for field in required_fields)

    latency = time.perf_counter() - start

    print("Baseline: Schema Validation")
    print("Schema valid:", valid)
    print("Security check performed:", False)
    print("Latency:", round(latency,4))