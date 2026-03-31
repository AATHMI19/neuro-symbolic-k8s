import yaml


def generate_k8s_yaml(user_input):
    k8s_objects = []

    app_name = user_input["application"]

    for svc in user_input["services"]:

        # 🔹 Deployment
        deployment = {
            "apiVersion": "apps/v1",
            "kind": "Deployment",
            "metadata": {
                "name": f"{svc['name']}-deployment"
            },
            "spec": {
                "replicas": svc["replicas"],
                "selector": {
                    "matchLabels": {
                        "app": svc["name"]
                    }
                },
                "template": {
                    "metadata": {
                        "labels": {
                            "app": svc["name"]
                        }
                    },
                    "spec": {
                        "containers": [
                            {
                                "name": svc["name"],
                                "image": svc["image"],
                                "ports": [
                                    {
                                        "containerPort": svc["port"]
                                    }
                                ],
                                "securityContext": {
                                    "runAsNonRoot": True
                                }
                            }
                        ]
                    }
                }
            }
        }

        # 🔹 Service
        service = {
            "apiVersion": "v1",
            "kind": "Service",
            "metadata": {
                "name": f"{svc['name']}-service"
            },
            "spec": {
                "selector": {
                    "app": svc["name"]
                },
                "ports": [
                    {
                        "protocol": "TCP",
                        "port": svc["port"],
                        "targetPort": svc["port"]
                    }
                ],
                "type": svc["exposure"]
            }
        }

        k8s_objects.append(deployment)
        k8s_objects.append(service)

    return k8s_objects


def save_yaml(objects, filename="k8s_output.yaml"):
    with open(filename, "w") as f:
        yaml.dump_all(objects, f, sort_keys=False)

    print(f"\n📄 Kubernetes YAML generated: {filename}")
