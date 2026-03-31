import os
import yaml
import random

def run():

    dataset_folder = "dataset_manifests"
    os.makedirs(dataset_folder, exist_ok=True)

    images = ["nginx", "redis", "node", "python"]
    security_options = [True, False]

    manifests_created = []

    for i in range(5):

        run_as_non_root = random.choice(security_options)

        manifest = {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {"name": f"demo-{i}"},
            "spec": {
                "containers": [
                    {
                        "name": "app",
                        "image": random.choice(images),
                        "securityContext": {
                            "runAsNonRoot": run_as_non_root
                        }
                    }
                ]
            }
        }

        file_path = os.path.join(dataset_folder, f"manifest_{i}.yaml")

        with open(file_path, "w") as f:
            yaml.dump(manifest, f)

        manifests_created.append((manifest["metadata"]["name"], run_as_non_root))

    print("Dataset Generation Complete")
    print("Total manifests:", len(manifests_created))

    for name, security in manifests_created:
        print("Manifest:", name, "| runAsNonRoot:", security)