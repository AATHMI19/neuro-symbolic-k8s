
def generate_manifest(non_root=True):
    return {
        "apiVersion":"v1",
        "kind":"Pod",
        "metadata":{"name":"demo"},
        "spec":{"containers":[{
            "name":"app",
            "image":"nginx",
            "securityContext":{"runAsNonRoot":non_root}
        }]}
    }
