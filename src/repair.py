
def repair(manifest,violations):
    if "NonRootViolation" in violations:
        manifest["spec"]["containers"][0]["securityContext"]["runAsNonRoot"]=True
    return manifest
