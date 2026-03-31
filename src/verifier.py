
def verify(manifest):
    violations=[]
    try:
        if not manifest["spec"]["containers"][0]["securityContext"].get("runAsNonRoot",False):
            violations.append("NonRootViolation")
    except:
        violations.append("InvalidManifest")
    return violations
